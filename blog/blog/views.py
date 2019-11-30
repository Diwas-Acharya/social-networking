from django.http import HttpResponse
from django.shortcuts import render
def index(request):
	return HttpResponse("<script>document.location='account/register/5'</script>")


def saurav(request):
	return render(request,"savrav.html",{})
