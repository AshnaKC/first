from django.shortcuts import render,redirect,HttpResponse
from .models import Category,Products
from .forms import ProductModelForm,RegistrationForm,EditForm
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def home(request):
    categories= Category.objects.all()
    # users = Users.objects.all()
    context={
    'categories':categories
    }
    return render(request,'home.html',context)
@login_required(login_url='/login/')
def add_product(request):
    if request.method =='POST':
        form = ProductModelForm(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('home')
        else:
            return render(request,'product.html',{'form':form})
    else:
        form = ProductModelForm()
        return render(request,'product.html',{'form':form})
def delete(request,id):
    product = Products.objects.get(id=id)
    cat_id=product.category.id
    product.delete()
    return redirect(f'/category/{cat_id}/')

def edit_product(request,id):
    product = Products.objects.get(id=id)
    if request.method =='POST':
        form = ProductModelForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request,'product.html',{'form':form})
    else:
        form = ProductModelForm(instance=product)
        return render(request,'product.html',{'form':form})
@login_required(login_url='/login/')
def show_product(request,id):
    category = Category.objects.get(id=id)
    products = category.products_set.all()
    context={
        'products':products
    } 
    return render(request,'show_product.html',context)
def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request,'register.html',{'form':form})
    else:
        form = RegistrationForm()
        return render(request,'register.html',{'form':form})
def login_page(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('username or password is incorrect')
    return render(request,'login.html')
def logout_fn(request):
    logout(request)
    return redirect('/login/')
def edit_user(request):
    if request.method =='POST':
        form = EditForm(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request,'product.html',{'form':form})
    else:
        form = EditForm(instance=request.user)
        return render(request,'product.html',{'form':form})
def change_password(request):
    if request.method =='POST':
        form =PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('home')
        else:
            return render(request,'product.html',{'form':form})
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request,'product.html',{'form':form})





