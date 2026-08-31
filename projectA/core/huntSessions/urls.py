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
]