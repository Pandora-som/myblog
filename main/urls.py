from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path("", views.index, name="index"),
    path("about_state/<int:states_id>", views.about_state, name="states_detail"),
]
