from rest_framework import serializers

from polling_api.models import Question, Poll, Vote, QueFieldOptions, RespondentUser


class QuestionSerializer(serializers.ModelSerializer):
    question_type = QueFieldOptions.objects.all(read_only=True)

    class Meta:
        fields = '__all__'
        model = Question


class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        fields = '__all__'
        model = Poll

class PollRWSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=False)

    class Meta:
        fields = '__all__'
        model = Poll


class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Vote


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        exclue = ['passwoed']
        model = RespondentUser