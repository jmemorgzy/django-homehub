from django.shortcuts import render


def home(request):
    return render(request, 'bulbs.html')


def test(request):
    return "yep"
