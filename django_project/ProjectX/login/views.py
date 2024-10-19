from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == "POST":
        user_ka_name=request.POST.get("username")
        user_ka_password=request.POST.get("password")

        user = auth.authenticate(request, username=user_ka_name, password=user_ka_password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.error(request,"Please check username and password again")
            return redirect("/login")




    else:    
        return render (request,'login.html')

def register(request):

    if request.method == "POST":
        f_name=request.POST.get("firstname")
        l_name=request.POST.get("lastname")
        email=request.POST.get("email")
        username=request.POST.get("username")
        password1=request.POST.get("password")
        password2=request.POST.get("confirm_password")

        if password1 == password2:

            if User.objects.filter(username=username).exists():

                messages.error(request,"sorry username alreday taken")
                return redirect('/login/register')
            
            elif User.objects.filter(email=email).exists():
                messages.error(request,"sorry email already taken")
                return redirect('/login/register')
                
            
            else:
                user = User.objects.create_user(first_name=f_name, last_name=l_name, email=email, username=username, password=password1)
                user.save()
                print("created success ")
                return redirect("/login")



        else:
            messages.error(request," please check again password is not the same ")
            return redirect('/login/register')   


    else:
        return render (request,'register.html')
    

def logout(request):
    auth.logout(request) 
    return redirect("/")