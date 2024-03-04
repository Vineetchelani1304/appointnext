from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    history = models.TextField(blank=True)
    refreshToken = models.CharField(max_length=255, blank=True)

    # Specify custom related names for the groups and user_permissions fields
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    def addToHistory(self, appointment_id):
        if not self.history:
            self.history = str(appointment_id)
        else:
            self.history += ',' + str(appointment_id)
        self.save()

# class appointment(models.Model):
#     withDoctor = models.ForeignKey(, related_name='doctor_appointments', on_delete=models.CASCADE)
#     user = models.ForeignKey(User, related_name='user_appointments', on_delete=models.CASCADE)
#     # time = models.TimeField(auto_now_add=True)
#     # date = models.DateField(auto_now_add=True)

# class organisation(models.Model):
#     name = models.CharField(max_length=50)
#     address = models.CharField(max_length=250)
#     contact = models.IntegerField()
#     appointments = models.ForeignKey(appointment, on_delete=models.CASCADE)

#     def addAppointment(self, appointment_id):
#         if not self.appointments.filter(id=appointment_id).exists():
#             self.appointments.add(appointment_id)



# class ServiceCategory(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()

#     def __str__(self):
#         return self.name

# class Service(models.Model):
#     category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     provider = models.ForeignKey(User, on_delete=models.CASCADE)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     duration_minutes = models.PositiveIntegerField()

#     def __str__(self):
#         return self.name

# class Appointment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     service = models.ForeignKey(Service, on_delete=models.CASCADE)
#     date_time = models.DateTimeField()
#     status_choices = [
#         ('BOOKED', 'Booked'),
#         ('CANCELLED', 'Cancelled'),
#         ('COMPLETED', 'Completed')
#     ]
#     status = models.CharField(max_length=10, choices=status_choices)

#     def __str__(self):
#         return f"{self.user.username} - {self.service.name} - {self.date_time.strftime('%Y-%m-%d %H:%M')}"

# class Review(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     service = models.ForeignKey(Service, on_delete=models.CASCADE)
#     rating = models.IntegerField()
#     comment = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username} - {self.service.name} - Rating: {self.rating}"

# class AppointmentReminder(models.Model):
#     appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
#     reminder_time = models.DateTimeField()

#     def __str__(self):
#         return f"{self.appointment} - Reminder at {self.reminder_time.strftime('%Y-%m-%d %H:%M')}"
