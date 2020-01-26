from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('user_name', 'pub_date', 'rating')


admin.site.register(Review, ReviewAdmin)

