from django.urls import path
from . import views

urlpatterns = [
    path('',views.menu_list,name='menuListesi'), 
    path('kahvaltiliklar/',views.breakfeast,name="breakfeast"),
    path('ogle-yemekleri/',views.lunchMenu,name="lunchMenu"),
    path('aksam-yemekleri/',views.nightMenu,name="nightMenu"),
    path('tatli-cesitleri/',views.dessertMenu,name="dessertMenu"),
    path('sicak-icecekler/',views.hotMenu,name="hotMenu"),
    path('soguk-icecekler/',views.coldMenu,name="coldMenu"),
]
