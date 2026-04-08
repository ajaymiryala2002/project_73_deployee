from django.contrib import admin

from app.models import employee


class employee_admin(admin.ModelAdmin):
    list_display=['emp_name','emp_id','emp_salary']
    
admin.site.register(employee,employee_admin)
