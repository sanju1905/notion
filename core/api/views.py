# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .models import Students
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.hashers import check_password, make_password

@csrf_exempt
def Create_User(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = data.get('user', '')
        password = data.get('password', '')

        # Use Django's User model for creating users with hashed passwords
        hashed_password = make_password(password)

        # Check if the user already exists
        existing_user = Students.objects.filter(user=user)
        if existing_user.exists():
            return JsonResponse({'message': 'User already created. Try with a different name!'})
        else:
            new_user = Students.objects.create(user=user, password=hashed_password)
            new_user.save()
            return JsonResponse({'message': 'User created successfully!'})

    return JsonResponse({'message': 'Invalid request method.'})
# Create your views here.
