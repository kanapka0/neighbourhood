from django import forms
from . import models


class NewReportForm(forms.ModelForm):

    class Meta:
        model = models.Report
        fields = ['name','location']

    def save(self, commit=True):
        report = super(NewReportForm, self).save(commit=False)
        report.name = self.cleaned_data['name']
        report.location = self.cleaned_data['location']

        report.value = 0

        if commit:
            report.save()
        return report