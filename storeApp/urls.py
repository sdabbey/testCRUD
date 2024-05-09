from django.urls import path
from . import views


urlpatterns = [
    # url(r'^product$', views.productAPI),
    # url(r'^product/([0-9]+)$', views.productAPI)
    path('product/', views.productAPI),
    path('product/<int:id>/', views.productAPI)
]
