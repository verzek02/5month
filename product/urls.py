from django.urls import path
from product import views
from product.views import *

urlpatterns = [
    path('api/v1/categories/', views.categories_list),
    path('api/v1/categories/<int:id>/', views.get_categories),
    path('api/v1/products/', views.list_products),
    path('api/v1/products/<int:id>/', views.get_products),
    path('api/v1/reviews/', views.list_review),
    path('api/v1/reviews/<int:id>/', views.get_review),

]
