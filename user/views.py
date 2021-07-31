from django.shortcuts import render
from allauth.account.views import SignupView
from photoshoots.models import photo_shoot
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from photoshoots.models import Review


class PersonalArea(LoginRequiredMixin, generic.ListView):
    """Личный кабинет, где перечисляются фотосессии пользователя"""
    model = photo_shoot
    template_name = 'user/PersonalArea.html'
    paginate_by = 10

    def get_queryset(self):
        return photo_shoot.objects.filter(linkUser=self.request.user)

    def get_context_data(self, **kwargs):
        menu = [
            ("bi-house", "portfolio")
        ]
        context = super().get_context_data(**kwargs)
        context['right_text'] = 'Личный Кабинет'
        context['navbar_show'] = True
        context['menu'] = menu
        context['title'] = "Личный Кабинет"

        return context


personal = PersonalArea.as_view()


class AccountSignupView(SignupView):
    """Кастомный вид для авторизации. Здесь включен navbar"""
    # Signup View extended
    template_name = "account/login.html"

    def get_context_data(self, **kwargs):
        menu = [
            ("bi-house", "portfolio")
        ]
        context = super().get_context_data(**kwargs)
        context['right_text'] = 'Авторизация'
        context['navbar_show'] = True
        context['menu'] = menu
        context['title'] = context['right_text']
        return context


account_signup_view = AccountSignupView.as_view()
