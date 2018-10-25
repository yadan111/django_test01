#coding=utf-8
from django.http import HttpResponse


def good_views(request):
    return HttpResponse('hello')
def login_view(request):
    return HttpResponse('111')