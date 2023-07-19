from django.contrib import admin
from .models import Country,Portfolio,Socials,Tags

for item in [Country,Socials,Tags]:

    admin.site.register(item)

class PortfolioAdmin(admin.ModelAdmin):
    exclude = ('modification_key',)

admin.site.register(Portfolio, PortfolioAdmin)

admin.site.site_header = "Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Welcome to Cameroon Portfolio admin panel"
