from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_manager(request):

    if request.method == 'POST' and 'add_task' in request.POST:
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        completed = request.POST.get('completed') == 'on'
        if title:
            Task.objects.create(title=title, description=description, completed=completed)
        return redirect('task_manager')


    if request.method == 'POST' and 'update_task' in request.POST:
        task_id = request.POST.get('task_id')
        task = get_object_or_404(Task, id=task_id)
        task.title = request.POST.get('title', '').strip()
        task.description = request.POST.get('description', '').strip()
        task.completed = request.POST.get('completed') == 'on'
        task.save()
        return redirect('task_manager')


    if request.method == 'POST' and 'delete_task' in request.POST:
        task_id = request.POST.get('task_id')
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return redirect('task_manager')


    tasks = Task.objects.all().order_by('-created_at')


    edit_id = request.GET.get('edit')
    task_to_edit = None
    if edit_id:
        task_to_edit = get_object_or_404(Task, id=edit_id)

    return render(request, 'task_list.html', {

        'tasks': tasks,
        'task_to_edit': task_to_edit,
    })