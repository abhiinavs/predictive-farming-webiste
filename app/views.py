import json
import smtplib
from datetime import datetime
from email.mime.text import MIMEText

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.sites import requests
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import requests

# Create your views here.
from pyexpat.errors import messages

from app.models import *
from app import predictioncnn
from app import read_csv




def loginpage(request):
    return render(request,"loginindex.html")

def logout(request):
    auth.logout(request)
    return render(request,"loginindex.html")



def loginpage_post(request):
    username=request.POST['textfield']
    pwrd=request.POST['textfield2']
    ob=login_table.objects.get(username=username,password=pwrd)
    if ob.type=='admin':
        ob1=auth.authenticate(username="admin",password="admin")
        if ob1 is not None:
            auth.login(request,ob1)
        request.session["lid"] = ob.id
        return HttpResponse('''<Script>
         alert("Login Successfull");window.location="/admin_admin_home"</Script>''')
    elif ob.type=='expert':
        ob1 = auth.authenticate(username="admin", password="admin")
        if ob1 is not None:
            auth.login(request, ob1)
        request.session['lid']=ob.id
        # ob=expert_table.objects.filter(LOGIN=ob.id)
        # if len(ob)>0:
        return HttpResponse('''<Script> 
             alert("Login Succesfull");window.location="/expert_manage_tips"</Script>"''')
    # else:
    #         return HttpResponse('''<Script>
    #                     alert("Invalid");window.location="/"</Script>"''')

    elif ob.type=='farmer':
        ob1 = auth.authenticate(username="admin", password="admin")
        if ob1 is not None:
            auth.login(request, ob1)
        request.session["lid"] = ob.id
        return HttpResponse('''<Script>
        alert("Login Succesfull");window.location="/farmer_farmer_home"</script>''')
    else :
        return HttpResponse('''<Script>
        alert("invalid username or password");window.location="/"''')


@login_required(login_url='/')

def admin_add_expert(request):
    return render(request,"admin/add expert.html")

@login_required(login_url='/')
def admin_add_expert_post(request):
    fname = request.POST['textfield']
    LastName=request.POST['textfield2']
    place=request.POST['textfield3']
    Qualification=request.POST['textfield4']
    Image=request.FILES['file']
    Phone=request.POST['textfield5']
    Email=request.POST['textfield6']
    Username=request.POST['textfield7']
    Password=request.POST['textfield8']

    fs=FileSystemStorage()
    date=datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+".jpg"
    fs.save(date,Image)
    path=fs.url(date)


    ob=login_table()
    ob.username=Username
    ob.password=Password
    ob.type="expert"
    ob.save()

    obb=expert_table()
    obb.FirstName=fname
    obb.LastName=LastName
    obb.LOGIN=ob
    ob.Place=place
    obb.qualification=Qualification
    obb.Phone=Phone
    obb.Email=Email
    obb.Image=path
    obb.save()

    return HttpResponse('''<Script>
         alert(" Successfull");window.location="/admin_manage_expert"</Script>''')

@login_required(login_url='/')
def admin_add_crop(request):
    a=crop_table.objects.all()


    return render(request,"admin/Add_crop.html",{'data':a})


@login_required(login_url='/')
def admin_add_crop_search(request):
    name=request.POST["textfield"]
    a=crop_table.objects.filter(name__contains=name)


    return render(request,"admin/Add_crop.html",{'data':a})



@login_required(login_url='/')
def delete_crop(request,id):
    a=crop_table.objects.get(id=id)
    a.delete()
    return HttpResponse('''<Script>
             alert(" Deleted");window.location="/admin_add_crop"</Script>''')

@login_required(login_url='/')
def admin_ADD_new_CROPS(request):
    return render(request,"admin/ADD_CROPS.html")

@login_required(login_url='/')
def admin_ADD_new_CROPS_post(request):
    productname = request.POST['textfield']
    price = request.POST['textfield2']
    stock = request.POST['textfield3']
    detail = request.POST['textfield4']

    a=crop_table()
    a.name=productname
    a.details=detail
    a.price=price
    a.stock=stock
    a.save()
    return HttpResponse('''<Script>
            alert(" Successfull");window.location="/admin_add_crop"</Script>''')



@login_required(login_url='/')
def admin_admin_home(request):
    return render(request,"admin/index.html")

@login_required(login_url='/')
def admin_manage_expert(request):
    a=expert_table.objects.all()
    return render(request,"admin/manage expert.html",{'data':a})


@login_required(login_url='/')
def MANAGENOTIFICATION(request):
    a=notification_table.objects.all()
    return render(request,"admin/MANAGE NOTIFICATION.html",{'data':a})

@login_required(login_url='/')
def delete_notification(request,id):
    a=notification_table.objects.get(id=id)
    a.delete()
    return HttpResponse('''<Script>
    alert(" Deleted");window.location="/MANAGENOTIFICATION" </Script>''')


