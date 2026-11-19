"""
Travel guide metadata: SEO title/description, hero, FAQ and related-guide cards.

Facts used here (confirmed by the community, Nov 2026):
- Cali -> Córdoba: ~2.5 h by road (Cali–Buenaventura road; Córdoba is BEFORE Buenaventura)
- Brujita Córdoba -> San Cipriano: 15-20 min, $24.000 round trip incl. insurance, 6am-6pm
- Reserve entry: $10.000 per person
- Lodging + 3 meals: $140.000 per person/night when booked via WhatsApp from the site
- Complete experience (lodging, 3 meals, guided tour): $220.000 per person
Keep prices here, in templates/guides/prices.html and templates/visitors/services.html in sync.
"""

from django.utils.translation import gettext_lazy as _

GUIDES = {
    "how_to_get": {
        "url_name": "guides:how_to_get",
        "image": "images/gallery/estacion-nueva.jpg",
        "emoji": "📍",
        "title": _("Cómo llegar a San Cipriano desde Cali (2026)"),
        "meta_description": _(
            "Cómo llegar a San Cipriano paso a paso: desde Cali son unas 2,5 horas por la vía a "
            "Buenaventura hasta Córdoba y luego 15-20 minutos en brujita. Rutas en carro y bus, "
            "horarios y parqueadero."
        ),
        "h1": _("Cómo llegar a San Cipriano"),
        "lead": _(
            "San Cipriano queda en el Pacífico colombiano, en el municipio de Buenaventura. No hay "
            "carretera hasta el pueblo: el último tramo se hace en brujita. Aquí tienes la ruta paso a paso."
        ),
        "card_title": _("Cómo llegar"),
        "card_desc": _("Ruta desde Cali y Buenaventura en carro o bus, paso a paso."),
        "faqs": [
            (
                _("¿Cuánto tiempo se demora de Cali a San Cipriano?"),
                _(
                    "Unas 2,5 horas por carretera desde Cali hasta Córdoba, más 15-20 minutos en "
                    "brujita hasta San Cipriano. En total, cuenta con unas 3 horas de viaje."
                ),
            ),
            (
                _("¿Se puede llegar en carro hasta San Cipriano?"),
                _(
                    "No. El carro llega hasta Córdoba, donde hay un parqueadero vigilado. El último "
                    "tramo hasta San Cipriano se hace en brujita, sobre los rieles que atraviesan la selva."
                ),
            ),
            (
                _("¿A qué hora funcionan las brujitas?"),
                _(
                    "Las brujitas operan de 6am a 6pm. El paseo ida y vuelta cuesta $24.000 COP por "
                    "persona e incluye el seguro."
                ),
            ),
        ],
    },
    "prices": {
        "url_name": "guides:prices",
        "image": "images/gallery/hotel-restaurante.jpg",
        "emoji": "💰",
        "title": _("Precios San Cipriano 2026: cuánto cuesta ir"),
        "meta_description": _(
            "¿Cuánto cuesta ir a San Cipriano en 2026? Entrada $10.000, brujita $24.000 ida y vuelta "
            "con seguro y hospedaje con 3 comidas desde $140.000 por persona. Presupuesto para "
            "pasadía y fin de semana."
        ),
        "h1": _("Precios de San Cipriano 2026"),
        "lead": _(
            "Los precios oficiales de la comunidad para que armes tu presupuesto sin sorpresas. "
            "Reservando directamente por WhatsApp no pagas intermediarios."
        ),
        "card_title": _("Precios 2026"),
        "card_desc": _("Entrada, brujita, hospedaje, comida y presupuestos de ejemplo."),
        "faqs": [
            (
                _("¿Cuánto cuesta la entrada a San Cipriano?"),
                _(
                    "La entrada a la reserva cuesta $10.000 COP por persona. La brujita se paga "
                    "aparte: $24.000 COP ida y vuelta, con seguro incluido."
                ),
            ),
            (
                _("¿Cuánto cuesta un pasadía en San Cipriano?"),
                _(
                    "Entrada y brujita suman $34.000 COP por persona. Con almuerzo (desde $25.000 "
                    "COP), un pasadía queda desde unos $59.000 COP por persona, sin contar el "
                    "transporte hasta Córdoba."
                ),
            ),
            (
                _("¿Cuánto cuesta dormir en San Cipriano?"),
                _(
                    "El plan de hospedaje con 3 comidas cuesta $140.000 COP por persona por noche "
                    "reservando por WhatsApp desde esta página. Con tour guiado incluido, la "
                    "experiencia completa cuesta $220.000 COP por persona."
                ),
            ),
        ],
    },
    "brujitas": {
        "url_name": "guides:brujitas",
        "image": "images/gallery/brujita-operador.jpg",
        "emoji": "🚃",
        "title": _("Brujitas de San Cipriano: precio y horario"),
        "meta_description": _(
            "Todo sobre las brujitas de San Cipriano: el transporte sobre rieles impulsado por moto "
            "que cruza la selva en 15-20 minutos. Precio $24.000 ida y vuelta con seguro, horario "
            "6am-6pm y consejos."
        ),
        "h1": _("Las brujitas de San Cipriano"),
        "lead": _(
            "Pequeños carros sobre rieles impulsados por motocicleta: la única forma de llegar a "
            "San Cipriano y una aventura en sí misma."
        ),
        "card_title": _("Las brujitas"),
        "card_desc": _("Qué son, cuánto cuestan, horario y consejos para el viaje."),
        "faqs": [
            (
                _("¿Cuánto cuesta la brujita en San Cipriano?"),
                _("$24.000 COP por persona, ida y vuelta, con seguro incluido."),
            ),
            (
                _("¿Cuánto dura el viaje en brujita?"),
                _("Entre 15 y 20 minutos desde la estación de Córdoba hasta San Cipriano."),
            ),
            (
                _("¿Es seguro montar en brujita?"),
                _(
                    "Sí. Los operadores son de la comunidad, conocen bien la vía y el pasaje incluye "
                    "un seguro. Solo debes sujetarte bien y seguir sus indicaciones."
                ),
            ),
        ],
    },
    "things_to_do": {
        "url_name": "guides:things_to_do",
        "image": "images/gallery/pozos-naturales.jpg",
        "emoji": "🌊",
        "title": _("Qué hacer en San Cipriano: 8 planes imperdibles"),
        "meta_description": _(
            "Qué hacer en San Cipriano: nadar en ríos cristalinos, bajar el río en flotador, caminar "
            "a cascadas, ver más de 200 especies de aves, viajar en brujita y probar la cocina del "
            "Pacífico. Cerca de Cali."
        ),
        "h1": _("Qué hacer en San Cipriano"),
        "lead": _(
            "Ríos de agua cristalina, selva tropical y una comunidad que te recibe como en casa: "
            "estos son los planes que no te puedes perder."
        ),
        "card_title": _("Qué hacer"),
        "card_desc": _("Ríos, tubing, cascadas, aves, cocina del Pacífico y cultura."),
        "faqs": [
            (
                _("¿Qué se puede hacer en San Cipriano?"),
                _(
                    "Nadar en ríos cristalinos, bajar el río en flotador, caminar hasta cascadas, "
                    "avistar aves, viajar en brujita y probar la cocina del Pacífico, entre otros "
                    "planes de naturaleza."
                ),
            ),
            (
                _("¿San Cipriano es un buen plan para niños?"),
                _(
                    "Sí, es apto para familias. Los niños deben estar siempre supervisados por un "
                    "adulto y usar chaleco salvavidas en las actividades acuáticas."
                ),
            ),
            (
                _("¿Se necesita guía en San Cipriano?"),
                _(
                    "Para los senderos y las cascadas recomendamos ir con guías de la comunidad: "
                    "conocen la selva y las normas de seguridad del río."
                ),
            ),
        ],
    },
}

