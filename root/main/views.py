from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from main.models import Receipt
from django.contrib.auth.models import User
from main.forms import ReceiptForm, RegistrationForm, LoginForm
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django import forms


# Create your views here.

class RegisterView(View):
    template_name="auth/register.html"
    def get(self,req):
        form = RegistrationForm()
        return render(req,template_name=self.template_name,context={'form':form})


    def post(self,req):
        form = RegistrationForm(req.POST)
        # check whether it's valid:
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password_2 = form.cleaned_data['password_2']
            #If username does not exist, return the error on the username field
            if not username:
                form.add_error('username','Please enter a username') 
            elif password != password_2:
                form.add_error('password','Passwords do not match') 
            #Check if username already used, exists will return true or false
            elif User.objects.filter(username=username).exists():
                form.add_error('username','Username is already taken') 
            else:
                #if there is no error, create a user
                user = User.objects.create(username=username)
                #Use set_password to hash the password instead of storing it in plain text
                user.set_password(password)
                user.save()
                #Avoid having the user to login again by logging him after creating his account
                login(req, user)
                return redirect('receipts')
            
        return render(req,template_name=self.template_name,context={'form':form})

class LoginView(View):
    template_name="auth/login.html"
    def get(self,req):
        form = LoginForm()
        return render(req,template_name=self.template_name,context={'form':form})

    
    def post(self,req):
        try:
            form = LoginForm(req.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                if not username:
                    form.add_error('username','Please enter a username') 
                if not password:
                    form.add_error('password','Please enter a password')
                else:
                    user = authenticate(username=username,password=password)
                    if user:
                        login(req, user)
                        return redirect('receipts')
                    else:
                        form.add_error('username','Wrong credentials') 

        except Exception as e:
            print(e)
        return render(req,template_name=self.template_name,context={'form':form})

        


class ReceiptView(ListView):
    model = Receipt
    template_name='receipts/list.html'

    def get_queryset(self):
        #Show only user's receipts
        return Receipt.objects.filter(user = self.request.user)


class ReceiptDetailView(DetailView):
    model = Receipt
    template_name="receipts/details.html"

class AddReceiptView(FormView):
    template_name = "receipts/add_edit.html"
    form_class = ReceiptForm

    def get_success_url(self):
        return reverse_lazy('receipts')
    
    def form_valid(self, form):
        #Use this to add user to the form as it's not listed with the fields shown to the user
        form.save(user = self.request.user)
        return super().form_valid(form)
    
class EditReceiptView(UpdateView):
    model = Receipt
    fields = ["store_name","item_list","purchase_date","total"]
    template_name = "receipts/add_edit.html"
    widgets = {
        'purchase_date': forms.DateTimeInput(),
    }

    #Make sure to give access only for user's receipts
    def get_object(self):
        #Use filter instead of get (get will give error if receipt not found, filter.first will return None)
        return Receipt.objects.filter(pk=self.kwargs.get('pk'),user = self.request.user).first()

    def get_success_url(self):
        return reverse_lazy('receipts')