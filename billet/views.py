from django.shortcuts import render, redirect
from .models import Billet
from .forms import BilletForm

# CRUD - create, retrieve, update, delete, list


def billet_list(request):
    billets = Billet.objects.all()
    context = {
        "billets": billets
    }
    return render(request, "billets.html", context)


def billet_retrieve(request, pk):
    billet = Billet.objects.get(id=pk)
    context = {
        "billet": billet
    }
    return render(request, "billet.html", context)


def billet_create(request):
    form = BilletForm()
    if request.method == "POST":
        form = BilletForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "billet_create.html", context)


def billet_update(request, pk):
    billet = Billet.objects.get(id=pk)
    form = BilletForm(instance=billet)

    if request.method == "POST":
        form = BilletForm(request.POST, files = request.FILES, instance=billet)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "billet_update.html", context)


def billet_delete(request, pk):
    billet = Billet.objects.get(id=pk)
    billet.delete()
    return redirect("/")
