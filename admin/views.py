from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.generic import TemplateView
from admin.models import AdminTable,CourseTable,ScheduleclassesTable
from admin.forms import adminform,scheduleclass
import json
from django.contrib import messages
from django.core.exceptions import ViewDoesNotExist
from django.db.utils import IntegrityError
from django.core import serializers

def checksession(request):
    try:
        request.session.exists('adminuser')
        mailid=request.session.get('adminuser')
        frm=AdminTable.objects.get(email=mailid)
        if(frm):
            return request.session.get('adminuser')
        return  False
    except Exception as e:
        return False


def showLogin(request):
    if (checksession(request)):
        return redirect('admin')
    else:
        return render(request, 'admin/login.html')


def verifylogin(request):
    if request.method == 'POST':
        try:
            data=AdminTable.objects.get(email=request.POST.get('adminemail'))
            if data.password == request.POST.get('adminpwd'):
                request.session['adminuser'] = request.POST.get('adminemail')
                request.session.set_expiry(600)
                return redirect('admin')
        except:
            messages.error(request, "Invalid Account Details")
            return redirect("login")

    return redirect("login")

def showadmindashboard(request):
    if(checksession(request)):
        data=AdminTable.objects.get(email=request.session['adminuser'])
        return render(request,'admin/dashboard.html',{"data":data})
    else:
        return redirect('login')

def Deletesession(request):
    if(checksession(request)):
        del request.session['adminuser']
        return redirect('login')

    return redirect("login")


def showadmins(request):
    if(checksession(request)):
        adminsdata=AdminTable.objects.all()
        dataform=adminform()
        context={'data':adminsdata,'form':dataform}
        return render(request,"admin/admins.html",context)
    else:
        return redirect('login')




def addadmin(request):
        checksession(request)
        if request.method == "POST":
            data=request.POST
            df=adminform(data)
            if df.is_valid():
                df.save()
                return JsonResponse({"success": 'New admin is Created'})
            else:
                error=df.errors
                error=json.dumps(error)
                return JsonResponse({"error": df.errors}, status=200)


def viewCourses(request):
    data=CourseTable.objects.all()
    return render(request,"admin/courses.html",{"couses":data})


def addCourses(request):
       if(checksession(request)):
           if request.method == "POST":
               data = request.POST
               try:
                   db=CourseTable(name=data['coursename'],fee=float(data['coursefee']))
                   db.save()
                   messages.success(request,"Course is Added")
                   return redirect("addCourse")
               except IntegrityError:
                   messages.error(request,"Course is already Exists")
                   return render(request, "admin/addcourse.html")


           else:
               return render(request,"admin/addcourse.html")
       else:
           return redirect("login")


def scheduleform(request):
    if(checksession(request)):
        if request.method == "POST":
            data=request.POST
            frm=scheduleclass(data)
            if frm.is_valid():
                frm.save()
                messages.success(request,"Class Schedule is added")
                return redirect("schedule")
            else:
                return render(request, "admin/scheduleform.html", {"form": data})
        data=scheduleclass()
        return render(request,"admin/scheduleform.html",{"form":data})
    else:
        return redirect("login")


def classeslist(request):
    if (checksession(request)):
        modeldata = ScheduleclassesTable.objects.all()
        return render(request, "admin/classes.html", {"data": modeldata})
    return redirect("login")
