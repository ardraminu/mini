from django.db import models

# Create your models here.


class District(models.Model):
    did = models.CharField(max_length=20,primary_key=True)
    district = models.CharField(max_length=200)

    def __str__(self):
        return self.district
    

class Taluk(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="taluk")
    taluk = models.CharField(max_length=200)  

    def __str__(self):
        return  self.district, self.taluk 



class Vaccine(models.Model):
    vid = models.IntegerField(primary_key=True)
    vname =  models.CharField(max_length=122)  

    def __str__(self):
        return self.vname    


class User(models.Model):
    aadhar = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=122)
    age= models.IntegerField()
    address = models.TextField(max_length=122)
    phone= models.CharField(max_length=10)
    email = models.CharField(max_length=122) 

    def __str__(self):
        return self.name, str(self.aadhar)



class Vaccine_center(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="vaccine_center")
    taluk = models.ForeignKey(Taluk, on_delete=models.CASCADE, related_name="vaccine_center")
    center_name = models.CharField(max_length=255)
    date_avail1 = models.DateField(blank=True, null=True) 
    date_avail2 = models.DateField(blank=True, null=True)      
    def __str__(self):
        return self.center_name


class Vaccination(models.Model):
    aadhar = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Vaccination")
    name = models.CharField(max_length=255)
    vid = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    dose1 = models.DateField(blank=True, null=True) 
    dose2 = models.DateField(blank=True, null=True) 
    def __str__(self):
        return self.name
        # str(self.aadhar)
   

    
class User_vaccine_registration(models.Model):
    aadhar= models.ForeignKey(User, on_delete=models.CASCADE, related_name="User_vaccine_registration")
    name = models.CharField(max_length=255)
    did = models.ForeignKey(District, on_delete=models.CASCADE)
    date_avail = models.ForeignKey(Vaccine_center, on_delete=models.CASCADE)
       
    def __str__(self):
        return self.name