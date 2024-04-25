from django.db import models

# Create your models here.
class  info(models.Model):
    name = models.CharField(max_length=32,null=False)
    email = models.EmailField(unique=True ,null=False)
    msg =  models.TextField(null=False)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self) :
        return self.name+" - "+str(self.date)
    
class Donation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    message = models.TextField()

    def __str__(self) :
        return self.name+" - "+str(self.amount)
    
class UserCreationForm(models.Model):
    username = models.CharField(max_length=32,null=False)
    password = models.CharField(max_length=16)
    
    def createUser(self):
        return self.username()

