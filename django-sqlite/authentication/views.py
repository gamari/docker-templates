from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render


def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect("dashboard")
            else:
                return redirect("user_dashboard")
        else:
            return HttpResponse("Invalid login credentials")
    else:
        return render(request, "pages/login.html")
