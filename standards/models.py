from django.db import models
from data.models import Category

class Standard(models.Model):
    STATUS_CHOICES = [
        ('current', 'Current'),
        ('pending', 'Pending'),
        ('review', 'Review'),
    ]
    CURRICULUM_CHOICES = [
        ('NZC', 'NZC'),
        ('NCEA', 'NCEA'),
        ('NZQA', 'NZQA'),
    ]
    curriculum = models.CharField(max_length=10, choices=CURRICULUM_CHOICES, default='NCEA')   
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='standards', null=True)
    standard_number = models.CharField(max_length=10, unique=True, default='AS92L')
    title = models.CharField(max_length=255)
    level = models.PositiveSmallIntegerField(default=3)
    credits = models.PositiveSmallIntegerField(default=5)

    # Achievement Standard, Unit Standard (future-proof), etc.
    assessment_type = models.CharField(max_length=50, default='Achievement Standard')

    # Internal / External
    mode = models.CharField(max_length=20, default='Internal')

    version = models.PositiveSmallIntegerField(default=1)

    # Current / Expiring / Expired
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    # Timestamps for your own tracking
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["standard_number"]

    def __str__(self):
        return f"{self.standard_number} – {self.title}"

