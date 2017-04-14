#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from blog import models

def index(request):
  return render(request,"index.html")

def right(request):
  if request.method=="POST":
    ip=request.POST.get('ip',None)
    hostname=request.POST.get('hostname',None)
    lable=request.POST.get('lable',None)
    password=request.POST.get('password',None)
    os=request.POST.get('os',None)
    area=request.POST.get('area',None)
    models.CmdbInfo.objects.create(ip=ip,os=os,hostname=hostname,password=password,lable=lable,area=area)
  data=models.CmdbInfo.objects.all()
  return render(request,"right.html",{'data':data})

def left(request):
  return render(request,"left.html")

