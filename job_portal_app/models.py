from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
import uuid

# Create your models here.

class JobCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class Job(models.Model):
    LOCATION_CHOICES = [
        ('remote', 'Remote'),
        ('hybrid', 'Hybrid'),
        ('On-site', 'On-site'),
        
    ]
    
    EMPLOYMENT_TYPE_CHOICES = [
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
        ('contract', 'Contract'),
    ]
    
    EXPERIENCE_LEVEL_CHOICES = [
        ('entry', 'Entry Level'),
        ('mid', 'Mid Level'),
        ('senior', 'Senior Level'),
    ]
    
    job_id = models.CharField(max_length=10, unique=True, blank=True)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE, related_name='jobs')
    location = models.CharField(max_length=20, choices=LOCATION_CHOICES)
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE_CHOICES)
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_LEVEL_CHOICES)
    active = models.BooleanField(default=True)
    about_role = models.TextField()
    key_responsibilities = models.TextField()
    required_skills = models.TextField()
    good_to_have = models.TextField()
    what_we_offer = models.TextField()
    how_to_apply = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.job_id} - {self.title}"

@receiver(pre_save, sender=Job)
def generate_job_id(sender, instance, **kwargs):
    if not instance.job_id:
        instance.job_id = f"JR{uuid.uuid4().hex[:6].upper()}"

class Applicant(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others'),
        ('not_disclose', 'Do not wish to disclose'),
        ('self_describe', 'Prefer to self-describe'),
    ]
    
    AVAILABILITY_CHOICES = [
        ('full_time', 'Full time'),
        ('part_time', 'Part time'),
    ]
    DISABLE = [
        ('Yes','Yes'),
        ('No','No')
    ]
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applicants')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.FileField(upload_to='cover_letters/', null=True, blank=True)
    linkedin = models.URLField(blank=True)
    disability = models.CharField(max_length=20,choices=DISABLE,null=True,blank=True)
    disability_detail = models.TextField(blank=True,null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    available = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.job.title}"
