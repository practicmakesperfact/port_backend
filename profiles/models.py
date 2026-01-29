from django.db import models
from django.core.validators import FileExtensionValidator

class Profile(models.Model):
    name = models.CharField(max_length=100, default="Haymanot Asmare")
    title = models.CharField(max_length=200, default="Full Stack Software Engineer")
    bio = models.TextField(
        default="I'm a passionate Full Stack Software Engineer with extensive experience in building scalable web applications and creating exceptional digital experiences. My expertise spans across modern frontend frameworks, robust backend systems, and intuitive UI/UX design."
    )
    detailed_bio = models.TextField(
        default="I specialize in transforming complex business requirements into elegant, efficient solutions that drive measurable results. With a strong foundation in both engineering and design principles, I bridge the gap between technical implementation and user experience."
    )
    profile_image = models.ImageField(
        upload_to='profile/', 
        blank=True, 
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp'])
        ],
        help_text="Upload a professional profile picture. Recommended size: 400x400px. Max file size: 5MB."
    )
    years_experience = models.PositiveIntegerField(default=5)
    projects_delivered = models.PositiveIntegerField(default=50)
    happy_clients = models.PositiveIntegerField(default=30)
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    upwork_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"
