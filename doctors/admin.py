from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Package)
# admin.site.register(ProofDonation)
admin.site.register(Article)
admin.site.register(New)
admin.site.register(Doctor)
admin.site.register(Patient)
# admin.site.register(Specialitie)
# admin.site.register(Appointment)
admin.site.register(Buy)

