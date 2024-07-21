from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os


class CV(models.Model):
    resume_url = models.URLField(max_length=200)  # Changed field name to 'resume_url'

    def __str__(self):
        return self.resume_url


class Projects(models.Model):
    """Model definition for ProjectSection."""

    name = models.CharField(max_length=200)
    description = models.TextField()
    demo_url = models.URLField(max_length=200)
    github_url = models.URLField(max_length=200)
    image = models.ImageField(upload_to="project_images/")

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        """Unicode representation of ProjectSection."""
        return self.name


@receiver(post_delete, sender=Projects)
def delete_project_image(sender, instance, **kwargs):
    """Delete image file from filesystem when corresponding `Projects` object is deleted."""
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
