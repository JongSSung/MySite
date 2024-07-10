from django.shortcuts import render
from django.http import HttpResponse

# urls.py에서 실행 (PageLoad?)
def index(reqest):
    return HttpResponse("안녕");