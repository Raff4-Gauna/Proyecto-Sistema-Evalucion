from django.urls import path
from .views import *
from . import views

app_name="usuarios"

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login_user'), 
    path('signup/', CustomRegisterUserView.as_view(), {'next_page': None}, name='signup_user'),  
    path('logout/', CustomLogoutView.as_view(), name='logout_user'),  
    path('confirm_logout/', CustomConfirmLogoutView.as_view(), {'next_page': None}, name='confirm_logout_user'),

    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),

    path('update/', CustomUpdateUserView.as_view(), name='update_user'),
    path('change_password/', CustomPasswordChangeView.as_view(), name='change_password'),

]

