from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def showLogin(request):
    return render(request,"student/login.html")


def showdashboard(request):
    return HttpResponse('loginDashboards')