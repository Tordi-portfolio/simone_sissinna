from django.contrib import admin
from .models import GalleryImage, FansCard,StoreFanCard, UserFanCardRecord

# Register your model
admin.site.register(GalleryImage)
admin.site.register(FansCard)
admin.site.register(StoreFanCard)
admin.site.register(UserFanCardRecord)