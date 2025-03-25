from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Subscriber

def subscribe_newsletter(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")

        if name and email:
            if not Subscriber.objects.filter(email=email).exists():
                Subscriber.objects.create(name=name, email=email)
                return JsonResponse({"success": True, "message": "Successfully subscribed!"})
            else:
                return JsonResponse({"success": False, "message": "This email is already subscribed!"})

    return JsonResponse({"success": False, "message": "Invalid request!"})
