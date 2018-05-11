from django.urls import path

from . import views

urlpatterns = [
    path('getSleep/', views.get_sleep),
    path('', views.ReactAppView.as_view(), name="react")
]

