from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


def staff_login(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect("admin_dashboard")

        if request.user.is_staff:
            return redirect("staff_dashboard")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None and user.is_staff:
            login(request, user)
            messages.success(request, "Login successful.")

            if user.is_superuser:
                return redirect("admin_dashboard")

            return redirect("staff_dashboard")

        messages.error(
            request,
            "Invalid username, password, or staff permission."
        )

    return render(request, "login/staff_login.html")


@login_required(login_url="staff_login")
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect("staff_dashboard")

    return render(request, "login/admin_welcome.html")


@login_required(login_url="staff_login")
def staff_dashboard(request):
    if not request.user.is_staff:
        return redirect("staff_login")

    if request.user.is_superuser:
        return redirect("admin_dashboard")

    return render(request, "login/staff_welcome.html")


def staff_logout(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "Logout successful.")

    return redirect("staff_login")