@login_required(login_url='/')
def admin_add_notification(request):
    return render(request,"admin/ADD NOTIFICATION.html")

@login_required(login_url='/')
def admin_send_reply(request,id):
    request.session['id']=id
    return render(request,"admin/Admin_sendreplycom.html")

@login_required(login_url='/')
def admin_send_reply_post(request):
    textfield=request.POST['textfield']
     # a.FARMER = farmer_table.objects.get(LOGIN_id=request.session['lid'])
    a=complaint_table.objects.get(id=request.session['id'])
    a.reply=textfield
    a.save()
    return HttpResponse('''<Script>
        alert(" Replied Succesfully");window.location="/admin_compalint"</Script>''')



@login_required(login_url='/')
def admin_add_notification_post(request):
    notification = request.POST['textfield']
    a=notification_table()
    a.notification=notification
    a.date = datetime.today()
    a.time=datetime.now()
    a.save()
    return HttpResponse('''<script>
                alert("Notification Added Sucessfully");
                window.location="/MANAGENOTIFICATION";
                </script>''')

@login_required(login_url='/')
def admin_manage_expert_post(request):
    search=request.POST['textfield4']
    return render(request,"admin/manage expert.html")

@login_required(login_url='/')
def admin_manage_expert_search(request):
    name=request.POST["textfield4"]
    a=expert_table.objects.filter(FirstName__contains=name)
    return render(request, "admin/manage expert.html",{'data':a})


@login_required(login_url='/')
def approve_farmer(request, id):
    # Get the farmer object based on the LOGIN id
    farmer = login_table.objects.get(id=id)

    # Update the type field of the related LOGIN record
    farmer.type = 'farmer'

    # Save the updated LOGIN record
    farmer.save()

    # Return the response with a JavaScript alert and redirect
    return HttpResponse('''<script>
            alert("Approved");
            window.location="/admin_verify_farmer";
            </script>''')
@login_required(login_url='/')
def reject_farmer(request, id):
    # Get the farmer object based on the LOGIN id
    farmer = farmer_table.objects.get(LOGIN_id=id)

    # Update the type field of the related LOGIN record
    farmer.LOGIN.type = 'reject'

    # Save the updated LOGIN record
    farmer.LOGIN.save()

    # Return the response with a JavaScript alert and redirect
    return HttpResponse('''<script>
            alert("Approved");
            window.location="/admin_verify_farmer";
            </script>''')


@login_required(login_url='/')
def admin_verify_farmer(request):
    a=farmer_table.objects.all()
    return render(request,"admin/verify farmer.html",{'data':a})
@login_required(login_url='/')

def admin_verify_farmer_search(request):
    name=request.POST["textfield"]
    a=farmer_table.objects.filter(fname__contains=name)
    return render(request, "admin/verify farmer.html",{'data':a})

@login_required(login_url='/')
def approve_expert(request, id):
    # Get the farmer object based on the LOGIN id
    farmer = expert_table.objects.get(id=id)

    # Update the type field of the related LOGIN record
    farmer.LOGIN.type = 'expert'

    # Save the updated LOGIN record
    farmer.LOGIN.save()

    # Return the response with a JavaScript alert and redirect
    return HttpResponse('''<script>
            alert("Approved");
            window.location="/admin_manage_expert";
            </script>''')
@login_required(login_url='/')
def reject_expert(request, id):
    # Get the farmer object based on the LOGIN id
    farmer = expert_table.objects.get(id=id)

    # Update the type field of the related LOGIN record
    farmer.LOGIN.type = 'reject'

    # Save the updated LOGIN record
    farmer.LOGIN.save()

    # Return the response with a JavaScript alert and redirect
    return HttpResponse('''<script>
            alert("Rejected");
            window.location="/admin_manage_expert";
            </script>''')







@login_required(login_url='/')
def admin_view_user(request):
    a=user_table.objects.all()
    return render(request,"admin/view_user.html",{'data':a})


@login_required(login_url='/')
def expert_add_fertilizer(request):
    return render(request,"Expert/Add fertilizer.html")

@login_required(login_url='/')
def expert_add_fertilizer_post(request):
    name=request.POST['textfield']
    image=request.FILES['file']
    details=request.POST['textarea']
    # price=request.POST['textfield2']
    fs = FileSystemStorage()
    date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".jpg"
    fn=fs.save(date, image)

    ob = fertilizer_table()
    ob.name =name
    ob.image = fn
    ob.details = details
    # ob.price = price
    ob.save()

    return HttpResponse('''<Script>
    alert(" Successfully Added");window.location="/expert_manage_fertilizer"</Script>''')
    # return render(request,"Expert/Add fertilizer.html")


