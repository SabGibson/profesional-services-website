from django.urls import path, include
from products import views

urlpatterns = [
    path('latest-products/', views.LatestProductsLists.as_view()),
    path('create-product/', views.ProductCreateView.as_view(), name='create_product'),
    path('products/search/', views.search),
    path('products/<slug:category_slug>/<slug:product_slug>/',
         views.ProductDetail.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/',
         views.ProductDetail.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),

]
