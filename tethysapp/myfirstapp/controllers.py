from django.shortcuts import render
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import Button

@login_required()
def home(request):
    """
    Controller for the app home page.
    """

    context = {
    }

    return render(request, 'myfirstapp/home.html', context)

def map(request):
    """
    Controller for the app map page.
    """

    context = {
    }

    return render(request, 'myfirstapp/map.html', context)