@login_required(login_url='/')
def delete_fertilizer(request,id):
    a=fertilizer_table.objects.get(id=id)
    a.delete()
    return HttpResponse('''<Script>
             alert(" Deleted");window.location="/expert_manage_fertilizer"</Script>''')

@login_required(login_url='/')
def expert_edit_fertilizer(request,id):
    request.session["fid"]=id
    obb = fertilizer_table.objects.get(id=id)
    return render(request, 'Expert/Edit_fertilizer.html',{"data":obb})

@login_required(login_url='/')
def expert_edit_fertilizer_post(request):
    name=request.POST['textfield']

    details=request.POST['textarea']
    # price=request.POST['textfield2']


    if 'file' in request.FILES:
        image = request.FILES['file']
        fs = FileSystemStorage()
        date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".jpg"
        fn=fs.save(date, image)

        ob = fertilizer_table.objects.get(id=request.session["fid"])
        ob.name =name
        ob.image = fn
        ob.details = details
        # ob.price = price
        ob.save()
    else:
        ob = fertilizer_table.objects.get(id=request.session["fid"])
        ob.name = name
        ob.details = details
        # ob.price = price
        ob.save()

    return HttpResponse('''<Script>
    alert(" Successfull");window.location="/expert_manage_fertilizer"</Script>''')



@login_required(login_url='/')
def expert_manage_tips(request):
    return render(request, "Expert/expert index.html")

@login_required(login_url='/')
def view_tips(request):
    ob=tips_table.objects.filter(EXPERT_ID__LOGIN_id=request.session['lid'])
    return render(request,"Expert/Tips.html",{'tips':ob})

@login_required(login_url='/')
def expert_add_tips(request):
    return render(request,"Expert/Add tips.html")

@login_required(login_url='/')
def expert_add_tips_post(request):
    tips=request.POST['textfield']
    Details=request.POST['textfield2']
    obb =tips_table()
    obb.EXPERT_ID=expert_table.objects.get(LOGIN__id=request.session['lid'])
    obb.Details=Details
    obb.tips=tips
    obb.save()
    return HttpResponse('''<Script>
            alert(" Successfull");window.location="/expert_tips"</Script>'''
    )



@login_required(login_url='/')
def expert_delete_tips(request,id):
    obb = tips_table.objects.get(id=id)
    obb.delete()
    return HttpResponse('''<Script>
            alert(" Deleted ");window.location="/expert_tips"</Script>''')


@login_required(login_url='/')
def expert_doubt(request):
    c = doubt_table.objects.all()
    # print(request.session["lid"])
    return render(request,"Expert/doubt.html",{'data':c})


@login_required(login_url='/')
def admin_compalint(request):
    c = complaint_table.objects.all()
    # print(request.session["lid"])
    return render(request,"admin/admin_complaint.html",{'data':c})

@login_required(login_url='/')
def expert_manage_fertilizer(request):
    ob=fertilizer_table.objects.all()
    return render (request,"Expert/manage_fertilizer.html",{"val":ob})


@login_required(login_url='/')
def farmer_view_fertilizer(request):
    ob=fertilizer_table.objects.all()
    return render (request,"Farmer/view_fertilizer.html",{"val":ob})

@login_required(login_url='/')
def expert_manage_soil(request):
    ob=soil_table.objects.all()
    return render(request,"Expert/Manage_soil.html",{"val":ob})

@login_required(login_url='/')
def farmer_view_soil(request):
    ob=soil_table.objects.all()
    return render(request,"Farmer/view_soil.html",{"val":ob})

@login_required(login_url='/')
def expert_add_soil(request):
    return render(request,"Expert/Add_Soil.html")

@login_required(login_url='/')
def expert_add_soil_post(request):
     soil_type= request.POST['textfield']
     details = request.POST['textfield2']
     obb = soil_table()
     obb.EXPERT_ID = expert_table.objects.get(LOGIN__id=request.session['lid'])
     obb.soil_type=soil_type
     obb.details = details
     obb.save()
     return HttpResponse('''<Script>
     alert(" Successfull");window.location="/expert_manage_soil"</Script>''')

@login_required(login_url='/')
def expert_edit_soil(request,id):
    request.session["fid"]=id
    obb = soil_table.objects.get(id=id)
    return render(request, 'Expert/Edit_soil.html',{"data":obb})

@login_required(login_url='/')
def expert_edit_soil_post(request):
    soil_type=request.POST['textfield']
    details=request.POST['textfield2']

    ob = soil_table.objects.get(id=request.session["fid"])
    ob.soil_type =soil_type
    ob.details = details
    ob.save()

    return HttpResponse('''<Script>
    alert(" Successfull");window.location="/expert_manage_soil"</Script>''')

@login_required(login_url='/')
def delete_soil(request,id):
    a=soil_table.objects.get(id=id)
    a.delete()
    return HttpResponse('''<Script>
             alert(" Deleted");window.location="/expert_manage_soil"</Script>''')



