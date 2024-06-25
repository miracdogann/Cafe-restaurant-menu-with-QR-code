from django.shortcuts import render
from .models import Category , MenuItem
import qrcode
# import os
# from PIL import Image
from qrcode.constants import ERROR_CORRECT_L

# Create your views here.



def menu_list(request):

    category = Category.objects.all()
    for item in category:
        print(item.name)


    # qr nesnesi oluşturma
    qr = qrcode.QRCode(
        version=1,
        error_correction=ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    # Veriyi QR koduna ekle
    data = "http://127.0.0.1:8001"
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black",back_color = "white")

    img.save("qrMenu.png")

    # img = Image.open("qrMenu.png")
    # img.show()

    context = {'kategoriler': category,}
    return render(request,'home.html',context)


def breakfeast(request):
    category = Category.objects.get(name = "Kahvaltılıklar")
    breakfeast_item = MenuItem.objects.filter(category=category)
    context = {'kahvaltiliklar':breakfeast_item,
                'kategoriAdi':category.name
    }
    # print(len(breakfeast_item))
    return render(request,'kahvaltiliklar.html',context)


def lunchMenu(request):
    category = Category.objects.get(name = "Öğlen Yemekleri")
    lunchmenu_item = MenuItem.objects.filter(category=category)
    context = {'oglen_menuleri':lunchmenu_item, 
                'kategoriAdi':category.name
    }
    return render(request , 'ogle.html',context)


def nightMenu(request):
    category = Category.objects.get(name = "Akşam Yemekleri")

    nightmenu_item = MenuItem.objects.filter(category = category)
    context = {'aksam_menuleri':nightmenu_item,
                'kategoriAdi':category.name
    }
    return render(request , 'aksam.html',context)


def dessertMenu(request):
    category = Category.objects.get(name = "Tatlı Çeşitleri")   
    dessert_item = MenuItem.objects.filter(category=category)
    context = {'tatlilar':dessert_item,
                'kategoriAdi':category.name
    }
    return render(request , 'tatli.html',context)


def hotMenu(request):
    category = Category.objects.get(name = "Sıcak İçecekler")

    hot_item = MenuItem.objects.filter(category = category)
    context = {'sicaklar':hot_item,
            'kategoriAdi':category.name
    }
    return render(request , 'sicak.html',context)


def coldMenu(request):
    category = Category.objects.get(name = "Soğuk İçecekler")

    cold_item = MenuItem.objects.filter(category = category)
    context = {'soguklar':cold_item,
            'kategoriAdi':category.name
    }
    return render(request , 'soguk.html',context)