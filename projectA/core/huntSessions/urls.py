from django.urls import path
from . import views


urlpatterns = [
    path(
        "staff/login/",
        views.staff_login,
        name="staff_login"
    ),

    path(
        "staff/logout/",
        views.staff_logout,
        name="staff_logout"
    ),

    path(
        "dashboard/admin/",
        views.admin_dashboard,
        name="admin_dashboard"
    ),

    path(
        "dashboard/staff/",
        views.staff_dashboard,
        name="staff_dashboard"
    ),
    path("dashboard/manage/hunts/",
    views.manage_hunts,
    name="manage_hunts"),

    path("dashboard/questions/",
    views.question_pool,
    name="question_pool"),
    
    path("dashboard/sessions/",
    views.manage_sessions,
    name="manage_sessions"),

    path("dashboard/manage/hunts/create/",
    views.create_hunt,
    name="create_hunt"),

    path("dashboard/questions/create/",
    views.create_question,
    name="create_question"),
]