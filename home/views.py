from django.shortcuts import render
from dotenv import load_dotenv
from home.functions import get_bulbs


def home(request):
    load_dotenv()
    bulbs = get_bulbs()
    print(bulbs)
    return render(request, 'home.html', {'bulbs': bulbs})
