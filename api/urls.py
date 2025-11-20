
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
    path("employee_login/",views.employee_login,name="employee_login"),
    path("employee_details/",views.employee_details,name="employee_details"),
    path("employee_update/<str:username>/",views.employee_update,name="employee_update"),
    path("employee_delete/<str:username>/",views.employee_delete,name="employee_delete"),
    path("create_scan_card/",views.create_scan_card,name="create_scan_card"),
    path("get_scan_card/",views.get_scan_card,name="get_scan_card"),
    path("scan_update/<str:name>/",views.scan_update,name="scan_update"),
    path("scan_delete/<str:name>/",views.scan_delete,name="scan_delete"),
    path("schedule_meeting_create/",views.schedule_meeting_create,name="schedule_meeting_create"),
    path("accept_meeting/<int:create_schedule_id>/", views.accept_meeting, name="accept_meeting"),
    path("reject_meeting/<int:create_schedule_id>/", views.reject_meeting, name="reject_meeting"),
    path("view_schedule_meeting/",views.view_schedule_meeting,name="view_schedule_meeting"),
    path("meeting_accept_details/",views.meeting_accept_details,name="meeting_accept_details"),
    path("meeting_reject_details/",views.meeting_reject_details,name="meeting_reject_details"),
    path("update_schedule_meeting/<str:name>/",views.update_schedule_meeting,name="update_schedule_meeting"),
    path("delete_schedule_meeting/<str:email>/",views.delete_schedule_meeting,name="delete_schedule_meeting"),
    path("create_eventpost/",views.create_eventpost,name="create_eventpost")

 
]