from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

def checksession(request):
    data=request.session.get('faculty')
    return HttpResponse(data)


def deletesession(request):
    try:
        del request.session.faculty
        return True
    except Exception as ex:
        return HttpResponse(ex)

def showLogin(request):
            return render(request,"faculty/login.html")


def validatelogin(request):
    if request.method == "POST":
        request.session['faculty']=request.POST.get("email")
        return redirect("dashboard")
    else:
        return HttpResponse('LOGIN IS NOT ACCEPT')


def showdashboard(request):
    try:
        checksession(request)
        return render(request,"faculty/dashboard.html")
    except:
        redirect("login")


def accountlogout(request):
    return  checksession(request)
    # try:
    #     del request.session['faculty']
    # except KeyError:
    #     return HttpResponse('nosession')
    # ses=request.session['faculty']
    # return HttpResponse(ses)