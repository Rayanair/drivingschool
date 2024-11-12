from django.shortcuts import render, redirect,  get_object_or_404
from .models import Student, Instructor, Secretary, Appointment
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib import messages
from .models import StudentPackage
from .forms import PurchaseHoursForm
def student_list(request):
    students = Student.objects.all()
    return render(request, 'driving_school/student_list.html', {'students': students})

def instructor_list(request):
    instructors = Instructor.objects.all()
    return render(request, 'driving_school/instructor_list.html', {'instructors': instructors})

def secretary_list(request):
    secretaries = Secretary.objects.all()
    return render(request, 'driving_school/secretary_list.html', {'secretaries': secretaries})


def home(request):
    return render(request, 'driving_school/home.html')

def euro(request):
    return render(request, 'driving_school/euro.html')

def contact(request):
    return render(request, 'driving_school/contact.html')

def connexion(request):
    if request.method == 'POST':
        email = request.POST['email']  
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)  
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error_message = "Adresse e-mail ou mot de passe incorrect."
            return render(request, 'driving_school/connexion.html', {'error_message': error_message})
    else:
        return render(request, 'driving_school/connexion.html')   
    
@login_required(login_url='connexion')
def dashboard_view(request):
    user = request.user
    user_info = {
        'username': user.username,
        'email': user.email,
    }
    if hasattr(user, 'instructor'):
        user_info['instructor'] = user.instructor
    elif hasattr(user, 'student'):
        student = user.student
        user_info['student'] = {
            'username': student.user.username,
            'email': student.user.email,
            'first_name': student.user.first_name,
            'last_name': student.user.last_name,
            'address': student.address,
            'phone_number': student.phone_number,
            'birth_date': student.birth_date,
            'hours_paid': student.hours_paid,
            'lessons_taken': student.lessons_taken,
            'hours_available': student.hours_available,
        }
    return render(request, 'driving_school/dashboard.html', {'user_info': user_info})
def deconnexion(request):
    logout(request)
    return redirect('home')

@login_required(login_url='connexion')
def student_appointments(request):
    if hasattr(request.user, 'student'):
        appointments = Appointment.objects.filter(student=request.user.student)
        return render(request, 'driving_school/student_appointments.html', {'appointments': appointments})
    else:
        return redirect('dashboard')  

@login_required(login_url='connexion')
def instructor_appointments(request):
    if hasattr(request.user, 'instructor'):
        appointments = Appointment.objects.filter(instructor=request.user.instructor)
        return render(request, 'driving_school/instructor_appointments.html', {'appointments': appointments})
    else:
        return redirect('dashboard') 

@login_required(login_url='connexion')
def instructor_students(request):
    if hasattr(request.user, 'instructor'):
       students = Student.objects.filter(appointment__instructor=request.user.instructor).distinct()
       return render(request, 'driving_school/instructor_students.html', {'students': students})
    else:
        return redirect('dashboard')

@login_required(login_url='connexion')
def new_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            return redirect('instructor_appointments')
    else:
        form = AppointmentForm()
    return render(request, 'driving_school/new_appointment.html', {'form': form})

@login_required(login_url='connexion')
@csrf_exempt
def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    appointment.delete()
    return redirect('instructor_appointments')

@login_required(login_url='connexion')
@csrf_exempt
def edit_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('instructor_appointments')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'driving_school/edit_appointment.html', {'form': form, 'appointment': appointment})

def get_student_hours(request, student_id):
    student = Student.objects.get(id=student_id)
    return JsonResponse({'hours_available': student.hours_available})



@login_required
def purchase_hours(request):
    # Vérifier si l'utilisateur est un étudiant
    try:
        student = request.user.student
    except Student.DoesNotExist:
        messages.error(request, "Vous devez être un étudiant pour acheter des heures.")
        return redirect('home')  # Redirigez vers une vue appropriée

    if request.method == 'POST':
        form = PurchaseHoursForm(request.POST)
        if form.is_valid():
            hours_to_add = form.cleaned_data['hours']
            student.hours_available += hours_to_add
            student.hours_paid += hours_to_add
            student.save()
            messages.success(request, f'Vous avez acheté {hours_to_add} heures de conduite.')
            return redirect('dashboard') 
    else:
        form = PurchaseHoursForm()

    return render(request, 'driving_school/acheter-heures.html', {'form': form})