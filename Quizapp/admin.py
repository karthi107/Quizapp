from django.contrib import admin
from .models import *

admin.site.register(QuestionBank)
admin.site.register(CustomUser)
admin.site.register(Questions)
admin.site.register(Useranswer)