from django.urls import path 
from . import views

urlpatterns = [
    path('index', views.home, name='home' ),
    path('menu', views.MenuList.as_view(), name="Menu"),
    path('menu/<int:pk>', views.SingleMenuItem.as_view(), name="Menu"),
]
