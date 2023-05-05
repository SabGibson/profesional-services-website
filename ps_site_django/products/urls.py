from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products import views


router = DefaultRouter()
router.register(r'', views.ProductViewSet)

urlpatterns = [
    path('latest-products/', views.LatestProductsLists.as_view()),
    path('product-admin/', include(router.urls)),
    path('products/search/', views.search),
    path('products/<slug:category_slug>/<slug:product_slug>/',
         views.ProductDetail.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),

]
