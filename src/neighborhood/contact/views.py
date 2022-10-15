from django.shortcuts import render
from django.views import View

class ContactView(View):
    initial = {}
    template_name = 'contact/contact.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        return render(request=request, template_name=self.template_name)