
from django.shortcuts import render
from .models import District, Taluk, Vaccine, User, Vaccination, Vaccine_center

from django.contrib import messages
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect 

# Create your views here.

#-----------------------district------------------------------------------

def districts(request):
    if request.method == 'POST':
        did = request.POST.get('did')
        district = request.POST.get('district')
        district = District(did=did,district=district)
        district.save()
        messages.success(request,"Item Added Succesfully!")
    return render(request,'district.html') 


def view_district(request):
    Districts = District.objects.all().values()
    template = loader.get_template('view_district.html')
    return render(request,'view_district.html', {'District': Districts})
     


# --------------------------Taluk----------------------------------
def taluk(request):
    
        district = District.objects.all()
        context = {
            'district': district,
    
        }

        if request.method == 'POST': 
           taluk = request.POST.get('taluk')
           t = Taluk(district=district, taluk=taluk) 
           t.save()
           messages.success(request, 'Item Added Successfully!')
        return render(request,'taluk.html', context) 
   
        

def view_taluk(request):
    taluk = Taluk.objects.all()
    template = loader.get_template('view_taluk.html')
    return render(request,'view_taluk.html', {'Taluk': taluk})



#-------------------------- Vaccine -------------------------------------------

# to add vaccine
def vaccine(request):
    if request.method == 'POST':
        vid = request.POST.get('vid')
        vname = request.POST.get('vname')
        vacc = Vaccine(vid=vid,vname=vname)
        vacc.save()
        messages.success(request,"Item Added Succesfully!")
    return render(request,'vaccine.html')     


# VIEW VACCINE LIST
def view_vaccine(request):
    vacc = Vaccine.objects.all().values()
    template = loader.get_template('view_vaccine.html') 
    return render(request,'view_vaccine.html', {'Vaccine': vacc})


# delete vaccine
def delete_vaccine(request,vid):
    if request.method =='POST':
       vac = Vaccine.objects.get(pk=vid)
       vac.delete()
       return redirect('view_vaccine')


#-----------------------------------user---------------------------------------------------

# insert user records
def user(request):
    if request.method == "POST":
        aadhar =  request.POST.get('aadhar')
        name =  request.POST.get('name')
        age = request.POST.get('age')
        address =  request.POST.get('address')
        phone =  request.POST.get('phone')
        email =  request.POST.get('email')
        user = User(aadhar=aadhar, name=name, age=age, address=address, phone=phone, email=email)
        user.save()
        messages.success(request, 'Item Added Successfully!')
    return render(request,'user.html') 


# display user record
def user_records(request):
    us = User.objects.all().values()
    template = loader.get_template('user_records.html') 
    return render(request,'user_records.html', {'User': us}) 


# update
def view_user(request,pk):
    us = User.objects.filter(pk=aadhar)
    template = loader.get_template('view_user.html') 
    return render(request,'view_user.html', {'User': us})   

# ------------------------------------------------------------------------------
    
def vaccine_center(request):
  
        district = District.objects.all()
        # tal = Taluk.objects.all()
        tal = Taluk.objects.filter(district)
        
        context = {
             'district': district ,
             'taluk':tal,
        }
        if request.method =='POST': 
           center_name = request.POST.get('center_name')
           date_avail1 = request.POST.get('date_avail1')
           date_avail2 = request.POST.get('date_avail2')

           center = Vaccine_center(district=district, taluk=taluk, center_name=center_name, date_avail1=date_avail1, date_avail2=date_avail2)      
           center.save()

           messages.success(request, 'Item Added Successfully!')
        return render(request,'vaccine_center.html', context) 


#=====================================================================

# def dis_list(request):
#      district = District.objects.all().values()
#      context = {
#              'district': district
#         }
#      return render(request,'dis_list.html',context) 

# def talu(request):
#    district = request.GET.get('taluk')
#    taluk=Taluk.objects.filter(distric=district)
#    context = {
#              'taluk':taluk
#         }
#    print(district)
#    messages.success(request, 'Item Added Successfully!')
#    return render(request,'talu.html',context)

# =====================================================
def vaccination(request):
    vacc = Vaccine.objects.all()
    us = User.objects.all().values()
    # aadhar = User.objects.filter(pk=aadhar)
    # name = User.objects.filter(name=name)
    if request.method =='POST':      
        aadhar = User.objects.filter(pk=aadhar)
        name = User.objects.filter(name=name) 
        
        vid = request.POST.get('vid')
        dose1 = request.POST.get('dose1')   
       
        user = Vaccination(aadhar=aadhar, name=name, vid=vid, dose1=dose1)
        user.save()

    return render(request, 'add_vaccination.html', {'Vaccine': vacc,'User':us}) 
    


# update
# def update_vaccination(request,aadhar):
#     vac = Vaccination.objects.get(pk=aadhar)
#     return render(request,'{}')



# def vaccination(request):
#     vacc = Vaccine.objects.all()
#     us = User.objects.all().values()

#     if request.method=='post':
#         aadhar =  request.POST.get('aadhar')
#         name =  request.POST.get('name')
#         vid = request.POST.get('vid')
#         dose1 = request.POST.get('dose1')   

#         user = Vaccination(aadhar=aadhar, name=name, vid=vid, dose1=dose1)
#         user.save()

#     return render(request,'add_vaccination.html', {'Vaccine': vacc,'User':us}) 



def view_vaccinated(request):
    v = Vaccination.objects.all().values()
    template = loader.get_template('view_vaccinated.html') 
    return render(request,'view_vaccinated.html', {'Vaccination':v})


# to update the user vaccination record
def update_vaccination(request):
    pass 


# to know about the user not vaccinated 
def not_vaccinated(requst):
    pass


#due vaccinated
def due_vaccinated(requst):
   v = Vaccination.objects.all()
   template = loader.get_template('due_vaccinated.html') 
   return render(request,'due_vaccinated.html', {'Vaccination':v})
   


# user_vaccine registration
def user_slot_booking(request):
    district = District.objects.all()
    # user=User.objects.all()
    context = {
            'district': district,
        }
    if request.method == 'post': 
        aadhar = request.POST.get('aadhar') 
        name = request.POST.get('name') 
        date = request.POST.get('date')

        user = User_vaccine_registration(aadhar=aadhar, name=name, did=did, date=date)
        user.save()


    return render(request,'user_slot_booking.html',context)     

def view_slot(request):
    us = User_vaccine_registration.objects.all().values()
    template = loader.get_template('view_slot.html') 
    return render(request,'view_slot.html', {'User_vaccine_registration':us})      

