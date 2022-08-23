from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=250, null=False, blank=False)

	def __str__(self):
		return self.name

class Post(models.Model):
	category = models.ForeignKey(Category,blank=False,null=True,on_delete=models.SET_NULL)
	title = models.CharField(max_length=200)
	image = models.ImageField(upload_to='images/')
	body = models.TextField()

	def __str__(self):
		return self.title

# python manage.py makemigrations  # models.py dagi yangilanishlarni saqlaydi
# python manage.py migrate  # db baza yaratb beradi

# python manage.py createsuperuser # bu buyruq admin panelga kirishimiz uchun user yaratb beradi