# Order used for the "related guides" block and the footer.
GUIDE_ORDER = ["how_to_get", "prices", "brujitas", "things_to_do"]

# Price list used on the prices guide and in its Offer schema (COP, per person unless noted).
PRICE_LIST = [
    {"name": _("Entrada a la reserva"), "price": "$10.000", "low": 10000, "high": None,
     "note": _("Por persona")},
    {"name": _("Brujita ida y vuelta"), "price": "$24.000", "low": 24000, "high": None,
     "note": _("Por persona, incluye seguro")},
    {"name": _("Plan hospedaje + 3 comidas"), "price": "$140.000", "low": 140000, "high": None,
     "note": _("Por persona, 1 noche, reservando por WhatsApp"), "highlight": True},
    {"name": _("Experiencia completa (hospedaje, 3 comidas y tour)"), "price": "$220.000",
     "low": 220000, "high": None, "note": _("Por persona, 1 noche")},
    {"name": _("Tour guiado (flotadores, chalecos, cascadas y pozos)"),
     "price": "$80.000 - $100.000", "low": 80000, "high": 100000, "note": _("Por persona")},
    {"name": _("Comida"), "price": "$25.000 - $45.000", "low": 25000, "high": 45000,
     "note": _("Por comida")},
    {"name": _("Parqueadero"), "price": "$15.000 - $20.000", "low": 15000, "high": 20000,
     "note": _("Por vehículo, por día o noche")},
]
