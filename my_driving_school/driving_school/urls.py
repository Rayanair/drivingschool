from django.urls import path
from . import views
from django.contrib import admin

path('delete_appointment/', views.delete_appointment, name='delete_appointment'),
urlpatterns = [
        path('admin/', admin.site.urls),
            path('', views.home, name='home'),
path('connexion/', views.connexion, name='connexion'),
    path('students/', views.student_list, name='student_list'),
    path('instructors/', views.instructor_list, name='instructor_list'),
    path('secretaries/', views.secretary_list, name='secretary_list'),
        path('dashboard/',views.dashboard_view, name='dashboard'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
  path('student_appointments/', views.student_appointments, name='student_appointments'),
    path('instructor_appointments/', views.instructor_appointments, name='instructor_appointments'),
        path('instructor_students/', views.instructor_students, name='instructor_students'),
  path('new_appointment/', views.new_appointment, name='new_appointment'),
path('delete_appointment/', views.delete_appointment, name='delete_appointment'),
path('edit_appointment/', views.edit_appointment, name='edit_appointment'),
    path('appointments/edit/<int:appointment_id>', views.edit_appointment, name='edit_appointment'),
    path('appointments/delete/<int:appointment_id>', views.delete_appointment, name='delete_appointment'),
    path('get_student_hours/<int:student_id>/', views.get_student_hours, name='get_student_hours'),

    path('auto-ecole-pour-permis-de-conduire', views.euro, name='euro'),
    path('contactez-nous-vauban-fourier-auto-moto-ecole-a-lyon', views.contact, name='contact'),
        path('acheter-heures', views.purchase_hours, name='purchase_hours'),


]
