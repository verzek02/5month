from django.urls import path
from product import views
from product.views import *

urlpatterns = [
    path('api/v1/categories/', CategoryView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/categories/<int:id>/',CategoryView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('api/v1/products/', Productview.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/products/<int:id>/', Productview.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('api/v1/reviews/', ReviewView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/reviews/<int:id>/', ReviewView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

]
