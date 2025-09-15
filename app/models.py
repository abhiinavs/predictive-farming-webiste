from django.db import models

# Create your models here.
class login_table(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)


class farmer_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    place= models.CharField(max_length=100)
    Post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    images = models.FileField()

class user_table(models.Model):
    LOGIN = models.ForeignKey(login_table, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Place = models.CharField(max_length=100)
    Post = models.CharField(max_length=100)
    Phone = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Image = models.FileField()


class expert_table(models.Model):
    LOGIN = models.ForeignKey(login_table, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Place = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    # gender= models.CharField(max_length=100)
    Phone = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Image = models.FileField()

#
#
class crop_table(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    stock = models.CharField(maxbt_length=100)


class notification_table(models.Model):
    date=models.DateField(max_length=100)
    notification=models.CharField(max_length=100)
    time=models.TimeField(max_length=100)

class doubt_table(models.Model):
    FARMER=models.ForeignKey(farmer_table, on_delete=models.CASCADE)
    # EXPERT=models.ForeignKey(expert_table, on_delete=models.CASCADE)
    doubt=models.CharField(max_length=100)
    date=models.DateField()
    reply=models.CharField(max_length=100)

class product_table(models.Model):
    FARMER=models.ForeignKey(farmer_table, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    image=models.FileField()
    stock=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    details=models.CharField(max_length=100)

class order_product(models.Model):
    user_id=models.ForeignKey(user_table,on_delete=models.CASCADE)
    total_amount=models.CharField(max_length=100)
    date=models.DateField(max_length=100)
    status=models.CharField(max_length=100)

class order_details(models.Model):
    ORDER=models.ForeignKey(order_product,on_delete=models.CASCADE)
    PRODUCT=models.ForeignKey(product_table,on_delete=models.CASCADE)
    quantity=models.IntegerField()

class complaint_table(models.Model):
    user_id=models.ForeignKey(login_table,on_delete=models.CASCADE)
    complaint=models.CharField(max_length=100)
    date=models.DateField()
    reply=models.CharField(max_length=100)

class feedback_table(models.Model):
    USER_ID=models.ForeignKey(login_table,on_delete=models.CASCADE)
    feedback=models.CharField(max_length=100)
    rating=models.CharField(max_length=10)
    date=models.DateField()

class fertilizer_table(models.Model):
    name=models.CharField(max_length=100)
    image=models.FileField()
    details=models.CharField(max_length=100)


class soil_table(models.Model):
    soil_type=models.CharField(max_length=100)
    details=models.CharField(max_length=100)
    EXPERT_ID = models.ForeignKey(expert_table, on_delete=models.CASCADE)


class tips_table(models.Model):
    tips=models.CharField(max_length=100)
    Details=models.CharField(max_length=100)
    EXPERT_ID=models.ForeignKey(expert_table,on_delete=models.CASCADE)

class complaints(models.Model):
    user_id = models.ForeignKey(login_table, on_delete=models.CASCADE)
    complaint=models.CharField(max_length=100)
    reply=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
















































































































































