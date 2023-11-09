from django.shortcuts import render,redirect
from django.views.generic.base import View
from store.mixins import ProfileMixin
from store.models.customer import Customer

from django.shortcuts import render , redirect , HttpResponse

class SaveBuy(ProfileMixin,View):

    def get(self, request):
        #customer = Customer.objects.get(user=request.user)
        #customer.email = 'abc@mail.ru'
        #customer.save()
        #request.session['customer'] = customer.id

        return render(request, 'about.html')

def email_success(request):
    res = 'Email is verified!'
    return HttpResponse('<p>%s</p>' % res)