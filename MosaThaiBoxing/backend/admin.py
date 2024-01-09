from django import forms
from django.contrib import admin
from .models import (
    Post,
    Trainer,
    Price,
    Merchandise,
    Feedback,
    TrainingRegistration,
    Contact,
    AboutUs,
    MerchandisePhoto,
    Size,
)

admin.site.register(Post)
admin.site.register(Trainer)
admin.site.register(Price)
admin.site.register(Merchandise)
admin.site.register(Feedback)
admin.site.register(TrainingRegistration)
admin.site.register(Contact)
admin.site.register(AboutUs)
admin.site.register(MerchandisePhoto)
admin.site.register(Size)
