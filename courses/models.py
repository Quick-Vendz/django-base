# courses/models.py
from django.db import models
from standards.models import Standard
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Category(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=10, default="neutral")

    def __str__(self):
        return self.name


class Course(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="courses",
        null=True,
    )
    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="courses_taught",
        limit_choices_to={"role": "teacher"},
    )
    level = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    blurb = models.TextField(max_length=600, blank=True)
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Anytime course: no fixed start/end required
    allow_self_enroll = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} (Level {self.level})"
    
    class Meta:
        ordering = ['level', 'title']


from django.db import models

class Block(models.Model):
    course = models.ForeignKey(
        "Course",
        on_delete=models.CASCADE,
        related_name="blocks"
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    description = models.TextField(blank=True)

    # Estimated duration (e.g., 3–6 weeks)
    estimated_weeks = models.PositiveIntegerField(default=4)

    # Standards attached to this block
    standards = models.ManyToManyField(
        Standard,
        related_name="blocks",
        blank=True
    )

    # Optional: resources, links, files, etc.
    resources = models.JSONField(default=dict, blank=True)

    # Optional: assessment rubric or criteria
    assessment_criteria = models.TextField(blank=True)

    # Whether the block is active/visible to students
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["course", "title"]

    def __str__(self):
        return f"{self.title} ({self.course.title})"


class Enrollment(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="enrollments",
        limit_choices_to={"role": "student"},
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="enrollments",
    )
    enrolled_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ("student", "course")