@login_required(login_url='/')
def expert_notification(request):
    a=notification_table.objects.all()
    return render(request,"Expert/notifictaion.html",{'data':a})

@login_required(login_url='/')
def farmer_notification(request):
    a=notification_table.objects.all()
    return render(request,"Farmer/view notification.html",{'data':a})

@login_required(login_url='/')
def expert_send_reply(request,id):
    request.session['ddid']=id
    return render(request,"Expert/send_rply.html")


@login_required(login_url='/')
def expert_send_reply_post(request):
    textfield=request.POST['textfield']
     # a.FARMER = farmer_table.objects.get(LOGIN_id=request.session['lid'])
    a=doubt_table.objects.get(id=request.session['ddid'])
    a.reply=textfield
    a.save()
    return HttpResponse('''<Script>
        alert(" Replied Succesfully");window.location="/expert_doubt"</Script>''')

@login_required(login_url='/')
def sendfeedback(request):
    ob = feedback_table.objects.filter(USER_ID__id=request.session['lid']).order_by('-id')
    return render(request, "Farmer/Sentfeedback.html",{"val":ob})

@login_required(login_url='/')
def sendfeedback_post(request):
    feedback = request.POST['feed']
    rating= request.POST['rating']


    ob = feedback_table()
    ob.feedback=feedback
    ob.rating=rating
    ob.USER_ID=login_table.objects.get(id=request.session["lid"])
    ob.date=datetime.now().date()
    ob.save()
    return HttpResponse('''<script>alert('feedback sent sucessfully');window.location='/sendfeedback'</script>''')

@login_required(login_url='/')
def feedback(request):
    ob = feedback_table.objects.all().order_by('-id')
    return render(request,"admin/view feedback.html",{"val":ob})



@login_required(login_url='/')
def expert_tips(request):
    tips = tips_table.objects.filter(EXPERT_ID__LOGIN_id=request.session['lid'])
    return render(request,"Expert/Tips.html",{'tips':tips})


@login_required(login_url='/')
def farmer_add_product(request):
    return render(request,"Farmer/Add Product.html")

@login_required(login_url='/')
def farmer_add_product_post(request):
    name = request.POST['textfield']
    image = request.FILES['file']
    stock = request.POST['textfield2']
    price = request.POST['textfield3']
    details = request.POST['textfield4']
    fs = FileSystemStorage()
    fn = fs.save(image.name,image)
    ob = product_table()
    ob.name = name
    ob.image = fn
    ob.stock = stock
    ob.price = price
    ob.details = details
    ob.FARMER = farmer_table.objects.get(LOGIN__id=request.session['lid'])
    ob.save()
    return HttpResponse('''<Script>
     alert(" Successfull");window.location="/farmer_manage_product"</Script>''')

@login_required(login_url='/')
def Farmer_notification(request):
    a=notification_table.objects.all()
    return render(request,"Farmer/view notification.html",{'data':a})


@login_required(login_url='/')
def delete_product(request,id):
    a=product_table.objects.get(id=id)
    a.delete()
    return HttpResponse('''<Script>
             alert(" Deleted");window.location="/farmer_manage_product"</Script>''')

@login_required(login_url='/')
def farmer_edit_product(request,id):
    request.session["fid"]=id
    obb = product_table.objects.get(id=id)
    return render(request,'Farmer/Farmer_edit_product.html',{"data":obb})

@login_required(login_url='/')
def farmer_edit_product_post(request):
    name=request.POST['textfield']
    stock=request.POST['textfield2']
    price=request.POST['textfield3']
    details=request.POST['textfield4']
    if 'file' in request.FILES:
        image = request.FILES['file']
        fs = FileSystemStorage()
        date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".jpg"
        fn=fs.save(date, image)

        ob = product_table.objects.get(id=request.session["fid"])
        ob.name =name
        ob.stock =stock
        ob.stock =stock
        ob.image = fn
        ob.details = details
        ob.price = price
        ob.save()
    else:
        ob = product_table.objects.get(id=request.session["fid"])
        ob.name = name
        ob.details = details
        ob.price = price
        ob.save()

    return HttpResponse('''<Script>
    alert(" Successfull");window.location="/farmer_manage_product"</Script>''')


@login_required(login_url='/')
def farmer_add_crop(request):
    return render(request,"Farmer/Add_crop.html")

@login_required(login_url='/')
def leaf_prediction(request):
    return render(request,"Farmer/leaf_prediction.html",{"res":"Choose image"})





@login_required(login_url='/')
def leaf_prediction_post(request):
    image = request.FILES['file']
    fs = FileSystemStorage()
    fs.save(image.name, image)

    path='C:\\Users\\sidha\\OneDrive\\Desktop\\predictive_farming (2)\\predictive_farming\\media\\'+image.name

    print(path)
    res=predictioncnn.predict(path)

    return render(request, "Farmer/leaf_prediction.html",{"res":res})

