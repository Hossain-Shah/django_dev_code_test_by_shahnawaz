from BalanceTransfer.views import signup, profile, RegistrationLogin, BalanceList
from django.urls import path

urlpatterns = [
      path('signup/', signup, name='signup'),
      path('profile/', profile, name='profile'),
      path('registration-login/', RegistrationLogin.as_view()),
      path('user-balance/', BalanceList.as_view())
]
