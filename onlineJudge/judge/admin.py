from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *

admin.site.register(Problem)
admin.site.register(TestCase)
admin.site.register(ProgrammingLanguage)
admin.site.register(Submission)
admin.site.register(CodeRunner)
