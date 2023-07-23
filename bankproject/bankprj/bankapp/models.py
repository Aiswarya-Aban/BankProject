from django.db import models

# Create your models here.

class Forms(models.Model):
    # genderchoices=(
    #     ('M','male'),
    #     ('F','female'),
    # )
    # accchoices = (
    #     ('S','savings'),
    #     ('C','current'),
    # )
    # distchoices=(
    #     ('Alapuzha','dist1'),
    #     ('Ernakulam','dist2'),
    #     ('Idukki','dist3'),
    #     ('Kottayam','dist4'),
    #     ('Kozhikode','dist5'),
    #     ('Palakkad','dist6'),
    # )
    # branchchoices=(
    #     ('br1', 'Cherthala'),
    #     ('br2', 'Kuttanad'),
    #     ('br3', 'Pattanakkad'),
    #     ('br4', 'Aluva'),
    #     ('br5', 'Eloor'),
    #     ('br6', 'Paravur'),
    #     ('br7', 'Adimali'),
    #     ('br8', 'Kattappana'),
    #     ('br9', 'Munnar'),
    #     ('br10', 'Ettumanoor'),
    #     ('br11', 'Kumarakam'),
    #     ('br12', 'Vaikom'),
    # )
    uname=models.CharField(max_length=250,default=True)
    dob=models.CharField(max_length=20,default=True)
    age=models.IntegerField(default=True)
    gender=models.CharField(max_length=10,default=True)
    phn=models.IntegerField(default=True)
    mail=models.EmailField(unique=True,default=True)
    dist=models.CharField(max_length=50,default=True)
    branch=models.CharField(max_length=50,default=True)
    acc=models.CharField(max_length=50,default=True)
    material=models.BooleanField(default=False)

    def __str__(self):
        return self.uname