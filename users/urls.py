from django.contrib.auth import logout
from django.urls import path
from users.views import user_login, signup, user_logout

app_name = "users"
urlpatterns = [
      path("login/", user_login, name = "login"),
      path('signup/', signup, name = "signup"),
      path("logout", user_logout, name="logout")
]