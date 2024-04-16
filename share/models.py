from django.db import models

# Create your models here.
class Material(models.Model): 
	name = models.CharField(max_length=50) 
	date_of_post = models.DateField()
	quantity = models.IntegerField()
	location = models.CharField(max_length=100)
	zip_code = models.IntegerField()
	mob_no = models.IntegerField(default=False)
	addhar_number = models.IntegerField()
	description = models.TextField(max_length=300) 
	Material_Img = models.ImageField(upload_to='images/')
    
	def __str__(self):
		return self.name



#Volunteer Model+==========================================
class Volt(models.Model): 
	name = models.CharField(max_length=50) 
	date_of_post = models.DateField()
	location = models.CharField(max_length=10)
	zip_code = models.IntegerField()
	mob_no = models.IntegerField(default = '')
	addhar_number = models.IntegerField()
	description = models.TextField(max_length=100)  
	Volt_Img = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.name			