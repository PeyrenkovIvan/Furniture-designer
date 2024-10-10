from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from . models import Bed


admin.site.register(Bed)
