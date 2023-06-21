from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def Insert_Topic(request):
    TN=input('enter topic_name')
    TO=Topic.objects.get_or_create(topic_name=TN)[0]
    TO.save()
    return HttpResponse('Topic data is inserted')
def Insert_Webpage(request):
    TN=input('enter tpoic_name')
    TO=Topic.objects.get_or_create(topic_name=TN)[0]
    TO.save()
    n=input('enter name')
    u=input('enter url')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    return HttpResponse('Webpage is completed')
def Insert_AccessRecord(request):
    TN=input('enter topic_name')
    TO=Topic.objects.get_or_create(topic_name=TN)[0]
    TO.save()
    n=input('enter name')
    u=input('enter url')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    d=input('enter date')
    a=input('enter author')
    ARO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
    ARO.save()
    return HttpResponse('AccessRecord is completed')