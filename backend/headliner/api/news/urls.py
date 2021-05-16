from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.ArticleApiView.as_view(), name="articles"),
]