@login_required(login_url='/')
def crop_prediction(request):
    return render(request, "Farmer/Crop_prediction.html")

@login_required(login_url='/')
def crop_prediction_post(request):

    print(request.POST)
    Nitrogen = request.POST['textfield']
    Phosphorus = request.POST['textfield2']
    Pottasium = request.POST['textfield3']
    Temparature = request.POST['textfield4']
    Humidty = request.POST['textfield5']
    PH = request.POST['textfield6']
    Rainfall = request.POST['textfield7']

    res=read_csv.random_forest(float(Nitrogen),
                               float(Phosphorus),
                               float(Pottasium),
                               float(Temparature),
                               float(Humidty),float(PH)
                               ,float(Rainfall))

    return render(request, "Farmer/Crop_prediction.html", {"res": res})




    # return HttpResponse('''<Script>
    #            alert(" Successfull");window.location="/crop_prediction"</Script>''')

@login_required(login_url='/')
def farmer_ask_doubt(request):
    a=doubt_table.objects.all()
    return render(request,"Farmer/Ask doubt.html",{'data':a})

@login_required(login_url='/')
def farmer_ask_doubt_post(request):

    # expert=request.POST['name']
    doubt=request.POST['textfield']

    a=doubt_table()
    # a.FARMER=farmer_table.objects.get(LOGIN_id=request.session['lid'])
    # a.EXPERT=expert_table.objects.get(id=expert)
    a.doubt=doubt
    a.date=datetime.now().date().today()
    a.reply='pending'
    a.save()

    return HttpResponse('''<Script>
       alert(" Successfull");window.location="/farmer_send_doubt_and_snd_reply"</Script>''')

    # return redirect('/farmer_ask_doubt_post')
@login_required(login_url='/')

def farmer_farmer_home(request):
    return render(request, "Farmer/farmer index.html")

@login_required(login_url='/')
def farmer_farmer_register(request):
    return render(request,"Farmer/farmer register.html")


@login_required(login_url='/')
def farmer_farmer_register_post(request):
    fname=request.POST['firstname']
    lname=request.POST['lastname']
    place=request.POST['place']
    post=request.POST['post']
    pin=request.POST['pin']
    images=request.FILES['file']
    fs=FileSystemStorage()
    date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".jpg"
    fn=fs.save(date,images)
    phone=request.POST['phone']
    email=request.POST['email']
    uname=request.POST['username']
    pwrd=request.POST['password']
    ob = login_table()
    ob.username = uname
    ob.password = pwrd
    ob.type = "farmer"
    ob.save()

    obb = farmer_table()
    obb.LOGIN = ob
    obb.fname = fname
    obb.lname = lname
    obb.place = place
    obb.post = post
    obb.pin = pin
    obb.email=email
    obb.phone=phone
    obb.images = fn
    obb.save()
    return HttpResponse('''<Script>
       alert(" Registration Sucessfull");window.location="/"</Script>''')



@login_required(login_url='/')
def farmer_manage_product(request):
    ob=product_table.objects.filter(FARMER__LOGIN__id=request.session['lid'])
    return render(request,"Farmer/manage product.html",{"val":ob})

@login_required(login_url='/')
def farmer_manage_product_search(request):
    name = request.POST["textfield"]
    a = product_table.objects.filter(name__contains=name)
    return render(request, "Farmer/manage product.html", {'data': a})

@login_required(login_url='/')
def farmer_send_doubt_and_snd_reply(request):
    a=doubt_table.objects.all()
    return render(request,"Farmer/Send doubt & view reply.html",{'val':a},)
@login_required(login_url='/')
def farmer_doubt_search(request):
    date=request.POST["textfield"]
    a=doubt_table.objects.filter(date__exact=date)
    return render(request,"Farmer/Send doubt & view reply.html",{'val':a})


@login_required(login_url='/')
def farmer_send_doubt_post(request):
    doubt = request.POST['textfield']
    a = doubt_table()
    a.doubt = doubt
    a.FARMER = farmer_table.objects.get(LOGIN_id=request.session['lid'])
    a.reply = "pending"
    a.date = datetime.today()
    a.save()
    return HttpResponse('''<Script>
       alert(" Successfull");window.location="farmer_send_doubt_and_snd_reply"</Script>''')







@login_required(login_url='/')
def farmer_complaint(request):
    ob=complaint_table.objects.all()
    return render(request,"Farmer/complaint.html",{"val":ob})

@login_required(login_url='/')
def farmer_send_complaints(request):
    return render(request,"Farmer/send_complaints.html")

@login_required(login_url='/')
def farmer_send_complaint(request):
    return render(request,"Farmer/send_complaint.html")

