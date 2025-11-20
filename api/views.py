from django.shortcuts import render
from .serializers import userSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import user,admin_user,employee_user,scan_card,schedule_meeting,eventpost
from .serializers import schedule_meetingSerializer

# Create your views here.

@api_view(['POST'])
def register(request):
    data = request.data
    username = data.get("username")
    email = data.get("email")
    phone_number=data.get("phone_number")
    password = data.get("password")

    if not username or not email or not phone_number or not password:
        return Response({"msg":"please fill in all required fields"},status=404)
    
    create_user =user.objects.create(
        username= username,
        email=email,
        phone_number=phone_number,
        password=password


    )
    create_user.save()

    return Response({"msg":"user register successfully",
                     "username":username,
                     "email":email,
                     "phone_number":phone_number,
                     "password":password },status=200)


@api_view(['POST'])
def user_login(request):
    username =request.data.get("username")
    password =request.data.get("password")
    
    if not username or not password:
        return Response({"msg":"invalid credentials"},status=404)
    try:
        user_instance =user.objects.get(
            username=username,
            password=password
            )
    except user.DoesNotExist:
        return Response({"msg":"user not found or invalid credentails"},status=404)
    return Response({"msg":"user login successfully"},status=200)



@api_view(['GET'])
def get_user_details(request):
    user_detail = user.objects.all()
    if not user_detail:
        return Response({"msg":"user not found"},status=404)
    
    user_view =[]
    for use in user_detail:
        user_view.append({
            "username":use.username,
            "email":use.email,
            "phone_number":use.phone_number,
            "password":use.password

        })
        return Response(user_view)

@api_view(["PUT"])
def user_update(request,username):
    user_instace= user.objects.filter(username=username).first()
    if not user_instace:
        return Response({"user name is not found"},status=404)
    
    user_instace.username = request.data.get("username",user_instace)
    user_instace.email = request.data.get("email",user_instace.email)
    user_instace.phone_number = request.data.get("phone_number",user_instace.phone_number)
    user_instace.password = request.data.get("password",user_instace.password)

    user_instace.save()
    return Response({"msg":"user update successfully",
                     "username":user_instace.username,
                     "email":user_instace.email,
                     "phone_number":user_instace.phone_number,
                     "password":user_instace.password},status=200)

@api_view(["DELETE"])
def user_delete(request,email):
    user_del =user.objects.filter(email=email).delete()
    if not user_del:
        return Response({"msg":"user not found"},status=404)
    return Response({"msg":"user delete sucessfully"},status=200)
    
#adminuser#
@api_view(['POST'])
def admin_login(request):
    name = request.data.get("name")
    password = request.data.get("password")

    if not name or not password:
        return Response({"msg":"invalid credentails"},status=404)
    admin_instance =admin_user.objects.get(name=name,password=password)
    return Response({"msg":"admin login successfully"},status=200)
    

@api_view(['POST'])
def employee_register(request):
    data = request.data
    username = data.get("username")
    email = data.get("email")
    phone_number=data.get("phone_number")
    password = data.get("password")
    role_type =data.get("role_type")

    if not username or not email or not phone_number or not password:
        return Response({"msg":"please fill in all required fields"},status=404)
    if role_type == "employee":
        create_user =employee_user.objects.create(
        username= username,
        email=email,
        phone_number=phone_number,
        password=password
        )
    else:
        return Response({"msg":"role type is invalid"},status=400)

    return Response({"msg":"user register successfully",
                     "username":username,
                     "email":email,
                     "phone_number":phone_number,
                     "password":password ,
                     "role_type":role_type},status=200)

@api_view(["POST"])
def employee_login(request):
    data = request.data
    username = data.get("username")
    password = data.get("password")
    role_type =data.get("role_type")

    if not username or not password or not role_type:
        return Response({"msg":"invalid credentials"},status=404)
    try:
        if role_type == "employee":
            user_instance =employee_user.objects.get(
            username=username,
            password=password,
            role_type=role_type
            )
        else:
            return Response({"msg":"invalid role type"},status=400)
    except user.DoesNotExist:
        return Response({"msg":"employee not found or invalid credentails"},status=404)
    return Response({"msg":"employee login successfully"},status=200)


