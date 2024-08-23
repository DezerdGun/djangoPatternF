def header(request):
    contacts = [
        {'icon': 'images/telephone.png', 'text': '+01 1234567890'},
        {'icon': 'images/mail.png', 'text': 'demo@gmail.com'},
        {'icon': 'images/location.png', 'text': 'Den mark Loram ipusum'},
    ]
    nav_items = [
        {'name': 'Home', 'url': 'index.html', 'active': True},
        {'name': 'About', 'url': 'about.html', 'active': False},
        {'name': 'Classes', 'url': 'class.html', 'active': False},
        {'name': 'Blog', 'url': 'blog.html', 'active': False},
    ]
    return {'contacts': contacts, 'nav_items': nav_items}
