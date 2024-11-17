from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)

from app.flat.tasks import upload_ipfs_link
from app.flat.models import Flat, FlatImage, IPFSLink


class FlatListView(ListView):
    model = Flat
    template_name = "flat/flat_list.html"
    context_object_name = "flats"


class FlatDetailView(DetailView):
    model = Flat
    template_name = "flat/flat_detail.html"
    context_object_name = "flat"


class FlatDeleteView(DeleteView):
    model = Flat
    template_name = "flat/flat_delete.html"
    success_url = reverse_lazy("flat:list")


class FlatCreateView(CreateView):
    model = Flat
    fields = [
        "address",
        "description",
        "price",
    ]
    template_name = "flat/flat_create.html"
    success_url = reverse_lazy("flat:list")

    def form_valid(self, form):
        response = super().form_valid(form)
        images = self.request.FILES.getlist("images")
        flat = self.object
        for image in images:
            flat_image = FlatImage.objects.create(flat=flat, image=image)
            cid, ipfs_link = upload_ipfs_link(image)
            if cid and ipfs_link:
                ipfs_entry = IPFSLink.objects.create(cid=cid, link=ipfs_link)
                flat_image.ipfs_link = ipfs_entry
                flat_image.save()
        return response
