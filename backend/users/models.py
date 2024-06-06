from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
class User(models.Model):
    username = models.CharField(max_length=150, unique=True, null=False)
    password = models.CharField(max_length=128, null=False)
    email = models.EmailField(unique=True, null=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    mobile_number = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        blank=True,
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
        )]
    )

    def __str__(self):
        return self.username
    


class UserProfile(models.Model):
        
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        bio = models.TextField(blank=True, null=True)
        profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
        phone_number = models.CharField(max_length=20, blank=True, null=True)
        address = models.CharField(max_length=255, blank=True, null=True)
        linkedin_url = models.URLField(blank=True, null=True)
        github_url = models.URLField(blank=True, null=True)
        website_url = models.URLField(blank=True, null=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.user.username