@api_view(['GET'])
def employee_details(request):
    emp_obj =employee_user.objects.all()
    if not emp_obj:
        return Response({"msg":"employee is not found"},status=404)
    
    get=[]
    for e in emp_obj:
        get.append({
            "username":e.username,
            "email":e.email,
            "phone_number":e.phone_number,
            "password":e.password,
            "role_type":e.role_type
        })

        return Response(get,status=200)

@api_view(["PUT"])
def employee_update(request,username):
    employee_instance= employee_user.objects.filter(username=username).first()
    if not employee_instance:
        return Response({"employee name is not found"},status=404)
    
    employee_instance.username = request.data.get("username",employee_instance.username)
    employee_instance.email = request.data.get("email",employee_instance.email)
    employee_instance.phone_number = request.data.get("phone_number",employee_instance.phone_number)
    employee_instance.password = request.data.get("password",employee_instance.password)

    employee_instance.save()
    return Response({"msg":"employee update successfully",
                     "username":employee_instance.username,
                     "email":employee_instance.email,
                     "phone_number":employee_instance.phone_number,
                     "password":employee_instance.password},status=200)


@api_view(["DELETE"])
def employee_delete(request,email):
    employee_del =employee_user.objects.filter(email=email).delete()
    if not employee_del:
        return Response({"msg":"employee not found"},status=404)
    return Response({"msg":"employee delete successfully"},status=200)



@api_view(['POST'])
def create_scan_card(request):
    name = request.data.get("name")
    company_name = request.data.get("company_name")
    email = request.data.get("email")
    address = request.data.get("address")
    phone_number = request.data.get("Phone_number")  
    office_number = request.data.get("office_number")
    company_website = request.data.get("company_website")

    # Create object
    create_scan = scan_card.objects.create(
        name=name,
        company_name=company_name,
        email=email,
        address=address,
        Phone_number=phone_number,
        office_number=office_number,
        company_website=company_website
    )

    return Response({
        "msg": "card created successfully",
        "data": {
            "name": name,
            "company_name": company_name,
            "email": email,
            "address": address,
            "Phone_number": phone_number,
            "office_number": office_number,
            "company_website": company_website
        }
    }, status=200)

    
@api_view(['GET'])
def get_scan_card(request):
    scan_obj = scan_card.objects.all()
    if not scan_obj:
        return Response({"msg":"scan_card not found"},status=404)
    
    list=[]
    for s in scan_obj:
        list.append({
            "name":s.name,
            "company_name":s.company_name,
            "email":s.email,
            "address":s.address,
            "phone_number":s.phone_number,
            "office_number":s.office_number
            
        })
        return Response({"msg":"view scan card detils successfully"},status=200)

@api_view(['PATCH'])
def scan_update(request,name):
    try:
        scan_instance =scan_card.objects.get(name=name)
    except scan_card.DoesNotExist:
        return Response({"msg":"name  not found"},status=404)
    
    scan_instance.name =request.data.get("name",scan_instance.name)
    scan_instance.company_name= request.data.get("company_name",scan_instance.company_name)
    scan_instance.email = request.data.get("email",scan_instance.email)
    scan_instance.address =request.data.get("address",scan_instance.address)
    scan_instance.Phone_number = request.data.get("Phone_number",scan_instance.Phone_number)
    scan_instance.office_number =request.data.get("office_number",scan_instance.office_number)
    scan_instance.company_website= request.data.get("company_website",scan_instance.company_website)

    return Response({"msg":"scan update successfully",
                     "name": scan_instance.name,
                     "company_name":scan_instance.company_name,
                     "email":scan_instance.email,
                     "address":scan_instance.address,
                     "Phone_number":scan_instance.Phone_number ,
                     "office_number":scan_instance.office_number,
                     "company_website":scan_instance.company_website},status=200)

    
@api_view(['DELETE'])
def scan_delete(request,name):
    try:
        scan_del =scan_card.objects.get(name=name)
        scan_del.delete()
        return Response({"msg":"scan card delete successfully"},status=200)
    except scan_card.DoesNotExist:
        return Response({"msg":"name not found"},status=404)

from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings


