from django.contrib import admin
from .models import Specialization ,Designation,AvailableTime,Doctor

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','image','meet_link' ,'fee']

    def first_name(self,obj):
        return obj.user.first_name
    
    def last_name(self,obj):
        return obj.user.last_name
    
class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Specialization,SpecializationAdmin)
admin.site.register(Designation,DesignationAdmin)
admin.site.register(AvailableTime)