from django.shortcuts import render,redirect
from .models import addcontestent
from .forms import regform,loginform,contestentform,votingform
from .models import regmodel,votingmodel
import urllib.request
from bs4 import BeautifulSoup
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')
def display(request):
    contestent=addcontestent.objects.all()
    return render(request,'contestent.html',{'contestent':contestent})
def register(request):
    if request.method == 'POST':
        reg_form=regform(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return redirect('home')

    form=regform()
    return render(request,'reg.html',{'regform':form})
def login(request):
    if request.method=='POST':
        forms=loginform(request.POST)
        if forms.is_valid():
            user_name=forms.cleaned_data['username']
            pass_word=forms.cleaned_data['password']
            dbuser=regmodel.objects.filter(username=user_name,password=pass_word)
            if dbuser:
                return render(request,'login.html',{'dbuser':dbuser,'forms':forms})
            else:
                return render(request,'login.html',{'dbuser1':dbuser,'forms':forms})
    form=loginform()
    return render(request,'login.html',{'form':form})
def insert(request):
    if request.method == 'POST':
        add_form=contestentform(request.POST or None,request.FILES or None)
        if add_form.is_valid():
            add_form.save()
            return redirect('display')
    addform=contestentform()
    return render(request,'insert.html',{'addform':addform})
def update(request,id):
    a=addcontestent.objects.get(id=id)
    contestent=contestentform(request.POST or None, request.FILES or None, instance=a)
    if request.method == 'POST':
        if contestent.is_valid():
            contestent.save()
            return redirect('display')
    return render(request,'update.html',{'contestent':contestent})
def delete(request,id):
    a=addcontestent.objects.get(id=id)
    #contestent=contestentform(request.POST or None,instance=a)
    if request.method == 'POST':
        a.delete()
        return redirect('display')
    return render(request,'delete.html',{'a':a})
def fun(request,id):
    if request.method == 'POST':
        contestent=addcontestent.objects.get(id=id)
        votes = int(request.POST.get('votes'))
        v=votingmodel(votes=votes,contestent_name=contestent)
        i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if votes in i:
            v.save()
            urllib.request.urlopen('https://api.thingspeak.com/update?api_key=N9BMXJOH7RAIB286&field1='+str(votes))
            return render(request,'vote.html',{'votes':votes,'v':v})
        else:
            return render(request,'vote.html',{'votes1':votes,'v':v})

    form=addcontestent.objects.get(id=id)
    forms=votingform()
    return render(request,'vote.html',{'form':form,'forms':forms})
