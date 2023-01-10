from django.urls import path

from products.views import new_product, list_product

urlpatterns = [
    path('new_product/', new_product),
    path('list_product/', list_product)
    

]
