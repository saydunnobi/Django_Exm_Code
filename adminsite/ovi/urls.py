from django.urls import path
from .views import *

urlpatterns = [
   path('',uploade , name="uploade"),
   path('delete-product/<int:id>/',deleteproduct,name="deletetodo"),
   path ('productlist/',productlist , name="productlist"),
   path('Update_product/<int:id>/', updateproduct , name="updateproduct"),
]