from django.db import models

class employee(models.Model):
    emp_name = models.CharField(max_length=20)
    emp_id = models.IntegerField(unique=True)
    emp_salary = models.FloatField()
