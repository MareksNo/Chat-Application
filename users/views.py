from django.shortcuts import render
from django.views.generic import edit
from django.http import HttpResponseRedirect
from users import forms


class LoginView(edit.FormView):
    template_name = 'users/login.html'
    form_class = forms.LoginForm
    success_url = 'chat/chatroom/1'

    def form_valid(self, form):
        login_status = form.login_user(request=self.request)
        if login_status:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))