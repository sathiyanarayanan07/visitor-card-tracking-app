from django.shortcuts import render
from .serializers import userSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import user,admin_user,employee_user

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


