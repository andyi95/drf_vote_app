from django.contrib import admin

from polling_api.models import Question, Poll, RespondentUser

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name')

class PollAdmin(admin.ModelAdmin):
    list_display = ('name', 'poll_respondent, ')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('poll', 'text', 'question_type', )

