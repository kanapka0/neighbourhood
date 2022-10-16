from django.shortcuts import render, redirect
from django.views import View
from .forms import NewReportForm
from django.contrib import messages

class IndexView(View):
    def get(self, request):
        reports = NewReportForm.objects.all()

        ctx = {
            'reports': reports,
        }
        return render(request, 'reports', context=ctx)

class AContactView(View):

    form_class = NewReportForm()
    initial = {}
    template_name = 'reports/new_report.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = NewReportForm(request.POST)
        if form.is_valid():
            report = form.save()
            return redirect('/reports')
        return render(request=request, template_name=self.template_name, context={"form": form})