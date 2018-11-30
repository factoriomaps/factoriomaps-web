from django.urls import path

import account.views


urlpatterns = [
    path(r'user/?', account.views.UserView.as_view())
]
