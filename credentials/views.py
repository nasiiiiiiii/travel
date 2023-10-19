from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect




# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['name']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['pass1']
        cpassword = request.POST['pass2']
        #PASSWORD MATCHING!
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "This username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "This email already exists")
                return redirect('register')
            else:
                #Create new user and store it to database - table name: auth_user (columnName=VariableNAme)
                user1 = User.objects.create_user(username=username, first_name=firstname,
                                                 last_name=lastname, email=email, password=password)
                user1.save()
                return redirect('login')
        else:
            messages.info(request, "Password not matching!")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")
def login(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['pass1']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else :
            messages.info(request, "Invalid")
    return render(request, "login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')


