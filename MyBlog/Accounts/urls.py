from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path("signup/",views.signup_view,name = "signup"),
    path("login/",views.login_view,name = "login"),
    path("logout/",views.logout_view,name = "logout"),
    path("<int:user_id>",views.profile_view),
    path("bloggerAccess/",views.register_as_blogger,name = "bloggerAccess"),
]
