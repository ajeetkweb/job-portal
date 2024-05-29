from django.db import models
from users.models import User
from companies.models import Company, JobListing

# Create your models here.


class JobApplication(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[
        ('APPLIED', 'Applied'),
        ('INTERVIEW', 'Interview'),
        ('OFFER', 'Offer'),
        ('REJECTED', 'Rejected'),
    ], default='APPLIED')

    def __str__(self):
        return f"{self.applicant.username} - {self.job_listing.job_title}"