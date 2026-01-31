# comments/models.py
from django.db import models
from django.conf import settings
from assignments.models import Assignment, Submission
from lessons.models import Lesson

User = settings.AUTH_USER_MODEL

class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    lesson = models.ForeignKey(
        Lesson,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    assignment = models.ForeignKey(
        Assignment,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    submission = models.ForeignKey(
        Submission,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # You can enforce “one of lesson/assignment/submission must be set” in clean()
