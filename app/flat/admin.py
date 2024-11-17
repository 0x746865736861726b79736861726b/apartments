from django.contrib import admin

from app.flat.models import Flat, FlatImage, IPFSLink

admin.site.register(Flat)
admin.site.register(FlatImage)
admin.site.register(IPFSLink)
