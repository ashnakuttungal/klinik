from django.shortcuts import render, redirect
from . models import *
# Create your views here.
def index1(request):
    return render(request,'index1.html')

def adddoctor(request):
    if request.method=="POST":
        docname=request.POST.get("docname")
        docspecification=request.POST.get("docspecification")
        docemail=request.POST.get("docemail")
        docphoto=request.FILES["docphoto"]
        data=doctordetails(docname=docname,docspecification=docspecification,docemail=docemail,docphoto=docphoto)
        data.save()
    return render(request,'add_doctors.html')

def doctoradviews(request):
    data=doctordetails.objects.all()
    return render(request,'doctor_adminviews.html',{'result':data})


def doctordelete(request,id):
    m=doctordetails.objects.get(pk=id)
    m.delete()
    return redirect(doctoradviews)

def doctorupdate(request,id):
    data=doctordetails.objects.get(pk=id)
    return render(request,'doctor_update.html',{'result':data})

def doctor_update(request,id):
    if request.method=="POST":
        docname=request.POST.get("docname")
        docspecification=request.POST.get("docspecification")
        docemail=request.POST.get("docemail")
        docphoto=request.FILES["docphoto"]
        data=doctordetails(docname=docname,docspecification=docspecification,docemail=docemail,docphoto=docphoto,id=id)
        data.save()
        return redirect(doctoradviews)
    return render(request,'doctor_update.html')

def adminprofile(request):
    return render(request,'adminprofile.html')


