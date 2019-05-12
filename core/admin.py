from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from core.models import Home,OurWork,OurServices,Blog,Gallery,Contact
# Register your models here.
class HomeAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
        summernote_fields = '__all__'
class OurWorkAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
        summernote_fields = '__all__'
class OurServicesAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
        summernote_fields = '__all__'
class BlogAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
        summernote_fields = '__all__'

admin.site.register(Home, HomeAdmin)
admin.site.register(OurWork, OurWorkAdmin)
admin.site.register(OurServices, OurServicesAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Gallery)
admin.site.register(Contact)