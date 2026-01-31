# courses/models.py
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="subcategories",
        null=True,
    )
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=30, default="gray")

    def __str__(self):
        return self.name


class Course(models.Model):
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="courses",
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
