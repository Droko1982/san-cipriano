"""
Visitors views - Form handling and counter
"""

from urllib.parse import quote

from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils import translation
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, TemplateView

from apps.core.utils import get_client_ip
from .forms import VisitorInquiryForm
from .models import VisitorInquiry, VisitorCounter


def build_inquiry_whatsapp_url(inquiry):
    """Build a wa.me link to the community with the inquiry details prefilled,
    so the visitor's request actually reaches the community's WhatsApp chat.
    The message is composed in Spanish (the community's language)."""
    def fmt_date(d):
        return d.strftime("%Y-%m-%d") if d else "Por definir"

    with translation.override("es"):
        services = ", ".join(str(s) for s in inquiry.services_display) or "No especificado"

    lines = [
        "Hola San Cipriano 🌿 Quiero planificar mi visita:",
        "",
        f"👤 Nombre: {inquiry.full_name}",
        f"📱 Tel/WhatsApp: {inquiry.phone}",
        f"✉️ Correo: {inquiry.email}",
        f"📍 Ciudad/País: {inquiry.city}, {inquiry.country}",
        f"📅 Llegada: {fmt_date(inquiry.estimated_arrival)} · Salida: {fmt_date(inquiry.estimated_departure)}",
        f"👥 Personas: {inquiry.number_of_people} (menores: {inquiry.number_of_children})",
        f"🎯 Servicios: {services}",
    ]
    if inquiry.special_requests:
        lines.append(f"📝 Solicitudes: {inquiry.special_requests}")

    # Resolve the community number the same way as the site-wide context
    # processor (DB config first, then settings) so all WhatsApp links match.
    community_whatsapp = getattr(settings, "COMMUNITY_WHATSAPP", "+573160592569")
    try:
        from apps.core.models import SiteConfiguration
        cfg = SiteConfiguration.get_config()
        if cfg and getattr(cfg, "community_whatsapp", None):
            community_whatsapp = cfg.community_whatsapp
    except Exception:
        pass

    number = community_whatsapp.lstrip("+").replace(" ", "")
    return f"https://wa.me/{number}?text={quote(chr(10).join(lines))}"


class InquiryFormView(CreateView):
    """
    Main inquiry form view.
    This is the central form that visitors must complete to receive detailed information.
    """

    model = VisitorInquiry
    form_class = VisitorInquiryForm
    template_name = "visitors/inquiry_form.html"
    success_url = reverse_lazy("visitors:thank_you")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = _("Planifica tu Visita")
        context["page_description"] = _(
            "Completa el formulario y recibirás información personalizada "
            "sobre tu visita a San Cipriano."
        )
        return context

    def form_valid(self, form):
        # Save visitor metadata
        form.instance.source_language = self.request.LANGUAGE_CODE
        form.instance.ip_address = get_client_ip(self.request)
        form.instance.user_agent = self.request.META.get("HTTP_USER_AGENT", "")

        response = super().form_valid(form)

        # Increment visitor counter
        counter = VisitorCounter.get_counter()
        counter.increment()

        # Build a WhatsApp handoff link with the inquiry details so the request
        # actually reaches the community's chat (the thank-you page uses this).
        self.request.session["inquiry_wa_url"] = build_inquiry_whatsapp_url(self.object)

        # Trigger notifications (handled by signals)
        messages.success(
            self.request,
            _("¡Gracias! Hemos recibido tu solicitud. La comunidad te contactará pronto.")
        )

        return response


class ThankYouView(TemplateView):
    """
    Thank you page shown after form submission.
    """

    template_name = "visitors/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = _("¡Gracias por tu interés!")
        # One-time WhatsApp handoff URL built from the submitted inquiry.
        context["inquiry_wa_url"] = self.request.session.pop("inquiry_wa_url", None)
        return context


class ServicesView(TemplateView):
    """
    Services overview page (without prices).
    Shows available services with descriptions but no pricing.
    """

    template_name = "visitors/services.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = _("Servicios")
        context["services"] = [
            {
                "icon": "🏠",
                "name": _("Hospedaje"),
                "description": _("Hoteles y alojamientos comunitarios en armonía con la naturaleza."),
            },
            {
                "icon": "🍽️",
                "name": _("Alimentación"),
                "description": _("Gastronomía local preparada por la comunidad con productos frescos."),
            },
            {
                "icon": "🚃",
                "name": _("Transporte en Brujitas"),
                "description": _("La experiencia única de viajar en los famosos carros sobre rieles."),
            },
            {
                "icon": "🅿️",
                "name": _("Parqueadero"),
                "description": _("Estacionamiento seguro y vigilado para tu vehículo."),
            },
            {
                "icon": "🎫",
                "name": _("Entrada a la Reserva"),
                "description": _("Acceso a los senderos, ríos y espacios naturales de la reserva."),
            },
            {
                "icon": "🧭",
                "name": _("Tours Guiados"),
                "description": _("Recorridos con guías locales que conocen cada rincón de la reserva."),
            },
            {
                "icon": "🌿",
                "name": _("Experiencias Naturales"),
                "description": _("Avistamiento de aves, senderismo, y contacto directo con la biodiversidad."),
            },
        ]
        return context
