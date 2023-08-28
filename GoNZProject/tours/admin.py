from django.contrib import admin
from .models import Tour,TourPicture
# Register your models here.


class PriceRangeFilter(admin.SimpleListFilter):
    title = ('Price Range')
    parameter_name = 'price_range'

    def lookups(self, request, model_admin):
        return (
            ('0-1500', ('0 to 1500')),
            ('1500-3500', ('1500-3500')),
            ('3500-5000', ('3500-5000')),
            ('5000-8000', ('5000-8000')),
            ('8000-10000', ('8000-10000')),
            ('above-10000', ('Above 10000')),
        )

    def queryset(self, request, queryset):
        if self.value() == '0-1500':
            return queryset.filter(price__range=(0, 1500))
        elif self.value() == '1500-3500':
            return queryset.filter(price__range=(1500, 3500))
        elif self.value() == '3500-5000':
            return queryset.filter(price__range=(3500, 5000))
        elif self.value() == '5000-8000':
            return queryset.filter(price__range=(5000, 8000))
        elif self.value() == '8000-10000':
            return queryset.filter(price__range=(8000, 10000))
        elif self.value() == 'above-10000':
            return queryset.filter(price__gt=10000)
        
class TourAdmin(admin.ModelAdmin):
    list_display=('id','title','destination','package_type','price','get_duration','get_period','agent','last_updated','tour_pictures_count')
    search_fields=('id','title','short_desc','desc','destination')
    list_filter=('destination','package_type',PriceRangeFilter,)
    
    class Meta:
        ordering=['id']

    def get_period(self,obj):
       
        return f"from {obj.start_date} to {obj.end_date}"
    
    get_period.short_description="date"

    def get_duration(self,obj):
        if obj.start_date and obj.end_date:
            no_of_days =(obj.end_date - obj.start_date).days
            if no_of_days>=0 :
                return f"{no_of_days} days"
            else:
                return f"error-0 days"
        return "N/A"
    get_duration.short_description="Duration"

    def tour_pictures_count(self, obj):
        return obj.tour_pictures.count()  # Return the count of tour pictures

    tour_pictures_count.short_description = 'Tour Pictures Count' 

admin.site.register(Tour,TourAdmin)
admin.site.register(TourPicture)