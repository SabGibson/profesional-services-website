from django.urls import path, include
from products import views

urlpatterns = [
    path('latest-products/',views.LatestProductsLists.as_view()),
]