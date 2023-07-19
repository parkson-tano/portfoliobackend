from django.contrib import admin
from .models import Country,Portfolio,Socials,Tags

for item in [Country,Portfolio,Socials,Tags]:

    admin.site.register(item)