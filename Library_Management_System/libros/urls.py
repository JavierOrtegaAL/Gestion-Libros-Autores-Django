from django.urls import path
from django.conf.urls.static import static
from Library_Management_System import settings
from .views import LibroDetail,LibrosDelete,AutoresDelete,LibroCreate, AutorDetail,AutorCreate, LibrosUpdate,AutorUpdate, LibrosPageView, AutoresPageView, InicioPageView

app_name="libros"
urlpatterns = [
    path('', InicioPageView.as_view(),name="inicio"),
    path('lista/', LibrosPageView.as_view(), name="lista"),
    path('autores/', AutoresPageView.as_view(), name="autores"),
    path('crear_libro/', LibroCreate.as_view(),name='crear_libro'),
    path('crear_autor/', AutorCreate.as_view(),name='crear_autor'),
	path('update_autor/<int:pk>/', AutorUpdate.as_view(), name='update_autor'),
    path('update_libro/<int:pk>/', LibrosUpdate.as_view(), name='update_libro'),
    path('delete_libro/<int:pk>/', LibrosDelete.as_view(),name="delete_libro"),
    path('delete_autor/<int:pk>/', AutoresDelete.as_view(),name="delete_autor"),
    path('autor/<int:pk>/', AutorDetail.as_view(),name="autor"),
    path('libro/<int:pk>/', LibroDetail.as_view(),name="libro"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)