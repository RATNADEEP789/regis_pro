from django.db import models
# Create your models here.
class registab(models.Model):
    fld_slno=models.AutoField(primary_key=True)
    full_name= models.CharField(db_index=True,max_length=50, null=True)
    dateofbirth= models.DateField(max_length=8)
    gender=models.CharField(db_index=True,max_length=250, null=False)
    mobile_number= models.CharField(db_index=True,max_length=100, null=True)
    email_id=models.TextField(db_index=True,null=True)
    home_town=models.CharField(db_index=True,max_length=250, null=False)
    Username=models.CharField(db_index=True,max_length=250, null=False)
    password=models.CharField(db_index=True,max_length=250, null=False)
    class Meta:
        db_table = "registab"