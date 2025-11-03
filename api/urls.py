
from django.urls import path
from .import views

urlpatterns = [
    path("register/",views.register,name="user_create"),
    path("user_login/",views.user_login,name="user_login"),
    path("get_user_details/",views.get_user_details,name="get_user_details"),
    path("user_update/<str:username>/",views.user_update,name="user_update"),
    path("user_delete/<str:email>/",views.user_delete,name="user_delete"),
    path("admin_login/",views.admin_login,name="admin_login"),
    path("employee_register/",views.employee_register,name="employee_register"),
    path("employee_login/",views.employee_login,name="employee_login")
 
]