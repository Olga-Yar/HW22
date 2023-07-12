import random

from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views import View
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
from users.utils import send_email_verify

from django.contrib.auth.tokens import default_token_generator as token_generator, default_token_generator


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.is_active = False
        new_user.save()

        # создание токена подтверждения
        token = default_token_generator.make_token(new_user)
        uid = urlsafe_base64_encode(force_bytes(new_user.pk))

        # формирование ссылки для подтверждения
        confirm_url = reverse('users:verify_email', kwargs={'uidb64': uid, 'token': token})
        confirm_url = self.request.build_absolute_uri(confirm_url)

        send_mail(
            subject='Подтвердите вашу почту',
            message=f'Для завершении регистрации подтвердите вашу почту, перейдя по ссылке: {confirm_url}.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


class EmailVerify(View):

    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            login(request, user)
            return redirect('users:profile')
        return redirect('users:invalid_verify')

    @staticmethod
    def get_user(uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist, ValidationError):
            user = None
        return user


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    send_mail(
        subject='Изменение пароля',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('catalog:home'))
