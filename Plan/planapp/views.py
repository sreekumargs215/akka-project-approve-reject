from django.shortcuts import render,redirect
from .models import Profile,Plan,Deposit,User
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib import messages

def index(request):

 show=Plan.objects.all()
 return render(request,"index.html",{'show':show})


def deposit(request):
  
    user = User.objects.all()
    if request.method == 'POST':
        
         amount=request.POST["amount"]
         image=request.POST["image"]
         user= User.objects.get(id=request.user.id)
         Deposit.objects.create(username=user,amount=amount,image=image)
         return redirect('/admin1')
    return render(request,"deposit.html")



def register(request):
    if request.method == 'POST':
        data=request.POST
        print(data)
        uform = SignUpForm(request.POST)

        if uform.is_valid():
            uform.save()
            messages.success(request, 'Form submission successful')
            City=data['city']
            phone=data['phone']
            email=data['email']
            country=data['country']
            data = Profile.objects.create(user_id=uform.instance.id,phone=phone,city=City,email=email,country=country)
       

            return redirect('/login')
        else:
            print(uform.errors)
            
    return render(request, 'register.html')



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        # twofa=request.POST['twofa']
        user = authenticate(request, username=username, password=password1)
        print(user)
        if user is not None:
            # user_data=Profile.objects.get(user_id=user.id)
            # totp = pyotp.TOTP(user_data.twofa)
            # if totp.now()==twofa:
                login(request, user)
                print(request.user)
                return redirect('/') 
        else:
            # messages.success(request, "Error. Message not sent.")
            msg="Invalid username"
            return render(request, 'login.html',{"msg":msg})

    return render(request, 'login.html')




def admin_login(request):
 if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        user = authenticate(request, username=username, password=password1)
        if user is not None and user.is_superuser==True:
            login(request, user)
            print(request.user.is_superuser)
            return redirect('/admin1') 
 return render(request, 'adminlogin.html')

def admin1(request):

    user12=Profile.objects.all()
    us123=Plan.objects.all()
    dep=Deposit.objects.all()
    return render(request, 'admin1.html',{'nivi':us123,'nivi1':user12,'dep':dep})
   


def user_logout(request):
    logout(request)
    return redirect('/')


# def buy_plan(request,pk):

#     buy=Plan.objects.get(id=pk) 
#     if request.method == 'POST':
#       plan_type=request.POST["plan_type"]
#       plan_per=request.POST["plan_per"]
#       profit=request.POST["profit"]
#       price=request.POST["price"]
#       Plan.objects.create(plan_type=plan_type,plan_per=plan_per,profit=profit,price=price)
     
#       return redirect('/')
#     return render(request,'buy.html',{"buy":buy})
def add_plan(request):
     if request.method == 'POST':
       plan_type=request.POST["plan_type"]
       plan_per=request.POST["plan_per"]
       profit=request.POST["profit"]
       price=request.POST["price"]
       Plan.objects.create(plan_type=plan_type,plan_per=plan_per,profit=profit,price=price)
       return redirect('/admin1')
     return render(request,"addplan.html")



def edit_plan(request,pk):
     
     edit1=Plan.objects.get(id=pk) 
     if request.method == 'POST':
         plan_type=request.POST["plan_type"]
         plan_per=request.POST["plan_per"]
         profit=request.POST["profit"]
         price=request.POST["price"]
         
         Plan.objects.filter(id=pk).update(plan_type=plan_type,plan_per=plan_per,profit=profit,price=price)
         return redirect('/admin1')
    
     return render(request,"edit.html",{"edit":edit1})



def del_plan(request,pk):
#   if request.method == 'POST':       
   del1=Plan.objects.get(id=pk) 
   del1.delete()
   return redirect('/admin1')


def update(request,dk):
     dep1=Deposit.objects.get(id=dk) 
     if request.method == 'POST':
        username=["username"]
        amount=request.POST["amount"]
        Profile.objects.filter(id=dk).update(amount=amount)
     
        return redirect('/admin1')
     return render(request,"update.html",{"dep1":dep1})

def accept(request,dk):
    div=Deposit.objects.get(id=dk)
    if request.method == 'POST':
        damount=request.POST["amount"]
        pro=Profile.objects.get(user_id=request.user.id)
        pro.amount=damount
        print(damount)
     
 
    return render(request,"admin1.html")




# def buy_book(request,pk):

#     buy=Book.objects.get(id=pk) 
#     # uname=request.user
#     # user=Profile.objects.get(id=pk)
#     if request.method == 'POST':
#       name=request.POST["name"]
#       bname=request.POST["bname"]
#       price=request.POST["price"]
#       BookHistory.objects.create(user_name=name,book_name=bname,price=price)
#       pro=Profile.objects.get(user_id=request.user.id)
#       totalamount=pro.amount
#       rem=totalamount-buy.price
#       totalamount=int(rem)
#       print(int(rem))
#       pro.amount=totalamount 
#       pro.save()
#       return redirect('/')
#     return render(request,'buy.html',{"buy":buy})
