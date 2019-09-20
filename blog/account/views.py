from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from account.models import details


# Create your views here.

def register(request,id):
	if id==1:
		print("signup")
		if request.method == 'POST':
			fname = request.POST["fname"]
			lname = request.POST["lname"]
			username1 = request.POST["username2"]
			email = request.POST["email"]
			password1 = request.POST["password1"]
			password2 = request.POST["password2"]

			if password2==password1:
				if User.objects.filter(username=username1).exists():
					messages.info(request,"This user name is alreadey taken try another one")
				elif User.objects.filter(email=email).exists():
					messages.info(request,"This email is alreadey taken try another one")
				else:
					user = User.objects.create_user(username=username1,password=password1,email=email,first_name=fname,last_name=lname)
					user.save()
					messages.info(request,"Account sucessfully created")
					return redirect("/account/register/{num}".format(num = 5))
			else:
				messages.info(request,"conform password is not matching")
				return redirect("/account/register/{num}".format(num = 5))
		return render(request,"signup.html")
			
	if id==2:
		print("login")
		if request.method=='POST':
			username2 = request.POST["username1"]
			password = request.POST["password"]
			user = auth.authenticate(username=username2,password=password)
			if user is not None:
				auth.login(request,user)
				return redirect("/account/profile/{num}".format(num = user.id))
			else:
				messages.info(request,"Invalid credintals")
				return redirect("/account/register/{num}".format(num = 5))
			return render(request,'signup.html')
		return render(request,'signup.html')
	else:
		print("random")
		return render(request,"signup.html")

@login_required(login_url='/account/register/5')
def profile(request,myid):
	user = User.objects.filter(id=myid)
	allposts = User.objects.all()[1:]
	uname =user[0].username
	username =user[0].username
	name = user[0].first_name
	lname = user[0].last_name
	email = user[0].email
	return render(request,"profile.html",{'username':username,'uname':uname,'name':name,'lname':lname,'email':email,"id":myid,"allposts":allposts})

@login_required(login_url='/account/register/5')
def userprofile(request,userid):
	user = User.objects.filter(id=userid)
	username =user[0].username
	name = user[0].first_name
	lname = user[0].last_name
	email = user[0].email

	if request.method=='POST':
		image = request.FILES["image"]
		name = request.POST["name"]
		livein = request.POST["livein"]
		nickname = request.POST["nickname"]
		work = request.POST["work"]
		dob = request.POST["dob"]
		status = request.POST["status"]
		alldetail = details(uid = userid ,name = name, image = image , livein = livein , nick_name = nickname , work = work ,dob = dob ,status = status)
		alldetail.save()

	return render(request,"userprofile.html",{'username':username,'name':name,'lname':lname,'email':email,"id":userid})

@login_required(login_url='/account/register/5')
def usernotifications(request,userid):
	user = User.objects.filter(id=userid)
	username =user[0].username
	name = user[0].first_name
	lname = user[0].last_name
	email = user[0].email
	return render(request,"notification.html",{'username':username,'name':name,'lname':lname,'email':email,"id":userid})

@login_required(login_url='/account/register/5')
def userchat(request,userid):
	user = User.objects.filter(id=userid)

	username =user[0].username
	name = user[0].first_name
	lname = user[0].last_name
	email = user[0].email
	return render(request,"chat.html",{'username':username,'name':name,'lname':lname,'email':email,"id":userid})


@login_required(login_url='/account/register/5')
def userfriends(request,userid):
	user = User.objects.filter(id=userid)
	allposts = User.objects.all()[1:]
	pic = details.objects.all()
	username =user[0].username
	name = user[0].first_name
	lname = user[0].last_name
	email = user[0].email
	users = []
	alluser=[]
	picture = []
	for name in allposts:
		if name.username==username:
			pass
		else:
			users.append(name)
	for nam in pic:
		if nam.name==username:
			pass
		else:
			picture.append(nam)

	for x in users:
		for y in picture:
			if x.username == y.name:
				lists = x,y
				alluser.append(lists)
	


	for x in users:
		print(x.username)
	for x in picture:
		print(x.name)

	

	ctx = {
	 'pic':picture,
	 'username':username,
	 'name':name,
	 'lname':lname,
	 'email':email,
	 "id":userid,
	 "users":users,
	 "alluser":alluser
	}

	return render(request,"friends.html",ctx)



def logut(request):
	return redirect("/account/profile/5")

@login_required(login_url='/account/register/5')
def userdetailes(request,userid,friendid):
	user = User.objects.filter(id=userid)
	holder = User.objects.filter(id=friendid)
	detail = details.objects.filter(uid=friendid)
	username =user[0].username
	name = user[0].first_name
	lname = user[0].last_name
	email = user[0].email
	friendusername =holder[0].username
	friendname = holder[0].first_name
	friendlname = holder[0].last_name
	friendemail = holder[0].email
	if len(detail)>0:
		x = [
        detail[0].livein,
		detail[0].image,
		detail[0].nick_name,
		detail[0].work,
		detail[0].dob,
		detail[0].status
		]
	else:
		x = ["NA","NA","NA","NA","NA","NA"]
	ctx = {
	     'username':username,
	     'name':name,
	     'lname':lname,
	     'email':email,
	     'friendusername':friendusername,
	     'friendname':friendname,
	     'friendlname':friendlname,
	     'friendemail':friendemail,
	     'userid':userid,
	     'friendid':friendid,
	     'frienddetail':x

	}
	return render(request,"userdetailes.html",ctx)