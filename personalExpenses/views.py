import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.views import View
from personalExpenses import password
from .models import userExpense
from .forms import ExpenseForm

class index(View):
    
    def get(self, request):
        return render(request,'personalExpenses/index.html')

    def post(self, request):
            
        if 'signin' in request.POST:
            user = authenticate(request=request, username=request.POST['username'], password=request.POST['password'])

            if user is None:
                return render(request,'personalExpenses/index.html', {'error':"Username and password do not match"})

            else:
                login(request, user)
                return redirect('dashboard')
        
        if 'signup' in request.POST:
            if request.POST['password1'] == request.POST['password2']:
                try:
                    #check the password
                    if(password.check(request.POST['password1'])):
                        user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password1'])
                        user.save()
                        login(request, user)
                        return redirect('dashboard')
                    else:
                        return render(request,'personalExpenses/index.html',{'error':'Password must contain an Uppercase, a lower case and a number!'})
                except IntegrityError:
                    return render(request,'personalExpenses/index.html',{'error':'Sorry the user name is already taken!'})
                except ValueError:
                    return render(request,'personalExpenses/index.html',{'error':'Please enter valid username or password!'})
        
            else:
                return render(request,'personalExpenses/index.html',{'error':'The password entered do not match!'})
            
        
def logOutUser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def home(request):
    return render(request, 'personalExpenses/home.html')

def dashboard(request):
    yearData = list(userExpense.objects.filter(user = request.user))
    finaldata = []
    for i in yearData:
        finaldata.append([i.month, i.monthly_earning, i.monthly_expenses, i.monthly_savings])

    finaldata = json.dumps(finaldata)
    print(finaldata)
    if request.method == 'GET':
        return render(request, 'personalExpenses/dashboard.html',{"form": ExpenseForm(), "yearData":finaldata, "user":request.user})
    
"""     else:
        print("retrieve from dashboard")
        monthdata = [request.POST['month'], request.POST['monthly_earning'], request.POST['monthly_expenses'], request.POST['monthly_savings']]

        if request.POST['month'] not in yearData:
            
            try:
                f = ExpenseForm(request.POST)
                print("saving the data")
                if f.is_valid():
                    newExpense = f.save(commit=False)
                    newExpense.user = request.user
                    newExpense.save()
                    print("data saved")
                else:
                    return render(request, 'personalExpenses/dashboard.html', {"data": monthdata, "error": f.errors, "user":request.user})
            except ValueError:
                return render(request, 'personalExpenses/dashboard.html', {"data": monthdata, "error":'Data is invalid', "user":request.user})

            print("sending back the data to dashboard")
            return render(request, 'personalExpenses/dashboard.html', {"data": monthdata, "yearData":"finaldata", "user":request.user})
        
        else:
             return render(request, 'personalExpenses/dashboard.html', {"data": monthdata, "yearData":"finaldata", "error":"Month data already exists, please change the value", "user":request.user})
 """

def new_expenses(request):
    yearData = list(userExpense.objects.filter(user = request.user))
    if request.method == 'GET':
        return render(request, 'personalExpenses/new_expenses.html')
    
    if request.method == 'POST':
        if 'addData' in request.POST:
            print("retrieve from dashboard")
            monthdata = [request.POST['month'], request.POST['monthly_earning'], request.POST['monthly_expenses'], request.POST['monthly_savings'],
                         request.POST['monthly_home_rent'], request.POST['monthly_food_expenses'], request.POST['monthly_travel_expenses'], request.POST['monthly_child_care'],
                         request.POST['monthly_pet_care'], request.POST['monthly_cellphone'], request.POST['monthly_internet'], request.POST['monthly_health_care'],
                         request.POST['monthly_entertainment'], request.POST['monthly_loan'], request.POST['monthly_retirement']]

            if request.POST['month'] not in yearData:
                
                try:
                    f = ExpenseForm(request.POST)
                    print("saving the data")
                    if f.is_valid():
                        newExpense = f.save(commit=False)
                        newExpense.user = request.user
                        newExpense.save()
                        print("data saved")
                    else:
                        return render(request, 'personalExpenses/new_expenses.html', {"data": monthdata, "error": f.errors, "user":request.user})
                except ValueError:
                    return render(request, 'personalExpenses/new_expenses.html', {"data": monthdata, "error":'Data is invalid', "user":request.user})

                print("sending back the data to dashboard")
                return render(request, 'personalExpenses/new_expenses.html', {"data": monthdata, "yearData":"finaldata", "user":request.user})
            
            else:
                return render(request, 'personalExpenses/new_expenses.html', {"data": monthdata, "yearData":"finaldata", "error":"Month data already exists, please change the value", "user":request.user})
        else:
            return render(request, 'personalExpenses/new_expenses.html')

