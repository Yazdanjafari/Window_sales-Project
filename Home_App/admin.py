from django.contrib import admin
from .models import Manager, FirstShow, WhyUPVC, WhyChoose, BeforeBuyCost, BeforeBuyWhyWindowmall, BeforeBuyOrder, SocialMedia, Request


class BaseReadOnlyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Manager)
class ManagerAdmin(BaseReadOnlyAdmin):
    list_display = ('First_Name', 'Last_Name', 'Email', 'Phone_Number')

@admin.register(FirstShow)
class FirstShowAdmin(BaseReadOnlyAdmin):
    pass

@admin.register(WhyChoose)
class WhyChooseAdmin(BaseReadOnlyAdmin):
    pass

admin.site.register(WhyUPVC)
admin.site.register(BeforeBuyCost)
admin.site.register(BeforeBuyWhyWindowmall)
admin.site.register(BeforeBuyOrder)
admin.site.register(SocialMedia)
admin.site.register(Request)