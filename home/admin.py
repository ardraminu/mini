from django.contrib import admin
from.models import District, Taluk, User, Vaccine, Vaccine_center, Vaccination, User_vaccine_registration


# Register your models here.

admin.site.register(District)
admin.site.register(Taluk)
admin.site.register(User)
admin.site.register(Vaccine)
admin.site.register(Vaccine_center)

admin.site.register(Vaccination)
admin.site.register(User_vaccine_registration)