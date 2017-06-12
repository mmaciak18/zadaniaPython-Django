from django.shortcuts import render, redirect
from .models import User
from django.http import HttpResponseNotFound
import csv
from django.http import HttpResponse
from sample.templatetags import blocked, fb
# Create your views here.
def list_of_users(request):
    user = User.objects.all()
    template = "home/list_of_users/list_of_users.html"
    context = {'post' : user}
    return render(request, template, context)

def view(request):
    user = User.objects.all()
    r = request.GET['id']
    template = "home/list_of_users/view.html"
    for u in user:
        if r == u.username:
            context = {'post' : u}
            return render(request, template, context)
    return HttpResponseNotFound('<h1>Page not found</h1>')

def delete(request):
    user = User.objects.all()
    r = request.GET['id']
    if request.method == 'POST' and request.POST.get('apply', 'delete'):
        for u in user:
            if r == u.username:
                u.delete()
                return redirect('list_of_users')
    template = "home/list_of_users/delete.html"
    for u in user:
        if r == u.username:
            context = {'post' : u}
            return render(request, template, context)
    return HttpResponseNotFound('<h1>Page not found</h1>')

def edit(request):
    user = User.objects.all()
    r = request.GET['id']
    if request.method == 'POST':
        un = request.POST.get('username', False)
        bd = request.POST.get('birthdate', False)
        for u in user:
            if r == u.username:
                u.username = un
                u.birth_date = bd
                u.save()
                return redirect('list_of_users')
    template = "home/list_of_users/edit.html"
    for u in user:
        if r == u.username:
            context = {'post' : u}
            return render(request, template, context)
    return HttpResponseNotFound('<h1>Page not found</h1>')

def add(request):
    if request.method == 'POST':
        un = request.POST.get('username', False)
        ps = request.POST.get('password', False)
        bd = request.POST.get('birthdate', False)
        try:
            user = User(username = un, password=ps, birth_date=bd)
            user.save()
        except:
            return HttpResponseNotFound('<h1>User already exists</h1>')
        return redirect('list_of_users')
    template = "home/list_of_users/add.html"

    return render(request, template)

def csvview(request):
    user = User.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="database.csv"'

    writer = csv.writer(response)
    writer.writerow(['UserName', 'Birthday', 'Eligible', 'Random Number', 'BizzFuzz',])
    for u in user:
        writer.writerow([u.username, u.birth_date, blocked.blocked(u.birth_date), u.rand, fb.fb(u.rand),])
    return response
