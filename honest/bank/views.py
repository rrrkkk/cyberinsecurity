from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from bank.models import Account

def get_id(request):
    try:
        magic = request.GET['magic']
        account = Account.objects.get(username=magic)
        return account.id
    except:
        magic = -1
    try:
        id = int(request.GET['id'])
    except:
        id = -1
    return id

def index(request):
    id = get_id(request)
    if id < 0:
        data = {'message': 'Please login'}
        return render(request, 'login.html', data)
    data = {'account': Account.objects.get(id=id)}
    return render(request, 'index.html', data)

def login(request):
    try:
        username = request.GET['username']
    except:
        data = {'message': 'No GET parameter'}
        return render(request, 'login.html', data)
    try:
        account = Account.objects.filter(username=username)
    except:
        data = {'message': 'No such username ' + username}
        return render(request, 'login.html', data)
    if request.GET['password'] != account.password:
        data = {'message': 'Wrong password'}
        return render(request, 'login.html', data)
    # Qapla' !
    return HttpResponseRedirect('/?id=' + str(account.id))
