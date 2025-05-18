from rest_framework import serializers
from .models import JobCategory, Job, Applicant

class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = '__all__'
        

class JobSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    location_display = serializers.CharField(source='get_location_display', read_only=True)
    employment_type_display = serializers.CharField(source='get_employment_type_display', read_only=True)
    experience_level_display = serializers.CharField(source='get_experience_level_display', read_only=True)
    
    class Meta:
        model = Job
        fields = '__all__'

class ApplicantSerializer(serializers.ModelSerializer):
    job_title = serializers.CharField(source='job.title', read_only=True)
    gender_display = serializers.CharField(source='get_gender_display', read_only=True)
    available_display = serializers.CharField(source='get_available_display', read_only=True)
    
    class Meta:
        model = Applicant
        fields = '__all__' 