from django import forms
from . import models
class ComSetNeighborlyForm(forms.ModelForm):

    class Meta:
        model = models.Comments
        fields = ['comment','title']

    def save(self, commit=True):
        report = super(ComSetNeighborlyForm, self).save(commit=False)
        report.comment = self.cleaned_data['comment']

        if commit:
            report.save()
        return report

class IcreaseValueForm(forms.Form):
    value = forms.IntegerField(label="Liczba like", min_value=0)

class NeighborlyHelpForm(forms.ModelForm):

    class Meta:
        model = models.NeighborlyHelp
        fields = ['title','name','description']

    def save(self, commit=True):
        report = super(NeighborlyHelpForm, self).save(commit=False)
        report.title = self.cleaned_data['title']
        report.name = self.cleaned_data['name']
        report.description = self.cleaned_data['description']


        if commit:
            report.save()
        return report

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

class NewSubmissionsForm(forms.ModelForm):

    class Meta:
        model = models.Submissions
        fields = ['name','surname','email','description','location']

    def save(self, commit=True):
        report = super(NewSubmissionsForm, self).save(commit=False)
        report.name = self.cleaned_data['name']
        report.surname = self.cleaned_data['surname']
        report.email = self.cleaned_data['email']
        report.description = self.cleaned_data['description']
        report.location = self.cleaned_data['location']
        report.done = 0


        if commit:
            report.save()
        return report