@csrf_exempt
@api_view(['POST'])
def schedule_meeting_create(request):
    card_name = request.data.get("card")
    name = request.data.get("name")
    mobile_no = request.data.get("mobile_no")
    email = request.data.get("email")
    purpose_of_meeting = request.data.get("purpose_of_meeting")
    meeting_type = request.data.get("meeting_type")
    Date = request.data.get("Date")
    Time = request.data.get("Time")
    meeting_link = request.data.get("meeting_link")

    try:
        card_instance = scan_card.objects.get(name=card_name)
    except scan_card.DoesNotExist:
        return Response({"msg": "card not found"}, status=404)


    create_schedule = schedule_meeting.objects.create(
        card=card_instance,
        name=name,
        mobile_no=mobile_no,
        email=email,
        purpose_of_meeting=purpose_of_meeting,
        meeting_type=meeting_type,
        Date=Date,
        Time=Time,
        meeting_link=meeting_link
    )


    accept_url = request.build_absolute_uri(
        reverse("accept_meeting", args=[create_schedule.id])
    )
    reject_url = request.build_absolute_uri(
        reverse("reject_meeting", args=[create_schedule.id])
    )

    
    subject = "New Meeting Request Received"
    message = f"""
    Hello {card_instance.name},

    you received a meeting request.

    name: {name}
    mobile: {mobile_no}
    email: {email}
    purpose: {purpose_of_meeting}
    date: {Date}
    time: {Time}


    Accept Meeting: {accept_url}
    Reject Meeting: {reject_url}
"""

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [card_instance.email],
        fail_silently=False
    )


    return Response({
        "msg": "Schedule meeting created successfully!",
        "meeting_id": create_schedule.id,
        "accept_url": accept_url,
        "reject_url": reject_url,
        "meeting_details": {
            "card": card_name,
            "name": name,
            "mobile_no": mobile_no,
            "email": email,
            "purpose_of_meeting": purpose_of_meeting,
            "meeting_type": meeting_type,
            "Date": Date,
            "Time": Time,
            "meeting_link": meeting_link
        }
    }, status=200)

@csrf_exempt
@api_view(['POST'])
def accept_meeting(request, create_schedule_id):
    try:
        meeting = schedule_meeting.objects.get(id=create_schedule_id)
    except schedule_meeting.DoesNotExist:
        return Response({"msg": "Meeting not found"}, status=404)

    meeting.is_accept = True
    meeting.is_reject = False
    meeting.is_closed = False
    meeting.save()

    subject = "Your Meeting Has Been Accepted"
    message = f"""
{meeting.name} has accepted your meeting.
Meeting link: {meeting.meeting_link}
"""
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL,
              [meeting.card.email], fail_silently=False)

    return Response({
        "msg": "Meeting accepted successfully!",
        "meeting_id": meeting.id,
        "accepted_by": meeting.name,
        "creator_notified": True
    }, status=200)


@csrf_exempt
@api_view(['POST'])
def reject_meeting(request, create_schedule_id):
    try:
        meeting = schedule_meeting.objects.get(id=create_schedule_id)
    except schedule_meeting.DoesNotExist:
        return Response({"msg": "Meeting not found"}, status=404)

    meeting.is_accept = False
    meeting.is_reject = True
    meeting.is_closed = True
    meeting.save()

    return Response({
        "msg": "Meeting rejected. Meeting is now closed.",
        "meeting_id": meeting.id,
        "status": "closed"
    }, status=200)


@api_view(['GET'])
def view_schedule_meeting(request):
    try:
        meeting_get =schedule_meeting.objects.all()
    except schedule_meeting.DoesNotExist:
        return Response({"msg":"meeting not found"},status=404)
    
    list =[]
    for meet in meeting_get:
        list.append({
            "card":meet.card.name,
            "name":meet.name,
            "mobile_no":meet.mobile_no,
            "email":meet.email,
            "purpose_of_meeting":meet.purpose_of_meeting,
            "meeting_type":meet.meeting_type,
            "Date":meet.Date,
            "Time":meet.Time,
            "meeting_link":meet.meeting_link

        })
        return Response(list,status=200)
    
@api_view(['GET'])
def meeting_accept_details(request):
    try:
        meeting_get =schedule_meeting.objects.all()
    except schedule_meeting.DoesNotExist:
        return Response({"msg":"meeting not found"},status=404)
    
    show =[]
    for s in meeting_get:
        show.append({
            "card_user":s.card.name,
            "is_accept":s.is_accept,
        })
        return Response(show,status=200)
    