@login_required(login_url='/')
def farmer_send_compaliant_post(request):
    complaint = request.POST['textfield']
    a=complaint_table()
    a.complaint=complaint
    a.user_id=login_table.objects.get(id=request.session['lid'])
    a.reply="pending"
    a.date=datetime.today()
    a.save()
    return HttpResponse('''<Script>alert(" Successfull");window.location="/farmer_complaint"</Script>''')


@login_required(login_url='/')

def farmer_complaint_search(request):
    date=request.POST["date"]
    a=complaint_table.objects.filter(date__exact=date)
    return render(request,"Farmer/complaint.html",{'val':a})

# def farmer_view_notification(request):
#     a = notification_table.objects.all()
#     return render(request,"Farmer/view notification.html",{'data':a})

@login_required(login_url='/')
def farmer_view_order_more(request,id):
    kk=order_details.objects.filter(ORDER__id=id)
    d=[]
    for i in kk:
       bb=int(i.PRODUCT.price)*int(i.quantity)
       row={'tot':bb}
       d.append(row)

    print(d,"cds")
    return render(request,"Farmer/view order more.html",{"kk":kk,"tot":d,"amt":bb})

@login_required(login_url='/')
def approve_order(request,id):

    order = order_product.objects.get(id=id)

    order.status = 'approved'
    order.save()
    return HttpResponse('''<script>alert("Approved");window.location="/farmer_view_order";</script>''')

@login_required(login_url='/')
def reject_order(request, id):
    order = order_product.objects.get(id=id)

    order.status = 'reject'
    order.save()
    return HttpResponse('''<script>
               alert("Rejected");
               window.location="/farmer_view_order";
               </script>''')

@login_required(login_url='/')
def farmer_view_order(request):
    ob = order_details.objects.all()
    r = []
    for i in ob:
        r.append(i.ORDER.id)
    kk = order_product.objects.filter(id__in=r)
    return render(request,"Farmer/view order.html",{"val":kk})

@login_required(login_url='/')
def farmer_view_tips(request):
    tips = tips_table.objects.all()
    return render(request,"Farmer/view tips.html",{'tips':tips})

@login_required(login_url='/')
def frget(request):
    return render(request,"forgotpage.html")

@login_required(login_url='/')
def forgot_password(request):
    print(request.POST)
    try:
        print("1")
        print(request.POST)
        email = request.POST['textfield']
        print(email)
        s=farmer_table.objects.filter(Email=email)
        if len(s)>0:
            s=s[0]
        else:
            s=expert_table.objects.filter(Email=email)
            if len(s)>0:
                s=s[0]
            else:
                return HttpResponse('''<script>alert('invalid email');window.location='/frget'</script>''')

        # qry = "SELECT login.password FROM student  JOIN login ON login.L_id = student.L_id WHERE email=%s"
        # s = selectone(qry, email)
        print(s, "=============")
        if s is None:
            return HttpResponse('''<script>alert('invalid email');window.location='/frget'</script>''')

            # return jsonify({'task': 'invalid email'})
        else:
            try:
                gmail = smtplib.SMTP('smtp.gmail.com', 587)
                gmail.ehlo()
                gmail.starttls()
                gmail.login('sidharthramachandran27@gmail.com', 'djpt xalj uvav mqtm')
                print("login=======")
            except Exception as e:
                print("Couldn't setup email!!" + str(e))
            msg = MIMEText("Your new password id : " + str(s.LOGIN.password))
            print(msg)
            msg['Subject'] = 'Predictive Farming'
            msg['To'] = email
            msg['From'] = 'Predictive farming team'

            print("ok====")

            try:
                gmail.send_message(msg)
            except Exception as e:
                return HttpResponse('''<script>alert('invalid email');window.location='/frget'</script>''')
            return HttpResponse('''<script>alert('sended');window.location='/'</script>''')
    except Exception as e:
        print(e)
        return HttpResponse('''<script>alert('invalid email');window.location='/frget'</script>''')

# user

def logincode(request):
    print(request.POST)
    un = request.POST['username']
    pwd = request.POST['password']
    print(un, pwd)
    try:
        ob = login_table.objects.get(username=un, password=pwd)

        if ob is None:
            data = {"task": "invalid"}
        else:
            print("in user function")
            data = {"task": "valid", "lid": str(ob.id),"type":str(ob.type)}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)
    except:
        data = {"task": "invalid"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)



def viewreply(request):
    lid=request.POST['id']
    ob=complaint_table.objects.filter(user_id__id=lid)
    print(ob,"HHHHHHHHHHHHHHH")
    mdata=[]
    for i in ob:
        data={'date':str(i.date),'complaint':i.complaint ,'reply':i.reply, 'id':i.id}
        mdata.append(data)
        print(mdata)
    return JsonResponse({"status":"ok","data":mdata})



