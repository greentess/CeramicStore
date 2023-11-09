from django.shortcuts import render,redirect
from django.views.generic.base import View
from store.mixins import ProfileMixin
from store.models.customer import Customer

from django.shortcuts import render , redirect , HttpResponse

class SaveBuy(ProfileMixin,View):

    def get(self, request):
        return render(request, 'email_success.html')