@api_view(['GET'])
def meeting_reject_details(request):
    try:
        meeting_get =schedule_meeting.objects.all()
    except schedule_meeting.DoesNotExist:
        return Response({"msg":"meeting not found"},status=404)
    
    show =[]
    for s in meeting_get:
        show.append({
            "card_user":s.card.name,
            "is_reject":s.is_reject,
            "is_closed":s.is_closed
        })
        return Response(show,status=200)
    
@api_view(['PUT'])
def update_schedule_meeting(request,name):
    try:
        update_schedule = schedule_meeting.objects.get(name=name)
    except schedule_meeting.DoesNotExist:
        return Response({"msg":"schedule meeting not found"},status=404)
    card_name =request.data.get("card")
    try:
        update_card = scan_card.objects.get(name=card_name)
        update_schedule.card = update_card
    except scan_card.DoesNotExist:
        return Response({"msg":"card not found"},status=404)
    
    update_schedule.name = request.data.get("name",update_schedule.name)
    update_schedule.mobile_no=request.data.get("mobile_no",update_schedule.mobile_no)
    update_schedule.email= request.data.get("email",update_schedule.email)
    update_schedule.purpose_of_meeting=request.data.get("purpose_of_meeting",update_schedule.purpose_of_meeting)
    update_schedule.meeting_type= request.data.get("meeting_type",update_schedule.meeting_type)
    update_schedule.Date= request.data.get("Date",update_schedule.Date)
    update_schedule.Time=request.data.get("Time",update_schedule.Time)
    update_schedule.meeting_link =request.data.get("meeting_link",update_schedule.meeting_link)

    update_schedule.save()

    return Response({
        "msg":"schedule update successfully",
        "name":update_schedule.name,
        "mobile_no":update_schedule.mobile_no,
        "email":update_schedule.email,
        "purpose_of_meeting":update_schedule.purpose_of_meeting,
        "meeting_type":update_schedule.meeting_type,
        "Date": update_schedule.Date,
        "Time": update_schedule.Time,
        "meeting_link":update_schedule.meeting_link 
    },status=200)


@api_view(['DELETE'])
def delete_schedule_meeting(request,email):
    try:
        del_schedule =schedule_meeting.objects.get(email=email)
    except schedule_meeting.DoesNotExist:
        return Response({"msg":"schedule meeting not found"},status=404)
    del_schedule.delete()
    return Response({"msg":"meeting delete successfully"},status=200)


@api_view(['POST'])
def create_eventpost(request):
    user_name =request.data.get("User")
    caption =request.data.get("caption")
    media =request.FILES.get("media")
    location =request.data.get("location")

    try:
        user_instance =user.objects.get(username=user_name)
    except user.DoesNotExist:
        return Response({"msg":"user not found"},status=404)
    
    event_create =eventpost.objects.create(
        User =user_instance,
        caption=caption,
        media=media,
        location=location
    )
    event_create.save()

    return Response({"msg":"post creates successfulyl",
                     "post":event_create.id},status=200)


@api_view(['POST'])
def like_post(request,post_id):
    user_name =request.data.get("User")
    try:
        user_obj = user.objects.get(name=user_name)
        post = eventpost.objects.get(id=post_id)
    except:
        return Response({"user and post not found"},status=404)
    
    if user_obj in post.like_by.all():
        post.like_by.remove(user_obj)
        return Response({"msg":"unlike the post"},status=404)
    else:
        post.like_by.add(user_obj)
        return Response({"msg":"post liked"},status=200)
    
@api_view(['POST'])
def save_post(request,post_id):
    user_name = request.data.get("User")
    try:
        user_obj =user.objects.get(name=user_name)
        post =eventpost.objects.get(id=post_id)
    except:
        return Response({"user and post not found"},status=404)

    if user_obj in post.saved_by.all():
        post.saved_by.remove(user_obj)
        return Response({"msg":"unsaved post"},status=404) 
    else:
        post.saved_by.add(user_obj)
        return Response({"msg":"post save"},status=200)







    
  
    


