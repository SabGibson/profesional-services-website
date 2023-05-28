from django.urls import path

from orders import views

urlpatterns = [
    path('checkout/',views.checkout,name='checkout'),
    path('orders/',views.OrdersList.as_view(),name='my-orders')
]