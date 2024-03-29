from django.http import HttpResponseRedirect
from random import random
from .forms import posForm
from django.shortcuts import render

center = (55.78574364129168, 12.521466792669964)

def centered(point):
    return [(point[i] % 360) - center[i] for i in range(len(point))]

def get_quadrant(centered_point):
    lat = centered_point[0]
    lon = centered_point[1]
    if lon > 0 and lat > 0:
        res = 1
    elif lon > 0 and lat < 0:
        res = 4
    elif lon < 0 and lat > 0:
        res = 2
    elif lon < 0 and lat < 0:
        res = 3
    else:
        res = [1,2,3,4]

            
    return res

def index(request):
    """det burde altsammen være med GET, men fuck it."""
    if request.method == "POST":
        form = posForm(request.POST)
        if form.is_valid():
            point = centered([form.cleaned_data[key] for key in ["lat","lon"]])
            quadrant = get_quadrant(point)
            return render(request, "findQuadrant/index.html", {"form": form,"quadrant":quadrant})

    else:
        form = posForm()

    return render(request, "findQuadrant/index.html", {"form": form})
