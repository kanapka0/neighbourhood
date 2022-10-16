from django.shortcuts import render, redirect
from django.views import View
from .forms import NewReportForm
from .models import Report
from django.contrib import messages

class IndexView(View):
    template_name = 'reports/reports.html'

    def get(self, request):
        reports = Report.objects.all()

        ctx = {
            'reports': reports,
        }
        return render(request, self.template_name, context=ctx)

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