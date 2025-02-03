from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    peoples=[
        {'name': 'Abhijeet', 'age': 24},
        {'name': 'Jatin', 'age': 45}
    ]

    vegetables=[
        'Pumpkin', 'Tomato', 'Potatoe'
    ]

    return render(request, "index.html", context={'peoples': peoples, 'vegetables': vegetables})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def success_page(request):
    return HttpResponse("<h1>Hey this is a success page</h1>")