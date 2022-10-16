from django.shortcuts import render, redirect
from django.views import View
from .forms import NewReportForm, NewSubmissionsForm , NeighborlyHelpForm,ComSetNeighborlyForm
from .models import Report, Announcements,NeighborlyHelp,Comments
from django.contrib import messages
class ComSetNeighborlyView(View):
    template_name = 'reports/com_set_neighborly.html'

    def post(self, request, product_id, *args,):
        form = ComSetNeighborlyForm(request.POST)
        ctx = {
            'form': form,
            'product_id': product_id,
        }

        if form.is_valid():
            form.title = 2
            form.save()
            return redirect('/reports/neighborly/board')
        return render(request=request, template_name=self.template_name, context={"form": form})
class BoardNeighborlyHelpView(View):
    template_name = 'reports/neighborly_board.html'

    def get(self, request):
        announcements = NeighborlyHelp.objects.all().values()
        comments = Comments.objects.all().values()

        ctx = {
            'announcements': announcements,
            'comments': comments,
        }
        return render(request, self.template_name, context=ctx)
class AddNeighborlyHelpView(View):

    form_class = NeighborlyHelpForm()
    initial = {}
    template_name = 'reports/new_neighborly_help.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = NeighborlyHelpForm(request.POST)
        if form.is_valid():
            report = form.save()
            return redirect('/reports/neighborly/board')
        return render(request=request, template_name=self.template_name, context={"form": form})

class AnnouncementsView(View):
    template_name = 'reports/announcements.html'

    def get(self, request):
        reports = Announcements.objects.all().values()

        ctx = {
            'reports': reports,
        }
        return render(request, self.template_name, context=ctx)
class IcreaseValueView(View):
    def post(self, request, product_id):
        form = Report.objects.get(id=product_id)
        form.value += 1
        form.save()
        return redirect('/reports')


class IndexView(View):
    template_name = 'reports/reports.html'

    def get(self, request):
        reports = Report.objects.all().values()

        ctx = {
            'reports': reports,
        }
        return render(request, self.template_name, context=ctx)

class SubmissionsView(View):

    form_class = NewSubmissionsForm()
    initial = {}
    template_name = 'reports/new_submissions.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = NewSubmissionsForm(request.POST)
        if form.is_valid():
            report = form.save()
            return redirect('/reports')
        return render(request=request, template_name=self.template_name, context={"form": form})

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