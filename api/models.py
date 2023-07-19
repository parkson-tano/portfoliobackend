from django.db import models
import random
import string


generate_random_string = lambda: ''.join(random.choices(string.ascii_letters + string.digits, k=20))
class Tags(models.Model):

    name = models.CharField(max_length=255)
    def __str__(self):

        return self.name

class Socials(models.Model):

    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):

        return self.name
    
class Country(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):

        return self.name

class Portfolio(models.Model):

    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    socials = models.ManyToManyField(Socials)
    tags = models.ManyToManyField(Tags)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    modification_key = models.CharField(default="ne met rien ici , je m'en charge",blank=True,null=True)

    def __str__(self):

        return f"{self.name} from {self.country}."
    
    def can_edit(self,key):

        return self.key == self.modification_key

    def save(self,*args,**kwargs):

        self.modification_key = generate_random_string()
        super(Portfolio,self).save(*args,**kwargs)