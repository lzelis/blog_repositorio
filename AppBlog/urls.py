from django.urls import path
from AppBlog.views import profesores, curso, entregables, estudiantes

urlpatterns = [
    path('curso/', curso),
    path('profesores/', profesores),
    path('entregables/', entregables),
    path('estudiantes/', estudiantes),
]