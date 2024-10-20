from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.shortcuts import render

class NewItemForm(forms.Form):
    item = forms.CharField(label="New Item")

class DeleteItemForm(forms.Form): 
    item = forms.CharField(label="Delete Item")

def index(request):
    if "shopping_list" not in request.session: 
        request.session["shopping_list"] = []
    return render(request, "shopping_list/index.html", {
        "shopping_list": request.session["shopping_list"]  # Corregido aquí
    }) 

def add(request): 
    if request.method == "POST":  # Corregido aquí
        form = NewItemForm(request.POST)
        if form.is_valid(): 
            item = form.cleaned_data["item"]  # Corregido aquí
            request.session["shopping_list"] += [item]
            request.session.modified = True  # Agregado aquí
            return HttpResponseRedirect(reverse("shopping_list:index"))
        else: 
            return render(request, "shopping_list/add.html", {
                "form": form
            })
    return render(request, "shopping_list/add.html", {
        "form": NewItemForm()
    })

def delete(request): 
    if request.method == "POST": 
        form = DeleteItemForm(request.POST)
        if form.is_valid(): 
            item_to_delete = form.cleaned_data["item"].lower()  # Corregido aquí
            shopping_list_lower = [item.lower() for item in request.session["shopping_list"]]
            if item_to_delete in shopping_list_lower: 
                index = shopping_list_lower.index(item_to_delete)
                del request.session["shopping_list"][index]
                request.session.modified = True
            else: 
                form.add_error('item', 'Item not found.')
            return HttpResponseRedirect(reverse("shopping_list:index"))
        else: 
            return render(request, "shopping_list/delete.html",{
                "form": form
            })
    return render(request, "shopping_list/delete.html", {
        "form": DeleteItemForm()
    })
