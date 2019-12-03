from django.db import models

# Create your models here.
class addcontestent(models.Model):
    contestent_name=models.CharField(max_length=20)
    ocuupation=models.CharField(max_length=20)
    age=models.IntegerField()
    born=models.DateField()
    origin=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)
    image=models.ImageField(blank=True)


    def __str__(self):
        return self.contestent_name

class regmodel(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()

    def __str__(self):
        return self.username

class votingmodel(models.Model):
    contestent_name=models.CharField(max_length=20)
    votes=models.IntegerField()

    def __str__(self):
        return self.contestent_name