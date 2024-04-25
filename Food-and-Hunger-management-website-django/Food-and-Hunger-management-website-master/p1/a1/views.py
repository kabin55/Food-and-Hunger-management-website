from django.shortcuts import render,redirect
from a1.forms import info2 ,SignupForms,LogInForm,DonationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
 

# Create your views here.
def home(request):
    return  render(request, 'index.html')

def a(request):
    return render(request,'a.html')

def aboutus(request):
    return render(request,'aboutus.html')

def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donate_success')
    else:
        form = DonationForm()
    return render(request, 'donate.html', {'form': form})

def donate_success(request):
    return render(request, 'succes.html')

def information(request):
    return render(request,'information.html')

def login(request):
    if request.method =="POST":
        form =  LogInForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            messages.success(request,"YOU have been logged in successfully!")
            return redirect("donate")
        else:
            messages.error(request,"invalid user name or password. Please try again")
    else:
        form = LogInForm()
    return  render(request, 'signin.html',{ "form" : form})

def signup(request):
    if request.method == 'POST':
        form = SignupForms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            messages.success(request, f'Account created for {username}!')
            # login(request, user)
           
            return redirect('/donate/')  # Redirect to the home page after successful 
        else:
            error_message = ', '.join([f'{k}: {v[0]}' for k, v in form.errors.items()])
            messages.error(request, f'Error creating account. Please correct the errors below: /n{error_message}')
            # messages.error(request, 'Error creating account. Please correct the errors below.')
    else:
        form = SignupForms()
    return render(request, 'signup.html', {'form': form})

def contact(request):
    form = info2()
    if  request.method == 'POST':
        form = info2(request.POST )
        if form.is_valid():
            form.save()
            messages.success(request,"message recorded!!!")
    context = {'form':form}
    return render(request,'contactus.html',context)

# def (request):

#     return  render(request, '.html')
