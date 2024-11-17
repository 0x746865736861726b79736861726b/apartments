from django.db import models

from app.base.models import BaseModel
from app.flat.managers import AvailableFlatManager


class Flat(BaseModel):
    address = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    is_purchased = models.BooleanField(default=False, blank=True)

    objects = models.Manager()
    available = AvailableFlatManager()

    class Meta:
        verbose_name = "Flat"
        verbose_name_plural = "Flats"

    def __str__(self) -> str:
        return self.address


class FlatImage(BaseModel):
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="media/")

    class Meta:
        verbose_name = "Flat Image"
        verbose_name_plural = "Flat Images"

    def __str__(self) -> str:
        return self.flat.address


class IPFSLink(BaseModel):
    cid = models.CharField(max_length=255, unique=True)
    link = models.URLField(max_length=500)

    class Meta:
        verbose_name = "IPFS Link"
        verbose_name_plural = "IPFS Links"

    def __str__(self) -> str:
        return self.link
