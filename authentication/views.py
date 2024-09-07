# authentication/views.py

from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import CustomUser
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .forms import ChildRegistrationForm
from django.utils.timezone import now
from datetime import timedelta, date
from .models import Child
from django.db.models import Count
from django.http import JsonResponse


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome, {user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')

@login_required
def dashboard(request):
    if request.user.is_admin():
        return render(request, 'authentication/dashboard_admin.html')
    elif request.user.is_teacher():
        return render(request, 'authentication/dashboard_teacher.html')
    else:
        return render(request, 'authentication/dashboard_student.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            # Optionally handle user types or additional logic
            user_type = form.cleaned_data.get('user_type')
            # Perform any additional actions based on the user_type or authentication value
            
            messages.success(request, 'User created successfully.')
            return redirect('dashboard')  # Redirect to a success page
        else:
            print(form.errors)
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'authentication/register.html', {'form': form})

def root_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('login')

def all_users(request):
    users = User.objects.all()
    return render(request, 'authentication/all_users.html', {'users': users})

def delete_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        messages.success(request, 'User deleted successfully.')
    except User.DoesNotExist:
        messages.error(request, 'User does not exist.')
    return redirect('all_users')

def reset_password(request, user_id):
    # Logic to reset the password (e.g., setting a temporary password and emailing it)
    user = User.objects.get(id=user_id)
    new_password = User.objects.make_random_password()
    user.set_password(new_password)
    user.save()
    # Email the new password to the user or display it in a message
    messages.success(request, f"Password for {user.username} has been reset. New password: {new_password}")
    return redirect('all_users')

def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully.')
            return redirect('all_users')
    else:
        form = CustomUserCreationForm(instance=user)

    return render(request, 'authentication/edit_user.html', {'form': form})

def all_users(request):
    print("All Users View Accessed")
    users = CustomUser.objects.all()  # Fetch all users from the database
    return render(request, 'authentication/all_users.html', {'users': users})

def register_child(request):
    if request.method == 'POST':
        form = ChildRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Child created successfully.')
            return redirect('dashboard')  # Redirect to a success page or another view
    else:
        form = ChildRegistrationForm()
    
    return render(request, 'authentication/register_child.html', {'form': form})

def dashboard(request):
    # Fetch the count of children by gender
    gender_data = Child.objects.values('gender').annotate(count=Count('gender'))

    total_children = Child.objects.count()

    # Fetch the 5 most recent children
    recent_children = Child.objects.order_by('-created_at')[:5]

    # Prepare gender data for the chart
    genders = ['Male', 'Female']
    male_count = gender_data.filter(gender='M').count()
    female_count = gender_data.filter(gender='F').count()

    # Pass data to the template
    context = {
        'total_children': total_children,
        'recent_children': recent_children,
        'male_count': male_count,
        'female_count': female_count,
    }
    
    # Pass it to the template context
    return render(request, 'authentication/dashboard_admin.html', context)

def all_children_view(request):
    children = Child.objects.all()

    # Calculate each child's age based on their date of birth
    for child in children:
        child.age = date.today().year - child.date_of_birth.year - (
            (date.today().month, date.today().day) < (child.date_of_birth.month, child.date_of_birth.day)
        )

    context1 = {
        'children': children,
    }

    return render(request, 'authentication/all_children.html', context1)

def child_details(request, child_id):
    child = Child.objects.get(id=child_id)
    data = {
        'first_name': child.first_name,
        'last_name': child.last_name,
        'date_of_birth': child.date_of_birth,
        'parent_name': child.parent_name,
        'contact_number': child.contact_number,
        'address': child.address,
        'gender': child.get_gender_display(),
        'passport_image_url': child.passport_image.url if child.passport_image else None,
    }
    return JsonResponse(data)