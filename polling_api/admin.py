from django.contrib import admin

from polling_api.models import Vote, Poll, RespondentUser


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name')


class PollAdmin(admin.ModelAdmin):
    list_display = ('start_time',
                    'end_time', 'name',
                    'poll_respondent',
                    'owner', 'poll_questions'
                    )
    search_fields = ('owner', 'start_time')
    list_filter = ('start_time', 'owner')


class VoteAdmin(admin.ModelAdmin):
    list_display = ('poll', 'vote_poll', 'choice')
    list_filter = ('poll')


admin.site.register(RespondentUser, UserAdmin)
admin.site.register(Poll, PollAdmin)
admin.site.register(Vote, VoteAdmin)
