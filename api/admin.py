from django.contrib import admin
from .models import Country,Portfolio,Socials,Tags

for item in [Country,Socials,Tags]:

    admin.site.register(item)

class PortfolioAdmin(admin.ModelAdmin):
    exclude = ('modification_key',)

admin.site.register(Portfolio, PortfolioAdmin)
