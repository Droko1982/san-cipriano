"""
Travel guide URLs — keyword-rich slugs served at the site root
(e.g. /como-llegar-a-san-cipriano/) so each guide can rank for its search intent.
"""

from django.urls import path

from .views import GuideView

app_name = "guides"

urlpatterns = [
    path(
        "como-llegar-a-san-cipriano/",
        GuideView.as_view(template_name="guides/how_to_get.html", guide_key="how_to_get"),
        name="how_to_get",
    ),
    path(
        "precios-san-cipriano/",
        GuideView.as_view(template_name="guides/prices.html", guide_key="prices"),
        name="prices",
    ),
    path(
        "brujitas-san-cipriano/",
        GuideView.as_view(template_name="guides/brujitas.html", guide_key="brujitas"),
        name="brujitas",
    ),
    path(
        "que-hacer-en-san-cipriano/",
        GuideView.as_view(template_name="guides/things_to_do.html", guide_key="things_to_do"),
        name="things_to_do",
    ),
]
