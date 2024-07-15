from django.shortcuts import render,redirect
from app1 .models import doctordetails
from . models import *
from my_python_project.models import Userdetailss 

# Create your views here.
def index2(request):
    return render(request,'index2.html')
def doctoruserviews(request):
    return render(request,'doctor_adminviews.html')
def doctorbooking(request):
    u_id=request.session['uid']
    if request.method=="POST":
        ptname=request.POST.get("ptname")
        ptemail=request.POST.get("ptemail")
        ptmobile=request.POST.get("ptmobile")
        ptdoctor=request.POST.get("ptdoctor")
        ptdate=request.POST.get("ptdate")
        pttime=request.POST.get("pttime")
        data=appointmentss(u_id=u_id,ptname=ptname,ptemail=ptemail,ptmobile=ptmobile,ptdoctor=ptdoctor,ptdate=ptdate,pttime=pttime)
        data.save()
    data1=doctordetails.objects.all()
    return render(request,'doctor_booking.html',{'result1':data1})

def userprofile(request):
    u_id=request.session['uid']
    data=Userdetailss.objects.get(pk=u_id)
    return render(request,'userprofile.html',{'res':data})

def appointment_delete(request,id):
    m=appointmentss.objects.get(pk=id)
    m.delete()
    return redirect(appointment_view)

def appointment_update(request,id):
    data1=doctordetails.objects.all()
    data=appointmentss.objects.get(pk=id)
    return render(request,'appointment_update.html',{'result':data, 'res':data1})

def appointments_update(request,id):
    u_id=request.session['uid']
    if request.method=="POST":
        ptname=request.POST.get("ptname")
        ptemail=request.POST.get("ptemail")
        ptmobile=request.POST.get("ptmobile")
        ptdoctor=request.POST.get("ptdoctor")
        ptdate=request.POST.get("ptdate")
        pttime=request.POST.get("pttime")
        data=appointmentss(u_id=u_id,ptname=ptname,ptemail=ptemail,ptmobile=ptmobile,ptdoctor=ptdoctor,ptdate=ptdate,pttime=pttime,id=id)
        data.save()
        return redirect(appointment_view)
    return render(request,'appointment_update.html')


def appointment_view(request):
    u_id=request.session['uid']
    data=appointmentss.objects.filter(u_id=u_id)
    return render(request,'appointment_views.html',{'result':data})