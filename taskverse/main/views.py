from django.shortcuts import render, redirect, get_object_or_404
from main.models import Task, History
from datetime import datetime, date
from django.contrib.auth import logout
from django.urls import reverse
from django.utils.http import urlencode


def task(request):
    filter_type = request.GET.get('filter', 'all')
    tasks = Task.objects.all().order_by('due_date', '-created_at')

    if filter_type == 'completed':
        tasks = tasks.filter(completed=True)
    elif filter_type == 'incomplete':
        tasks = tasks.filter(completed=False)

    return render(request, 'task.html', {
        'tasks': tasks,
        'filter': filter_type,
        'today': date.today()
    })


def add(request):
    if request.method == 'POST':
        title = request.POST.get('task_title')
        desc = request.POST.get('desc')
        due_date = request.POST.get('due_date') or None
        if due_date:
            due_date = datetime.strptime(due_date, "%Y-%m-%d").date()

        if title.strip():
            new_task = Task.objects.create(
                task_title=title,
                desc=desc,
                due_date=due_date
            )
            History.objects.create(task_title=new_task.task_title, action='Created')
        return redirect('task')
    return render(request, 'add.html')


def edit(request, id):
    task_obj = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        new_title = request.POST.get('task_title')
        new_desc = request.POST.get('desc')
        due_date = request.POST.get('due_date') or None
        if due_date:
            due_date = datetime.strptime(due_date, "%Y-%m-%d").date()

        if new_title.strip():
            task_obj.task_title = new_title
            task_obj.desc = new_desc
            task_obj.due_date = due_date
            task_obj.save()
            History.objects.create(task_title=task_obj.task_title, action='Updated')
        return redirect('task')
    return render(request, 'edit.html', {'task': task_obj})


def delete(request, id):
    task_obj = get_object_or_404(Task, id=id)
    History.objects.create(task_title=task_obj.task_title, action='Deleted')
    task_obj.delete()
    return redirect('task')


def history(request):
    logs = History.objects.order_by('-timestamp')
    return render(request, 'history.html', {'logs': logs})


def toggle_complete(request, id):
    task_obj = get_object_or_404(Task, id=id)
    task_obj.completed = not task_obj.completed
    task_obj.save()

    History.objects.create(
        task_title=task_obj.task_title,
        action='Completed' if task_obj.completed else 'Marked Incomplete'
    )

    base_url = reverse('task')
    query_string = urlencode({'filter': 'completed' if task_obj.completed else 'incomplete'})
    url = f"{base_url}?{query_string}"
    return redirect(url)


def restore_task(request, log_id):
    log = get_object_or_404(History, id=log_id)
    Task.objects.create(task_title=log.task_title)
    log.delete()
    return redirect('history')


def delete_log(request, log_id):
    log = get_object_or_404(History, id=log_id)
    log.delete()
    return redirect('history')


def logout_view(request):
    logout(request)
    return redirect('login')  # Make sure 'login' URL name exists and points to login.html
