from django.urls import path
from .vistas_modelos.iva import IVAListView, IVACreateView, IVAUpdateView, IVADeleteView
from .vistas_modelos.otros_autores import OtrosAutoresListView, OtrosAutoresCreateView, OtrosAutoresUpdateView, OtrosAutoresDeleteView
from .vistas_modelos.editorial import EditorialListView, EditorialCreateView, EditorialUpdateView, EditorialDeleteView
from .vistas_modelos.pais import PaisListView, PaisCreateView, PaisUpdateView, PaisDeleteView
from .vistas_modelos.genero import GeneroListView, GeneroCreateView, GeneroUpdateView, GeneroDeleteView
from .vistas_modelos.autor import AutorListView, AutorCreateView, AutorUpdateView, AutorDeleteView
from .vistas_modelos.producto import ProductoListView, ProductoUpdateView, ProductoCreateView, ProductoDeleteView
from .views import DashboardView

urlpatterns = [
    path('', DashboardView.as_view(), name='inventario-dashboard'),

    # listados
    path('listado-producto', ProductoListView.as_view(), name='listado-producto'),
    path('listado-autor', AutorListView.as_view(), name='listado-autor'),
    path('listado-genero', GeneroListView.as_view(), name='listado-genero'),
    path('listado-pais', PaisListView.as_view(), name='listado-pais'),
    path('listado-editorial', EditorialListView.as_view(), name='listado-editorial'),
    path('listado-otro-autor', OtrosAutoresListView.as_view(), name='listado-otro-autor'),
    path('listado-iva', IVAListView.as_view(), name='listado-iva'),

    # crear
    path('crear-producto', ProductoCreateView.as_view(), name='crear-producto'),
    path('crear-autor', AutorCreateView.as_view(), name='crear-autor'),
    path('crear-genero', GeneroCreateView.as_view(), name='crear-genero'),
    path('crear-pais', PaisCreateView.as_view(), name='crear-pais'),
    path('crear-editorial', EditorialCreateView.as_view(), name='crear-editorial'),
    path('crear-otro-autor', OtrosAutoresCreateView.as_view(), name='crear-otro-autor'),
    path('crear-iva', IVACreateView.as_view(), name='crear-iva'),

    # editar
    path('editar-producto/<pk>/', ProductoUpdateView.as_view(), name='editar-producto'),
    path('editar-autor/<pk>/', AutorUpdateView.as_view(), name='editar-autor'),
    path('editar-genero/<pk>/', GeneroUpdateView.as_view(), name='editar-genero'),
    path('editar-pais/<pk>/', PaisUpdateView.as_view(), name='editar-pais'),
    path('editar-editorial/<pk>/', EditorialUpdateView.as_view(), name='editar-editorial'),
    path('editar-otro-autor/<pk>/', OtrosAutoresUpdateView.as_view(), name='editar-otro-autor'),
    path('editar-iva/<pk>/', IVAUpdateView.as_view(), name='editar-iva'),

    # eliminar
    path('eliminar-producto/<pk>/', ProductoDeleteView.as_view(), name='eliminar-producto'),
    path('eliminar-autor/<pk>/', AutorDeleteView.as_view(), name='eliminar-autor'),
    path('eliminar-genero/<pk>/', GeneroDeleteView.as_view(), name='eliminar-genero'),
    path('eliminar-pais/<pk>/', PaisDeleteView.as_view(), name='eliminar-pais'),
    path('eliminar-editorial/<pk>/', EditorialDeleteView.as_view(), name='eliminar-editorial'),
    path('eliminar-otro-autor/<pk>/', OtrosAutoresDeleteView.as_view(), name='eliminar-otro-autor'),
    path('eliminar-iva/<pk>/', IVADeleteView.as_view(), name='eliminar-iva'),
]