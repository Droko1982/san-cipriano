"""
Content views - Static pages
"""

import json
from datetime import date

from django.templatetags.static import static
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import get_language
from django.views.generic import TemplateView

from .guides import GUIDE_ORDER, GUIDES, PRICE_LIST
from .models import BiodiversityEntry, Experience, FAQ, BiodiversityCategory


class AboutView(TemplateView):
    """
    About San Cipriano page.
    History, location, community focus.
    """

    template_name = "content/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Sobre San Cipriano"
        return context


class BiodiversityView(TemplateView):
    """
    Biodiversity and experiences page.
    Uses TemplateView to avoid database dependency.
    """

    template_name = "content/biodiversity.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Biodiversidad y Experiencias"
        context["entries"] = []
        context["categories"] = {}
        context["experiences"] = []

        # Try to load from database, but don't fail if tables don't exist
        try:
            entries = BiodiversityEntry.objects.filter(is_active=True)
            context["entries"] = entries

            # Group entries by category
            for cat_value, cat_label in BiodiversityCategory.choices:
                cat_entries = entries.filter(category=cat_value)
                if cat_entries.exists():
                    context["categories"][cat_label] = cat_entries

            # Add experiences
            context["experiences"] = Experience.objects.filter(is_active=True)
        except Exception:
            # Database tables don't exist yet - template will show static content
            pass

        return context


class FAQView(TemplateView):
    """
    Frequently asked questions page.
    Uses TemplateView to avoid database dependency.
    """

    template_name = "content/faq.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Preguntas Frecuentes"
        context["faqs"] = []

        # Try to load from database, but don't fail if tables don't exist
        try:
            context["faqs"] = FAQ.objects.filter(is_active=True)
        except Exception:
            pass

        return context


class GuideView(TemplateView):
    """
    Travel guide pages (how to get there, prices, brujitas, things to do).
    Template and guide_key are set per URL in guide_urls.py; SEO texts and
    FAQs live in guides.py so the page and its JSON-LD always match.
    """

    guide_key = None

    # Bump GUIDE_UPDATED when the guides' content (prices, routes) is reviewed.
    # Shown on the page and used as dateModified in the Article schema.
    GUIDE_PUBLISHED = date(2026, 11, 18)
    GUIDE_UPDATED = date(2026, 11, 18)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        guide = GUIDES[self.guide_key]
        base_url = f"{self.request.scheme}://{self.request.get_host()}"

        context["guide"] = guide
        context["guide_published"] = self.GUIDE_PUBLISHED
        context["guide_updated"] = self.GUIDE_UPDATED
        context["related_guides"] = [
            {**GUIDES[key], "url": reverse(GUIDES[key]["url_name"])}
            for key in GUIDE_ORDER
            if key != self.guide_key
        ]
        if self.guide_key == "prices":
            context["price_list"] = PRICE_LIST
        context["guide_schema"] = self._build_schema(guide, base_url)
        return context

    def _build_schema(self, guide, base_url):
        page_url = f"{base_url}{self.request.path}"
        image_url = f"{base_url}{static(guide['image'])}"
        graph = [
            {
                "@type": "Article",
                "@id": f"{page_url}#article",
                "headline": str(guide["title"]),
                "description": str(guide["meta_description"]),
                "image": image_url,
                "inLanguage": get_language(),
                "datePublished": self.GUIDE_PUBLISHED.isoformat(),
                "dateModified": self.GUIDE_UPDATED.isoformat(),
                "mainEntityOfPage": page_url,
                "author": {"@id": f"{base_url}/#organization"},
                "publisher": {"@id": f"{base_url}/#organization"},
                "about": {"@id": f"{base_url}/#attraction"},
            },
            {
                "@type": "FAQPage",
                "@id": f"{page_url}#faq",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": str(question),
                        "acceptedAnswer": {"@type": "Answer", "text": str(answer)},
                    }
                    for question, answer in guide["faqs"]
                ],
            },
        ]
        if self.guide_key == "prices":
            offers = []
            for item in PRICE_LIST:
                offer = {"@type": "Offer", "name": str(item["name"]), "priceCurrency": "COP"}
                if item["high"]:
                    offer["priceSpecification"] = {
                        "@type": "PriceSpecification",
                        "minPrice": item["low"],
                        "maxPrice": item["high"],
                        "priceCurrency": "COP",
                    }
                else:
                    offer["price"] = item["low"]
                offers.append(offer)
            graph.append({
                "@type": "OfferCatalog",
                "@id": f"{page_url}#prices",
                "name": str(guide["h1"]),
                "itemListElement": offers,
            })
        data = {"@context": "https://schema.org", "@graph": graph}
        # Escape "</" so a translated string can never close the <script> tag.
        return mark_safe(json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))


class ContactView(TemplateView):
    """
    Contact page with WhatsApp and email info.
    """

    template_name = "content/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Contacto"
        return context
