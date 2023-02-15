from django.db import models

# Create your models here.
class regmodel(models.Model):  # table created
    name=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=20)

class reg2model(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.IntegerField()
    addr=models.CharField(max_length=40)

class filemodel(models.Model):
    iname=models.CharField(max_length=20)
    iprice=models.IntegerField()
    des=models.CharField(max_length=50)
    image=models.FileField(upload_to="calculator_app/static")

class regbootmodel(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    repassword=models.CharField(max_length=20)