def AppComplaint(request):
    print(request.POST)
    print(request.POST,"hhhhhhhhhhhhhhhhhhhhh")
    lid = request.POST['id']
    complaint = request.POST['complaint']

    lob = complaint_table()
    lob.user_id=login_table.objects.get(id=lid)
    lob.complaint = complaint
    lob.reply = 'pending'
    lob.date = datetime.today()
    lob.save()
    return JsonResponse({'task':'ok'})







def viewnotification(request):
    ob=notification_table.objects.all()
    print(ob,"HHHHHHHHHHHHHHH")
    mdata=[]
    for i in ob:
        data={'notification':i.notification,'time':str(i.time),'date':str(i.date),'id':i.id}
        mdata.append(data)
        print(mdata)
    return JsonResponse({"status":"ok","data":mdata})



def viewproduct(request):
    ob=product_table.objects.all()

    print(ob,"HHHHHHHHHHHHHHH")
    mdata=[]
    for i in ob:
        data={'FARMER':i.FARMER.fname+i.FARMER.lname,"name":i.name,'image':request.build_absolute_uri(i.image.url),'stock':i.stock,'price':i.price,'details':i.details,'id':i.id}
        mdata.append(data)
        print(mdata)
    return JsonResponse({"status":"ok","data":mdata})


def viewproductmore(request):
    pid=request.POST['pid']
    ob=product_table.objects.filter(id=pid)

    print(ob,"HHHHHHHHHHHHHHH")
    mdata=[]
    for i in ob:
        data={'FARMER':i.FARMER.fname+i.FARMER.lname,"name":i.name,'image':request.build_absolute_uri(i.image.url),'stock':i.stock,'price':i.price,'details':i.details,'id':i.id}
        mdata.append(data)
        print(mdata)
    return JsonResponse({"status":"ok","data":mdata})







def Androidregistration(request):
    print(request.FILES,"lllllllllllllllll")
    name = request.POST['textfield']
    lname = request.POST['lname']
    place = request.POST['textfield2']
    pin = request.POST['textfield3']
    post = request.POST['textfield4']
    email = request.POST['textfield5']
    phone = request.POST['textfield7']
    username = request.POST['textfield8']
    password = request.POST['textfield9']

    image = request.FILES['file']
    fs = FileSystemStorage()
    fp = fs.save(image.name, image)

    log = login_table()
    log.username = username
    log.password = password
    log.type = 'user'
    log.save()

    u_obj = user_table()
    u_obj.FirstName = name
    u_obj.LastName = lname
    u_obj.Place = place
    u_obj.Pin = pin
    u_obj.Post = post
    u_obj.Email = email
    u_obj.Phone = phone
    u_obj.Image = fp
    u_obj.LOGIN = log
    u_obj.save()
    print("okkk", u_obj)
    return JsonResponse({'status':'ok'})




def orderscode(request):
    print(request.POST, "=================================")
    pro_id = request.POST['pid']
    qty = request.POST['qty']
    lid = request.POST['lid']
    print(pro_id, "PPPPPPPPPPPPPPPPPPPPPPP")
    print(qty, "qqqqqqqqqqqqqqqqqqqqqqq")
    print(lid, "lllllllllllllllllllllllll")
    ob = product_table.objects.get(id=pro_id)
    tt = float(ob.price) * int(qty)
    stock = ob.stock
    print(stock, "SSSSSSSSSSSSSSSSSSSSSSSSS")
    nstk = int(stock) - int(qty)
    print(nstk, "OOOOOOOOOOOOOOOOOOOO")
    if int(stock)>= int(qty):
        up = product_table.objects.get(id=pro_id)
        up.stock = nstk
        up.save()
        ob = order_product()
        ob.status = 'ORDER'
        ob.date = datetime.now()
        ob.user_id = user_table.objects.get(LOGIN__id=lid)
        ob.total_amount = tt
        ob.save()
        obj = order_details()
        obj.ORDER = ob
        obj.PRODUCT=product_table.objects.get(id=pro_id)
        obj.quantity = qty
        obj.save()
        id = ob.id
        data = {"task": "valid", "oid": id,"price":int(tt)}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)
    else:
        data = {"task": "out of stock"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)




