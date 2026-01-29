from django.db import models

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class")
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Skill Categories"
        ordering = ['order']

    def __str__(self):
        return self.name

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend Development'),
        ('backend', 'Backend Development'),
        ('database', 'Databases'),
        ('design', 'UI/UX Design'),
        ('mobile', 'Mobile Development'),
        ('tools', 'Tools & Collaboration'),
        ('soft', 'Soft Skills'),
    ]

    name = models.CharField(max_length=100)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class")
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category', 'order']

    def __str__(self):
        return f"{self.name} ({self.category.name})"
