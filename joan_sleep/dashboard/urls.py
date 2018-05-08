from django.urls import path
from django.views.generic import TemplateView
from .views import DashboardView

urlpatterns = [
    path('settings/', DashboardView.as_view(), name='dashboard-settings')
]
