from django.urls import path, include
from account.views import SendPasswordResetEmailView, UserChangePasswordView, UserLoginView, UserProfileView, UserRegistrationView, UserPasswordResetView,RestuarantsApiView,addRestuarantsView,MenuView,menuViewSet,resturantView,SaveMenuView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('menu',MenuView,basename='menu')
router.register('menu_like',menuViewSet,basename='menu_like')
router.register('rest_like',resturantView,basename='restulike')



urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
      
    path('resturants/', RestuarantsApiView.as_view(),name='get'),
    path('resturants/<int:pk>/', RestuarantsApiView.as_view(),name='get'),
    path('addrestu/', addRestuarantsView.as_view(),name='add'),
    path('', include(router.urls)),
    path('user_save_menu/',SaveMenuView.as_view(),name='user_save_menu')
    

]