from django.shortcuts import render,redirect
from . models import *

# Create your views here.
def pro1(request):
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')

def user_register(request):
    if request.method=="POST":
        username=request.POST.get("username")
        useremail=request.POST.get("useremail")
        usermobile=request.POST.get("usermobile")
        userpassword=request.POST.get("userpassword")
        data=Userdetailss(username=username,useremail=useremail,usermobile=usermobile,userpassword=userpassword)
        data.save()
    return render(request,'user_register.html')

def user_login(request):
    useremail = request.POST.get('useremail')
    userpassword = request.POST.get('userpassword')
    if useremail == 'admin@gmail.com' and userpassword =='admin':
        request.session['adminemail'] = useremail
        request.session['admin'] ='admin'
        return render(request,'index.html',{'status': 'admin login successfull'} )
 
    elif Userdetailss.objects.filter(useremail=useremail,userpassword=userpassword).exists():
        udet=Userdetailss.objects.get(useremail=request.POST['useremail'],userpassword=userpassword)
        if udet.userpassword == request.POST['userpassword']:
            request.session['uid'] = udet.id
            request.session['uname'] = udet.username
            request.session['uemail'] = useremail
            request.session['user'] = 'user'
            return render(request,'index.html',{'status': 'user login successfull'})
 
    else:
            return render(request, 'user_login.html', {'status': 'incorrect credentials'})
 
def user_views(request):
    data=Userdetailss.objects.all()
    return render(request,'user_views.html',{'result':data})
def userdelete(request,id):
    m=Userdetailss.objects.get(pk=id)
    m.delete()
    return redirect(user_views)
def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(pro1)