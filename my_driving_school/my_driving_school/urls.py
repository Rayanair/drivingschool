from django.urls import path, include

urlpatterns = [
    path('', include('driving_school.urls')),  # Importation des URLs de l'application driving_school
]