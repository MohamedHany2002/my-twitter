
from django import forms
from django.forms.utils import ErrorList
from django.contrib.auth.mixins import LoginRequiredMixin


class FormMixin(object):
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            return super(FormMixin,self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS]=ErrorList(["user must be logged in to continue"])
            return self.form_invalid(form)

class checkowner(object):
    def form_valid(self,form):
        if form.instance.user == self.request.user:
            return super(checkowner,self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS]=ErrorList(["you can't edit this tweet"])
            return self.form_invalid(form)
