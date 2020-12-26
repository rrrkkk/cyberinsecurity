from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from bank.models import Account
import sqlite3

def get_id(request):
    ''' Return ID of the current user, or -1 in case of none '''

    # One dream, one soul
    # One prize, one goal
    # One golden glance of what should be
    # It's a kind of magic
    # -Queen
    try:
        magic = request.GET['magic']
        account = Account.objects.get(username=magic)
        return account.id
    except:
        magic = -1

    # normal id
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
        account = Account.objects.get(username=username)
    except:
        data = {'message': 'No such username ' + username}
        return render(request, 'login.html', data)
    if request.GET['password'] != account.password:
        data = {'message': 'Wrong password'}
        return render(request, 'login.html', data)
    # Qapla' !
    return HttpResponseRedirect('/?id=' + str(account.id))

def search(request):
    id = get_id(request)
    if id < 0:
        data = {'message': 'Please login'}
        return render(request, 'login.html', data)
    data = {'account': Account.objects.get(id=id)}
    return render(request, 'search.html', data)

def search_action(request):
    id = get_id(request)
    if id < 0:
        data = {'message': 'Please login'}
        return render(request, 'login.html', data)
    username = request.GET['username']
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    response = cursor.execute("SELECT username FROM bank_account WHERE username LIKE '" + username + "'").fetchall()
    data = {'account': Account.objects.get(id=id), 'response': response}
    return render(request, 'search_action.html', data)

def transfer(request):
    id = get_id(request)
    if id < 0:
        data = {'message': 'Please login'}
        return render(request, 'login.html', data)
    data = {'account': Account.objects.get(id=id)}
    return render(request, 'transfer.html', data)

def transfer_action(request):
    id = get_id(request)
    if id < 0:
        data = {'message': 'Please login'}
        return render(request, 'login.html', data)
    username = request.GET['username']
    amount = int(request.GET['amount'])
    hisaccount = Account.objects.get(username=username)
    myaccount = Account.objects.get(id=id)
    status = 'failed'
    if myaccount.balance >= amount:
        myaccount.balance -= amount
        hisaccount.balance += amount
        myaccount.save()
        hisaccount.save()
        status = 'succeeded'
    data = {'account': myaccount, 'status': status}
    return render(request, 'transfer_action.html', data)
