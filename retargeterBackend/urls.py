from django.urls import path
from .views import get_leads


urlpatterns = [
    path('leads/', get_leads, name='get_leads'),
]
