from store.models.customer import Customer
from django import views
from django.shortcuts import render,redirect

class ProfileMixin(views.generic.detail.SingleObjectMixin, views.View):
    def dispatch(self, request, *args, **kwargs ):
        if request.user.is_authenticated:
            customer=Customer.objects.filter(user=request.user).first()
            if not customer:
                customer=Customer.objects.create(user=request.user)
            customer.save()
            request.session['customer'] = customer.id
        return super().dispatch(request, *args, **kwargs)
