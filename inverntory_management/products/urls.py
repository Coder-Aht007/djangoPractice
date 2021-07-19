from . import views
from django.urls import path

app_name = "products"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:prod_id>/', views.detail, name='detail'),
    path('search/', views.product_search, name="search"),
    path('update/',views.update_product, name='update'),
    path('delete',views.delete_product, name='delete'),
    path('delete',views.delete_product, name='delete'),
    path('add/', views.add_product, name='add')
]