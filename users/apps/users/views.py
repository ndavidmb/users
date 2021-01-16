from django.shortcuts import render
from django.core.mail import send_mail
from django.views.generic.edit import FormView
from django.views.generic import View
from django.http import HttpResponseRedirect

from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import (
    UserRegisterForm,
    LoginForm,
    UpdatePasswordForm,
    VerificationForm,
)
from .models import User

from .functions import code_generator


class UserCreateView(FormView):
    template_name = "users/add_user.html"
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self, form):
        # Generamos el código
        code = code_generator()

        user = User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            names=form.cleaned_data['names'],
            last_names=form.cleaned_data['last_names'],
            gender=form.cleaned_data['gender'],
            register_code=code,
        )
        # enviar el código al email
        subject = 'Confirmación del email'
        message = 'Código de verificación: ' + code
        from_email = 'developerdmail.debug@gmail.com'
        send_mail(subject, message, from_email, [form.cleaned_data['email'], ])
        # redirigir a pantalla de verificación

        return HttpResponseRedirect(
            reverse(
                'users_app:verification',
                kwargs={
                    'pk': user.id
                }
            ),
        )


class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:panel')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse('users_app:login-register')
        )


class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = 'users/update.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('users_app:update-password')
    login_url = reverse_lazy('users_app:login-register')

    def form_valid(self, form):
        user = self.request.user
        authenticate(
            username=user.username,
            password=form.cleaned_data['password1'],
        )
        if user:
            new_password = form.cleaned_data['password2']
            user.set_password(new_password)
            user.save()

        logout(self.request)
        return super(UpdatePasswordView, self).form_valid(form)


class CodeVerificationView(FormView):
    template_name = 'users/verification.html'
    form_class = VerificationForm
    success_url = reverse_lazy('users_app:login-register')

    def get_form_kwargs(self):
        kwargs = super(CodeVerificationView, self).get_form_kwargs()
        kwargs.update({
            'pk': self.kwargs['pk'],
        })
        return kwargs

    def form_valid(self, form):
        User.objects.filter(
            id=self.kwargs['pk'],
        ).update(
            is_active=True
        )

        return super(CodeVerificationView, self).form_valid(form)
