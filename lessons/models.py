# lessons/models.py
from django.db import models
from courses.models import Course

class Lesson(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="lessons",
    )
    title = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)

    # Optional: gating
    requires_previous_completion = models.BooleanField(default=False)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.course.title} – {self.title}"


class LessonBlock(models.Model):
    TEXT = "text"
    VIDEO = "video"
    IMAGE = "image"
    EMBED = "embed"

    BLOCK_TYPE_CHOICES = [
        (TEXT, "Text"),
        (VIDEO, "Video"),
        (IMAGE, "Image"),
        (EMBED, "Embed"),
    ]

    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name="blocks",
    )
    block_type = models.CharField(max_length=20, choices=BLOCK_TYPE_CHOICES)
    order = models.PositiveIntegerField(default=0)

    # Atomic payload fields (only some used per type)
    text = models.TextField(blank=True)
    media_url = models.URLField(blank=True)
    embed_code = models.TextField(blank=True)

    class Meta:
        ordering = ["order"]
