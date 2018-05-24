from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')

def count(request):
    text = request.GET['fulltext']
    wordcount = text.split()     
    return render(request,'count.html',{'stext':text,'wordcount':len(wordcount)})

def bio(request):
    nome = request.GET['nome']
    return render (request,'bio.html',{'nome':nome})