from django.urls import path
from . import views
from django.conf import settings  # settings 가져오
from django.conf.urls.static import static  # static 가져오기

app_name = 'profiles'

urlpatterns = [
    path('', views.profile, name='profile_main'),
    path('edit_nickname/', views.edit_nickname, name='edit_nickname'),
    path('edit_profile_image/', views.edit_profile_image, name='edit_profile_image'),
    path('logout/', views.logout, name='logout'),
    path('<str:username>/', views.friend_profile, name='friend_profile'),  # 친구 프로필 페이지
    path('delete_friend/<str:username>/', views.delete_friend, name='delete_friend'),
    path('send_request/<str:username>/', views.send_friend_request, name='send_request'),
]
if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
