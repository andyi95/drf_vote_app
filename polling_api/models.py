from django.contrib.auth.models import (PermissionsMixin, AbstractUser,
                                        AbstractBaseUser)
from django.db import models
from django.utils.translation import ugettext_lazy as _


class RespondentUser(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    username = models.CharField(
        _('username'), max_length=30,
        unique=False, null=True
    )
    first_name = models.CharField(40, null=True)
    last_name = models.CharField(40, null=True)
    email = models.EmailField(null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


class Poll(models.Model):
    name = models.CharField(max_length=200)
    start_time = models.DateTimeField(
        auto_now_add=True, editable=False
    )
    end_time = models.DateTimeField(
        blank=True,
        null=True
    )
    owner = models.ForeignKey(RespondentUser, on_delete=models.CASCADE)

    class Meta:
        ordering = ['start_time', ]

    def __str__(self):
        return self.name[:50]


class QueFieldOptions(models.Model):
    text = models.CharField(max_length=200)
    choice = models.CharField(max_length=200)

    def __str__(self):
        return self.text[:40]


class Question(models.Model):
    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        related_name='poll_questions'
    )
    text = models.TextField(max_length=120)
    question_type = models.ManyToManyField(
        QueFieldOptions,
        default='text', null=False
    )

    def __str__(self):
        return self.text[:40]


class Vote(models.Model):
    respondent = models.ForeignKey(
        RespondentUser,
        on_delete=models.CASCADE, related_name='vote_poll'
    )
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice = models.ManyToManyField(QueFieldOptions)
