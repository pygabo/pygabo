from django.contrib import admin
from .models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'owner']


admin.site.register(Person, PersonAdmin)
