from django.urls import path
from .views import *
urlpatterns = [
	path('',dashboard, name="dashboard"),
	path('ajouter-client', AddClient.as_view(), name="ajouter-client"),
]