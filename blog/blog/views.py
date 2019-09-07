from django.http import HttpResponse
def index(request):
	return HttpResponse("<script>document.location='account/register/5'</script>")
