from django.db import models

# Create your models here.
class details(models.Model):
	uid = models.IntegerField()
	image = models.FileField(upload_to='account/images',default="profile.png")
	livein = models.CharField(max_length = 200,default = "")
	nick_name = models.CharField(max_length = 200,default = "")
	work = models.CharField(max_length = 200,default = "")
	dob = models.DateField(default = "")
	status = models.CharField(max_length = 200,default = "")
	name = models.CharField(default="",max_length=200)
	adress = models.CharField(default="",max_length=200)

	def __str__(self):
		return self.nick_name
