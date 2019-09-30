<<<<<<< HEAD
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
	return HttpResponse("<script>document.location='account/register/5'</script>")


def saurav(request):
	return render(request,"savrav.html",{})
=======
from django.http import HttpResponse
def index(request):
	return HttpResponse("<script>document.location='account/register/5'</script>")
>>>>>>> cc1c517a828147c4443c82bd127b223322e1666a
