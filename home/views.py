from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def test(request):
    return render(request, 'test.html')


def error(request):
    return render(request, 'error.html')


def menu(request):
    return render(request, "menu.html", {})

