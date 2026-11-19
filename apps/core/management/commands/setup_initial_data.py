"""
Management command to create initial data for San Cipriano site.
"""

from django.core.management.base import BaseCommand

from apps.core.models import SiteConfiguration
from apps.visitors.models import VisitorCounter
from apps.content.models import BiodiversityEntry, Experience, FAQ


class Command(BaseCommand):
    help = "Create initial data for San Cipriano site"

    def handle(self, *args, **options):
        self.stdout.write("Creating initial data for San Cipriano...")

        # Site Configuration
        config, created = SiteConfiguration.objects.get_or_create(
            pk=1,
            defaults={
                "site_name": "San Cipriano",
                "tagline": "Reserva Natural Comunitaria",
                "welcome_message": "Bienvenidos a San Cipriano, una reserva natural cuidada por su comunidad.",
                "community_whatsapp": "+573160592569",
                "community_email": "",
                "visitor_counter_base": 45,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS("✓ Site configuration created"))
        else:
            self.stdout.write("  Site configuration already exists")

        # Visitor Counter
        counter, created = VisitorCounter.objects.get_or_create(
            pk=1,
            defaults={
                "base_count": 45,
                "inquiry_count": 0,
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS("✓ Visitor counter created (starts at 45)"))
        else:
            self.stdout.write(f"  Visitor counter exists: {counter.total_count}")

        # Biodiversity Entries
        biodiversity_data = [
            {
                "name": "Tucán Pico Iris",
                "scientific_name": "Ramphastos sulfuratus",
                "category": "aves",
                "description": "Ave icónica de la selva húmeda, reconocible por su enorme pico multicolor. Se alimenta principalmente de frutas y es fundamental para la dispersión de semillas.",
                "conservation_status": "Preocupación menor",
                "is_featured": True,
            },
            {
                "name": "Colibrí Ermitaño",
                "scientific_name": "Phaethornis guy",
                "category": "aves",
                "description": "Pequeño colibrí de cola larga que habita en el sotobosque. Polinizador esencial de las heliconias y otras flores tubulares.",
                "conservation_status": "Preocupación menor",
                "is_featured": True,
            },
            {
                "name": "Tangara Dorada",
                "scientific_name": "Tangara arthus",
                "category": "aves",
                "description": "Hermosa ave de plumaje dorado y negro. Viaja en bandadas mixtas buscando frutas e insectos en el dosel del bosque.",
                "conservation_status": "Preocupación menor",
                "is_featured": False,
            },
            {
                "name": "Rana Venenosa Dorada",
                "scientific_name": "Phyllobates terribilis",
                "category": "anfibios",
                "description": "Una de las ranas más venenosas del mundo. Su brillante color amarillo advierte a los depredadores de su toxicidad. Las comunidades indígenas usaban su veneno para las puntas de sus dardos.",
                "conservation_status": "En peligro",
                "is_featured": True,
            },
            {
                "name": "Rana de Cristal",
                "scientific_name": "Centrolenidae",
                "category": "anfibios",
                "description": "Fascinante familia de ranas con piel translúcida que permite ver sus órganos internos. Habitan cerca de arroyos y son indicadores de la calidad del agua.",
                "conservation_status": "Vulnerable",
                "is_featured": True,
            },
            {
                "name": "Rana Dardo Roja",
                "scientific_name": "Oophaga pumilio",
                "category": "anfibios",
                "description": "Pequeña rana de intenso color rojo. Los machos cuidan los huevos y transportan los renacuajos a fuentes de agua seguras.",
                "conservation_status": "Preocupación menor",
                "is_featured": False,
            },
            {
                "name": "Mono Aullador",
                "scientific_name": "Alouatta seniculus",
                "category": "mamiferos",
                "description": "Su potente aullido puede escucharse a kilómetros de distancia. Vive en grupos familiares en las copas de los árboles alimentándose de hojas y frutas.",
                "conservation_status": "Preocupación menor",
                "is_featured": True,
            },
            {
                "name": "Perezoso de Tres Dedos",
                "scientific_name": "Bradypus variegatus",
                "category": "mamiferos",
                "description": "Mamífero arbóreo que pasa la mayor parte de su vida colgado de las ramas. Su pelaje alberga algas y hongos que le ayudan a camuflarse.",
                "conservation_status": "Preocupación menor",
                "is_featured": True,
            },
            {
                "name": "Heliconia Rostrata",
                "scientific_name": "Heliconia rostrata",
                "category": "flora",
                "description": "Espectacular planta tropical con inflorescencias rojas colgantes en forma de pinzas de langosta. Atrae colibríes y es emblemática del bosque húmedo.",
                "conservation_status": "No evaluada",
                "is_featured": True,
            },
            {
                "name": "Orquídea del Pacífico",
                "scientific_name": "Epidendrum spp.",
                "category": "flora",
                "description": "Familia diversa de orquídeas epífitas que crecen sobre los árboles. Sus delicadas flores son un tesoro del bosque nublado.",
                "conservation_status": "Variable",
                "is_featured": True,
            },
            {
                "name": "Mariposa Morpho Azul",
                "scientific_name": "Morpho peleides",
                "category": "insectos",
                "description": "Impresionante mariposa de alas azul iridiscente. El color no proviene de pigmento sino de la estructura de las escamas que refractan la luz.",
                "conservation_status": "Preocupación menor",
                "is_featured": True,
            },
        ]

        for data in biodiversity_data:
            entry, created = BiodiversityEntry.objects.get_or_create(
                name=data["name"],
                defaults=data
            )
            if created:
                self.stdout.write(f"  ✓ Biodiversity: {data['name']}")

        self.stdout.write(self.style.SUCCESS(f"✓ {BiodiversityEntry.objects.count()} biodiversity entries"))

        # Experiences
        experiences_data = [
            {
                "name": "Avistamiento de Aves",
                "description": "Recorridos al amanecer con guías expertos para observar las más de 200 especies de aves que habitan la reserva. Tucanes, colibríes, tangaras y muchas más.",
                "duration_info": "3-4 horas",
                "difficulty": "Fácil",
                "icon": "🐦",
                "is_featured": True,
                "order": 1,
            },
            {
                "name": "Senderismo en la Selva",
                "description": "Caminatas guiadas por senderos ancestrales, conociendo la flora y fauna local. Aprende sobre plantas medicinales y el ecosistema del bosque húmedo.",
                "duration_info": "2-5 horas",
                "difficulty": "Moderado",
                "icon": "🥾",
                "is_featured": True,
                "order": 2,
            },
            {
                "name": "Baño en Charcos Naturales",
                "description": "Disfruta de las aguas cristalinas del río San Cipriano en charcos naturales supervisados. Refréscate rodeado de selva virgen.",
                "duration_info": "Libre",
                "difficulty": "Fácil",
                "icon": "🏊",
                "is_featured": True,
                "order": 3,
            },
            {
                "name": "Tour Nocturno de Ranas",
                "description": "Expedición nocturna para descubrir las ranas venenosas y otras especies que cobran vida cuando cae el sol. Una experiencia mágica e inolvidable.",
                "duration_info": "2-3 horas",
                "difficulty": "Fácil",
                "icon": "🐸",
                "is_featured": True,
                "order": 4,
            },
            {
                "name": "Viaje en Brujita",
                "description": "La experiencia única de viajar en los tradicionales carros sobre rieles impulsados por motocicletas. Una aventura que solo encontrarás en San Cipriano.",
                "duration_info": "15-20 minutos",
                "difficulty": "Fácil",
                "icon": "🚃",
                "is_featured": True,
                "order": 5,
            },
            {
                "name": "Observación de Mariposas",
                "description": "Recorrido por los jardines de mariposas naturales donde podrás ver morphos azules y decenas de especies multicolores.",
                "duration_info": "1-2 horas",
                "difficulty": "Fácil",
                "icon": "🦋",
                "is_featured": False,
                "order": 6,
            },
        ]

        for data in experiences_data:
            exp, created = Experience.objects.get_or_create(
                name=data["name"],
                defaults=data
            )
            if created:
                self.stdout.write(f"  ✓ Experience: {data['name']}")

        self.stdout.write(self.style.SUCCESS(f"✓ {Experience.objects.count()} experiences"))

        # FAQs
        faqs_data = [
            {
                "question": "¿Cómo llego a San Cipriano?",
                "answer": "San Cipriano se encuentra cerca de Buenaventura, Valle del Cauca. Las indicaciones exactas de llegada se proporcionan después de completar el formulario de registro. Esto nos ayuda a proteger la reserva y garantizar una visita organizada. Generalmente se llega en vehículo hasta un punto de encuentro donde abordas las famosas 'brujitas'.",
                "order": 1,
            },
            {
                "question": "¿Cuánto cuesta visitar San Cipriano?",
                "answer": "Los costos varían según los servicios que necesites (hospedaje, alimentación, tours, transporte), el número de personas y la duración de tu estadía. Una vez completes el formulario, te enviaremos información personalizada con precios exactos. Esto nos permite ofrecerte opciones que se ajusten a tu presupuesto.",
                "order": 2,
            },
            {
                "question": "¿Necesito reservar con anticipación?",
                "answer": "Sí, recomendamos contactarnos con al menos una semana de anticipación, especialmente en temporada alta (diciembre-enero, Semana Santa, festivos) y fines de semana. Esto nos permite organizar mejor tu experiencia y garantizar disponibilidad de hospedaje y guías.",
                "order": 3,
            },
            {
                "question": "¿Puedo llevar niños?",
                "answer": "Sí, San Cipriano es apto para familias. Sin embargo, los niños deben estar SIEMPRE supervisados por un adulto responsable. Es obligatorio que usen chaleco salvavidas en todas las actividades acuáticas. La comunidad no se hace responsable por menores sin supervisión adecuada.",
                "order": 4,
            },
            {
                "question": "¿Qué debo llevar?",
                "answer": "Recomendamos: ropa cómoda de colores claros, manga larga para protección natural contra insectos, zapatos para agua (sandalias con agarre), traje de baño, gorra o sombrero (NO protector solar ni repelente químico - contaminan el río), careta de snorkel, toalla, cámara con funda impermeable, y muy importante: una bolsa para llevarte tu basura.",
                "order": 5,
            },
            {
                "question": "¿Hay señal de celular en San Cipriano?",
                "answer": "La señal de celular es muy limitada en San Cipriano. Esto es parte de la experiencia de desconexión con la naturaleza. Algunos hospedajes tienen WiFi básico, pero no lo garantizamos. Te recomendamos avisar a tus contactos que estarás desconectado y disfrutar de la tranquilidad.",
                "order": 6,
            },
            {
                "question": "¿Qué son las 'brujitas'?",
                "answer": "Las brujitas son pequeños carros sobre rieles impulsados por motocicletas adaptadas. Son el transporte tradicional para llegar a San Cipriano, ya que no hay carretera vehicular. El viaje en brujita atraviesa la selva y cruza puentes sobre el río - es una experiencia única en sí misma.",
                "order": 7,
            },
            {
                "question": "¿Es seguro nadar en el río?",
                "answer": "El río San Cipriano tiene aguas cristalinas pero también corrientes y profundidades variables. Es seguro nadar SOLO en las zonas autorizadas, siguiendo las instrucciones de los guías, y usando chaleco salvavidas. Está prohibido nadar bajo efectos de alcohol. El riesgo de ahogamiento es real si no se respetan las normas.",
                "order": 8,
            },
            {
                "question": "¿Puedo llevar alcohol o hacer fiestas?",
                "answer": "NO. Está prohibido el ingreso de alcohol y drogas a la reserva. San Cipriano es un lugar de turismo consciente y respeto por la naturaleza. Buscamos visitantes que quieran conectar con el ecosistema, no hacer fiestas. Hay otros destinos para ese tipo de turismo.",
                "order": 9,
            },
            {
                "question": "¿Se puede acampar?",
                "answer": "No se permite acampar libremente en la reserva. Sin embargo, algunos hospedajes comunitarios ofrecen zonas de camping. Consulta esta opción al hacer tu reserva. Recuerda que debes llevarte toda tu basura.",
                "order": 10,
            },
        ]

        for data in faqs_data:
            faq, created = FAQ.objects.get_or_create(
                question=data["question"],
                defaults=data
            )
            if created:
                self.stdout.write(f"  ✓ FAQ: {data['question'][:50]}...")

        self.stdout.write(self.style.SUCCESS(f"✓ {FAQ.objects.count()} FAQs"))

        self.stdout.write("")
        self.stdout.write(self.style.SUCCESS("=" * 50))
        self.stdout.write(self.style.SUCCESS("Initial data created successfully!"))
        self.stdout.write(self.style.SUCCESS("=" * 50))
