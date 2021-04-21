from django.urls import include, path
from rest_framework.routers import DefaultRouter

from polling_api.views import PollViewSet, UserViewSet, VoteViewset

router = DefaultRouter()
router.register('', PollViewSet, basename='polls')
router.register(r'polls/(?P<poll_id>\d+', PollViewSet, basename='poll')
router.register(r'users/(?P<user_id>\d+', UserViewSet, basename='user')
router.register(r'polls/(?P<poll_id>\d+/vote', VoteViewset, basename='vote')

urlpatterns = [
    path('api/', include(router.urls)),
]
