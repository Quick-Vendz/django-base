from django.db import models

from django.db import models

class LearningArea(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Strand(models.Model):
    learning_area = models.ForeignKey(LearningArea, on_delete=models.CASCADE, related_name="strands")
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.learning_area.name} – {self.name}"


class NZCExpectation(models.Model):
    strand = models.ForeignKey(Strand, on_delete=models.CASCADE, related_name="expectations")

    # NZC structural fields
    phase = models.CharField(max_length=20)  # e.g., "Phase 1", "Phase 2"
    year_level = models.PositiveIntegerField(null=True, blank=True)  # optional, NZC is phase-based

    # Core expectation text
    expectation_text = models.TextField()  # the actual NZC expectation

    # Indicators / success criteria
    indicators = models.JSONField(default=list, blank=True)
    # Example: ["Reads numbers to 100", "Orders numbers correctly"]

    # Optional metadata
    progression_code = models.CharField(max_length=50, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.strand.name}: {self.expectation_text[:60]}..."

