from django.shortcuts import render
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    context = {
        "todo_items": todo_items
    }
    return render(request, "todoApp/index.html", context)


def add_todo(request):
    if request.method == "POST":
        current_date = timezone.now()
        content = request.POST["content"]
        created_obj = Todo.objects.create(
            added_date=current_date,
            text=content
        )
    return HttpResponseRedirect("/")


def delete_todo(request, todo_id):
    if request.method == "POST":
        Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")