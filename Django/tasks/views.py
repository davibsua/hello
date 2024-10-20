from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.shortcuts import render

class NewTaskForm(forms.Form): 
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)
# Create your views here.
def index(request): 
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html",{
        "tasks": request.session["tasks"]
    })

def add(request): 
    if request.method == "POST": 
        form = NewTaskForm(request.POST)
        if form.is_valid(): 
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else: 
            return render(request, "tasks/add.html", {
                "form": form
            })
    return render(request, "tasks/add.html",{
        "form": NewTaskForm()
    })

class DeleteTaskForm(forms.Form): 
    task = forms.CharField(label="Delete Task")

def delete(request): 
    if request.method == "POST":
        form = DeleteTaskForm(request.POST)
        if form.is_valid(): 
            task_to_delete = form.cleaned_data["task"].lower()  # Convertir a minúsculas

            # Convertir todas las tareas en la lista a minúsculas para la comparación
            tasks_lower = [task.lower() for task in request.session["tasks"]]

            if task_to_delete in tasks_lower:
                # Obtener el índice de la tarea original (con mayúsculas/minúsculas correctas)
                index = tasks_lower.index(task_to_delete)
                del request.session["tasks"][index]  # Eliminar la tarea original

                # Marcar la sesión como modificada
                request.session.modified = True
            else:
                # Si no existe, puedes agregar un mensaje o simplemente recargar el formulario
                form.add_error('task', 'Task not found.')
                
            return HttpResponseRedirect(reverse("tasks:index"))
        else: 
            return render(request, "tasks/delete.html", {
                "form": form
            })
    return render(request, "tasks/delete.html", {
        "form": DeleteTaskForm()
    })




