from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import Slide, Options, Contact, About, Phone, Partners, Features


# Apply summernote to all TextField in model.
class OptionsModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(Slide)
admin.site.register(Contact, OptionsModelAdmin)
admin.site.register(About, OptionsModelAdmin)
admin.site.register(Options, OptionsModelAdmin)
admin.site.register(Features, OptionsModelAdmin)
admin.site.register(Partners)
admin.site.register(Phone)