def add_to_cart(request):
    print(request.POST, "hhhhhhhhhhhh")
    qty = request.POST['quantity']
    pid = request.POST['pro_id']
    lid = request.POST['lid']
    qq = product_table.objects.get(id=pid)
    tt = int(qq.price) * int(qty)
    stock = int(qq.stock)
    print(stock, qty, "jjjjjjjjjjjjjjjjjjjjjj")
    nstk = int(stock) - int(qty)
    if stock >= int(qty):
        up = product_table.objects.get(id=pid)
        up.stock = nstk
        up.save()
        q = product_table.objects.filter(USER=user.objects.get(LOGIN__id=lid), status='OFFCART')
        if len(q) == 0:
            qt = order_details()
            qt.date = datetime.today()
            qt.USER = user_table.objects.get(LOGIN=lid)
            qt.status = 'OFFCART'
            qt.amount = tt
            qt.ordertype = 'online'
            qt.save()
            qty1 = order_product()
            qty1.quantity = qty
            qty1.PRODUCT = order_product.objects.get(id=pid)
            qty1.ORDER = qt
            qty1.date = datetime.today()
            qty1.save()
            data = {"task": "valid"}
            r = json.dumps(data)
            print(r)
            return HttpResponse(r)
        else:
            total = int(q[0].amount) + int(tt)
            qt = order_product.objects.get(id=q[0].id)
            qt.amount = total
            qt.save()
            qty1 = order_product.objects.filter(PRODUCT_id=pid, ORDER_id=q[0].id)
            if len(qty1) == 0:
                qqt =order_product()
                qqt.ORDER = q[0]
                qqt.PRODUCT = order_product.objects.get(id=pid)
                qqt.quantity = qty
                qqt.save()
            else:
                qry1 = order_product.objects.get(id=qty1[0].id)
                quty = int(qty1[0].quantity) + int(qty)
                qry1.quantity = quty
                qry1.save()
                data = {"task": "valid"}
                r = json.dumps(data)
                print(r)
                return HttpResponse(r)
    else:
        data = {"task": "out"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)
    data = {"task": "invalid"}
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)

def viewprofile(request):
    lid=request.POST['lid']
    user = user_table.objects.get(LOGIN=lid)
    profile = {
        'id':user.id,
        'firstname':user.FirstName+user.LastName,
        'place':user.Place,
        'post':user.Post,
        'phone':user.Phone,
        'email':user.Email,
        'photo':user.Image.url,
    }
    return JsonResponse({'status':'ok','profile':[profile]})

def user_edit_profile(request):
    id = request.POST['id']
    FirstName = request.POST['firstname']
    Lastname = request.POST['lastname']
    phone = request.POST['phone']
    Placename = request.POST['place']
    email = request.POST['email']
    post = request.POST['post']

    user = user_table.objects.get(LOGIN=id)

    if 'photo' in request.FILES:
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        fp = fs.save(photo.name,photo)
        user.Image = fp
        user.save()

    user.FirstName = FirstName
    user.LastName = Lastname
    user.Email = email
    user.phone = phone
    user.Place = Placename
    user.Post = post
    user.Phone = phone
    user.save()
    return JsonResponse({'status':'ok'})

def userpayment(request):
    oid=request.POST['oid']
    ob=order_product.objects.get(id=oid)
    ob.status='paid'
    ob.save()
    kk=order_details.objects.filter(ORDER__id=oid)
    for i in kk:
        i.status='paid'
        i.save()
    return JsonResponse({'status': 'ok'})
def DeleteMyComplaint(request):
    print(request.POST)
    oid=request.POST['complaint_id']
    ob=complaint_table.objects.get(id=oid)

    ob.delete()

    return JsonResponse({'status': 'ok'})

# def weather (request):
#     return render(requests,'Farmer/weather.html')
#
#
# def home(request):
#     if 'city' in request.POST:
#         city = request.POST['city']
#     else:
#         city = 'indore'
#
#     url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid='
#     PARAMS = {'units': 'metric'}
#
#     API_KEY = 'fb280b72baf43ec729a52c539015d9c8'
#
#     SEARCH_ENGINE_ID = 'AIzaSyDAf_8J-w_Wo5BXMsbUbEFMiKjbSdzG1Cc'
#
#     query = city + " 1920x1080"
#     page = 1
#     start = (page - 1) * 10 + 1
#     searchType = 'image'
#     city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"
#
#     data = requests.get(city_url).json()
#     count = 1
#     search_items = data.get("items")
#     image_url = search_items[1]['link']
#
#     try:
#
#         data = requests.get(url, params=PARAMS).json()
#         description = data['weather'][0]['description']
#         icon = data['weather'][0]['icon']
#         temp = data['main']['temp']
#         day = datetime.date.today()
#
#         return render(request, 'Farmer/weather.html',
#                       {'description': description, 'icon': icon, 'temp': temp, 'day': day, 'city': city,
#                        'exception_occurred': False, 'image_url': image_url})
#
#     except KeyError:
#         exception_occurred = True
#         messages.error(request, 'Entered data is not available to API')
#         # city = 'indore'
#         # data = requests.get(url,params=PARAMS).json()
#
#         # description = data['weather'][0]['description']
#         # icon = data['weather'][0]['icon']
#         # temp = data['main']['temp']
#         day = datetime.date.today()
#
#         return render(request, 'Farmer/weather.html',
#                       {'description': 'clear sky', 'icon': '01d', 'temp': 25, 'day': day, 'city': 'indore',
#                        'exception_occurred': exception_occurred})



