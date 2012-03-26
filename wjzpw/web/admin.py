# coding: utf-8
from django.contrib import admin
from wjzpw.web.models import Province, Industry, Location, City, UserProfile, Service, Job, PictureAdv, Announcement, Configuration, Feedback, FriendlyLink

class IndustryAdmin(admin.ModelAdmin):
    pass

class LocationAdmin(admin.ModelAdmin):
    pass

class CityAdmin(admin.ModelAdmin):
    pass

class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('name', 'type','spell', 'code')
    list_display_links =('name','type')
    list_filter = ('type',)
    ordering = ('name','type')
    search_fields = ('name', 'type')

class UserProfileAdmin(admin.ModelAdmin):
    pass

class ServiceAdmin(admin.ModelAdmin):
    pass

class JobAdmin(admin.ModelAdmin):
    pass

class PictureAdvAdmin(admin.ModelAdmin):
    pass

class AnnouncementAdmin(admin.ModelAdmin):
    pass

class ConfigAdmin(admin.ModelAdmin):
    pass

class FeedbackAdmin(admin.ModelAdmin):
    pass

class FriendlyLinkAdmin(admin.ModelAdmin):
    pass

admin.site.register(Industry, IndustryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Province, ProvinceAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(PictureAdv, PictureAdvAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Configuration, ConfigAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(FriendlyLink, FriendlyLinkAdmin)