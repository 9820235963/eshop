from django.contrib import admin

from myApp.models import Student,Category,Product

# Register your models here.
admin.site.register(Student)
admin.site.register(Category)
admin.site.register(Product)