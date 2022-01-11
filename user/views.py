from allauth.account.views import SignupView
from photoshoots.models import PhotoShoot
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from photoshoots.models import Review
import vk_api
from PhotographSite.settings import VK_BOT_TOKEN, VK_GROUP_ID
from allauth.socialaccount.models import SocialAccount


class PersonalArea(LoginRequiredMixin, generic.ListView):
    """Личный кабинет, где перечисляются фотосессии пользователя"""
    model = PhotoShoot
    template_name = 'user/PersonalArea.html'
    paginate_by = 10

    def get_queryset(self):
        return PhotoShoot.objects.filter(linkUser=self.request.user)

    def get_context_data(self, **kwargs):
        menu = [
            ("bi-house", "portfolio")
        ]
        context = super().get_context_data(**kwargs)
        context['right_text'] = 'Личный Кабинет'
        context['navbar_show'] = True
        context['menu'] = menu
        context['title'] = "Личный Кабинет"

        # Проверка можно ли писать пользователю сообщения
        vk_session = vk_api.VkApi(token=VK_BOT_TOKEN)
        vk_session_api = vk_session.get_api()
        user_id = SocialAccount.objects.get(user=self.request.user).uid
        if vk_session_api.messages.isMessagesFromGroupAllowed(user_id=user_id, group_id=VK_GROUP_ID)['is_allowed']:
            context['warning_vk'] = False
        else:
            context['warning_vk'] = True
        context['VK_GROUP_ID'] = VK_GROUP_ID

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
