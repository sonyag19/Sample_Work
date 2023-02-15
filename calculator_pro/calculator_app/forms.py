from django import forms

class regform(forms.Form):
    name=forms.CharField(max_length=30)
    email=forms.EmailField()
    password=forms.CharField(max_length=20)
    confirm=forms.CharField(max_length=20)

class reg2form(forms.Form):
    fname=forms.CharField(max_length=20)
    lname=forms.CharField(max_length=20)
    email=forms.EmailField()
    phone=forms.IntegerField()
    addr=forms.CharField(max_length=40)

class loginform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=20)

class searchform(forms.Form):
    name=forms.CharField(max_length=20)
    email=forms.EmailField()
    phone=forms.IntegerField()

class fileform(forms.Form):
    iname=forms.CharField(max_length=20)
    iprice=forms.IntegerField()
    des=forms.CharField(max_length=50)
    image=forms.FileField()

class regbootform(forms.Form):
    fname=forms.CharField(max_length=30)
    lname=forms.CharField(max_length=30)
    email=forms.EmailField()
    password=forms.CharField(max_length=20)
    repassword=forms.CharField(max_length=20)

class loginbootform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=20)




