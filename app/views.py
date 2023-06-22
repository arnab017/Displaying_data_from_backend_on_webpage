from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def input_topic(request):
    tn = input('Enter topic : ')
    TO = Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('<center><h1>Topic Created</h1></center>')

def input_webpage(request):
    tn = input('Enter topic : ')
    TO = Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n = input('Enter webpage : ')
    u = input('input url : ')
    WO = Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    return HttpResponse('<center><h1>Webpage Created</h1></center>')

def input_ar(request):
    tn = input('Enter topic : ')
    TO = Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n = input('Enter webpage : ')
    u = input('input url : ')
    WO = Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    d = input('Enter date(yyyy-mm-dd) : ')
    a = input('Enter author : ')
    ARO = AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
    ARO.save()
    return HttpResponse('<center><h1>AccessRecord Created</h1></center>')


def display_topic(request):
    topics = Topic.objects.all()
    d = {"topics": topics}
    return render(request,'display_topic.html',d)


def display_webpage(request):
    webpages = Webpage.objects.all()
    d = {"webpages": webpages}
    return render(request,'display_webpage.html',d)


def display_accessrecords(request):
    accessrecords = AccessRecord.objects.all()
    d = {"accessrecords": accessrecords}
    return render(request,'display_accessrecords.html',d)

def display_all(request):
    topics = Topic.objects.all()
    webpages = Webpage.objects.all()
    accessrecords = AccessRecord.objects.all()
    d = {"topics": topics, "webpages": webpages, "accessrecords": accessrecords}
    return render(request,'display_all.html',d)


