from django.shortcuts import render

def hello_view(request):
    return render (request,'hello.html')

def hello_view(request):
    menu_items = [
        {"name": "Home", "url": "index", "active": True},
        {"name": "About", "url": "about", "active": False},
        {"name": "Classes", "url": "classes", "active": False},
        {"name": "Blog", "url": "blog", "active": False},
    ]
    return render(request, 'hello.html', {'menu_items': menu_items})

def slider_view(request):
    slides = [
        {'active': True, 'title': 'Boxing Center', 'button_text': 'Contact Us'},
        {'active': False, 'title': 'Boxing Center', 'button_text': 'Contact Us'},
        {'active': False, 'title': 'Boxing Center', 'button_text': 'Contact Us'},
    ]
    return render(request, 'hello.html', {'slides': slides})