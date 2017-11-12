from django.shortcuts import render
from django.http import HttpResponse
import datetime


def index(request):
    return render(request, 'summaggle_mvp/index.html')
    #now = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    #return HttpResponse(html)
