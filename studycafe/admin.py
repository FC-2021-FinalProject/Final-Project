from django.contrib import admin

from .models import PersonalUser, BusinessUser, StudyCafe, CafeImage, Reservations, Date, HourTime, Seats, Review, BookmarkedCafe

class PhotoInline(admin.TabularInline) :
    model = CafeImage

class ArticleAdmin(admin.ModelAdmin) :
    inlines = [PhotoInline, ]

# Register your models here.
admin.site.register(PersonalUser)
admin.site.register(BusinessUser)
admin.site.register(Reservations)
admin.site.register(StudyCafe, ArticleAdmin)
admin.site.register(Date)
admin.site.register(HourTime)
admin.site.register(Seats)
admin.site.register(Review)
admin.site.register(BookmarkedCafe)