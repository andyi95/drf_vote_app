from rest_framework import status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from polling_api.permissions import IsStaffOrOwner
from polling_api.models import Poll, RespondentUser
from polling_api.serializers import PollSerializer, UserSerializer, VoteSerializer


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsStaffOrOwner, ]

    def perform_create(self, serializer):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('poll_id'))
        if self.request.user.is_authenticated:
            serializer.save(respondent=self.request.user, poll=poll)
        elif self.request.session['responder_id'] is None:
            new_user = RespondentUser.objects.create()
            self.request.session['responder_id'] = new_user.pk
            serializer.save(respondent=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    # queryset = get_object_or_404(Poll, respondent=request.HttpRequest.user)
    serializer_class = UserSerializer
    permission_classes = [IsStaffOrOwner, ]

    def get_queryset(self):
        polls = Poll.objects.select_related('poll_questions', 'poll_respondent').filter(
            respondent=self.request.user
        )
        return polls.all()


class VoteViewset(APIView):

    def post(self, request):
        if not self.request.user.is_authenticated():
            user = RespondentUser.objects.create()
        else:
            user=RespondentUser.objects.get(id=self.request.user.id)
        serializer = VoteSerializer(respondent=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
