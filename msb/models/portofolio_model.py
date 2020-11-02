import os
from django.conf import settings
from django.db import models

# Create your models here.
class Portofolio(models.Model):
	porto_id = models.AutoField(primary_key=True)
	porto_project_name = models.CharField(max_length=100)
	porto_project_desc = models.TextField()
	porto_created_by = models.CharField(max_length=100)
	porto_photo = models.ImageField(upload_to='msb/assets/images/portofolio', max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

# class Template(models.Model):
# 	temp_id = models.AutoField(primary_key=True)
# 	temp_code = models.CharField(max_length=100)
# 	temp_name = models.CharField(max_length=100)
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	updated_at = models.DateTimeField(auto_now=True)

# class Customers(models.Model):
# 	cust_id = models.AutoField(primary_key=True)
# 	cust_name = models.CharField(max_length=100)
# 	cust_address = models.TextField()
# 	cust_email = models.CharField(max_length=100)
# 	cust_photo = models.ImageField(upload_to='msb/assets/images/customers', max_length=100)
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	updated_at = models.DateTimeField(auto_now=True)

# class Order(models.Model):
# 	order_id = models.AutoField(primary_key=True)
# 	temp = models.ForeignKey(Template,on_delete=models.CASCADE)
# 	order_subfolder = models.CharField(max_length=100)
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	updated_at = models.DateTimeField(auto_now=True)

# class OrderCustDetail(models.Model):
# 	ocd_id = models.AutoField(primary_key=True)
# 	order = models.ForeignKey(Order,on_delete=models.CASCADE)
# 	cust = models.ForeignKey(Customers,on_delete=models.CASCADE)
# 	ocd_cust_status = models.CharField(max_length=100)
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	updated_at = models.DateTimeField(auto_now=True)

# class OrderAcaraDetail(models.Model):
# 	oad_id = models.AutoField(primary_key=True)
# 	order = models.ForeignKey(Order, on_delete=models.CASCADE)
# 	oad_tittle = models.CharField(max_length=30)
# 	oad_start_time = models.DateTimeField()
# 	oad_end_time = models.DateTimeField()
# 	oad_place = models.TextField()
# 	oad_maps = models.URLField(max_length=200)
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	updated_at = models.DateTimeField(auto_now=True)

# class OrderGaleriDetail(models.Model):
# 	oid_id = models.AutoField(primary_key=True)
# 	order = models.ForeignKey(Order, on_delete=models.CASCADE)
# 	oid_photo = models.ImageField(upload_to='msb/assets/images/ordergaleri', max_length=100)
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	updated_at = models.DateTimeField(auto_now=True)

# class OrderVideoDetail(models.Model):
# 	ovd_id = models.AutoField(primary_key=True)
# 	order = models.ForeignKey(Order, on_delete=models.CASCADE)
# 	ovd_desc = models.CharField(max_length=30)
# 	ovd_url = models.URLField(max_length=200)
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	updated_at = models.DateTimeField(auto_now=True)

# class OrderQuotesDetail(models.Model):
# 	oqd_id = models.AutoField(primary_key=True)
# 	order = models.ForeignKey(Order, on_delete=models.CASCADE)
# 	oqd_quote = models.TextField()
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	updated_at = models.DateTimeField(auto_now=True)

# class OrderTamuDetail(models.Model):
# 	otd_id = models.AutoField(primary_key=True)
# 	order = models.ForeignKey(Order, on_delete=models.CASCADE)
# 	otd_ucapan = models.TextField()
# 	otd_status = models.IntegerField()
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	updated_at = models.DateTimeField(auto_now=True)