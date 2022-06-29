from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView as LogView
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import (
    LoginForm,
    NewUserForm,
    UserRoleApplicationAndRegistrationFormset
)
from users.logic import _get_user_registration_formset, remember_user_for_two_week


class LoginView(LogView):
    authentication_form = LoginForm

    def form_valid(self, form):
        if form.data.get('remember_me'):
            remember_user_for_two_week(self.request)
        return super().form_valid(form)


class CreateUserRegistrationRequest(CreateView):
    form_class = NewUserForm
    template_name = 'registration/register.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['user_role_application_and_registration_formset'] = \
            UserRoleApplicationAndRegistrationFormset()
        return ctx

    def post(self, request, *args, **kwargs):
        self.object = None  # noqa
        form = self.get_form(self.get_form_class())
        user_role_application_and_registration_formset = \
            UserRoleApplicationAndRegistrationFormset(self.request.POST or None)
        if form.is_valid() and user_role_application_and_registration_formset.is_valid():
            return self.form_valid(form, user_role_application_and_registration_formset)
        return self.form_invalid(form, user_role_application_and_registration_formset)

    def form_valid(  # noqa pylint: disable=W0221
            self, form: NewUserForm,
            user_role_application_and_registration_formset:
            UserRoleApplicationAndRegistrationFormset):
        self.object = form.save(commit=False)  # noqa
        self.object.save()
        form = _get_user_registration_formset(user_role_application_and_registration_formset)
        form.user = self.object
        form.save()
        return redirect(reverse_lazy('successfully_created_registration_request'))

    def form_invalid(  # noqa pylint: pylint: disable=W0221
            self, form: NewUserForm,
            user_role_application_and_registration_formset:
            UserRoleApplicationAndRegistrationFormset):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                user_role_application_and_registration_formset=
                user_role_application_and_registration_formset,
            ),
            status=400
        )


@login_required
def index_view(request: HttpRequest):
    if request.user.is_authenticated and request.user.is_admin:  # noqa
        return redirect(reverse_lazy('admin_page'))
    return render(request, 'index.html')


def successfully_created_registration_request(request: HttpRequest):
    return render(request, 'successfully_created_registration_request.html')
