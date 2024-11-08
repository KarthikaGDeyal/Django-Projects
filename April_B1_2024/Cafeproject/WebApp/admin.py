from django.contrib import admin
from WebApp.models import ContactInfoDb,FooterDb,AboutDb

@admin.register(ContactInfoDb)
class ContactInfoDbAdmin(admin.ModelAdmin):
    list_display = ('Place', 'Address', 'Phone', 'Email','Description')

@admin.register(FooterDb)
class FooterDbAdmin(admin.ModelAdmin):
    list_display = ('Description1', 'Description2', 'Description3','Description4','Email')

@admin.register(AboutDb)
class AboutDbAdmin(admin.ModelAdmin):
    list_display = ('Description','Description1')


