from django.urls import path,include
from .views import *
app_name = 'main'


urlpatterns = [
   path('product/', ProductView.as_view(), name = 'index'),
   path('user/', UserView.as_view(), name='user'),
   path('product/<int:pk>/', product_detail, name = 'product_detail'),
   path('city/', CityView.as_view(), name = 'city'),
   path('country/', CountryView.as_view(), name = 'country'),
   path('material/', MaterialView.as_view(), name = 'material'),
   #path('product2/<int:pk>/', product2_detail, name = 'product2_detail'),
]
