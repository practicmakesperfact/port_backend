from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    tech_stack = models.TextField(help_text="Comma-separated list of technologies")
    features = models.TextField(help_text="Comma-separated list of features")
    is_featured = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def get_tech_stack_list(self):
        return [tech.strip() for tech in self.tech_stack.split(',') if tech.strip()]

    def get_features_list(self):
        return [feature.strip() for feature in self.features.split(',') if feature.strip()]
