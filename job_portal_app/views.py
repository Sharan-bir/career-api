from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.mail import send_mail
from django.conf import settings
from .models import JobCategory, Job, Applicant
from .serializers import JobCategorySerializer, JobSerializer, ApplicantSerializer
from django.db import models

# Create your views here.

class JobCategoryViewSet(viewsets.ModelViewSet):
    queryset = JobCategory.objects.all()
    serializer_class = JobCategorySerializer

    @action(detail=False, methods=['get'])
    def with_counts(self, request):
        categories = JobCategory.objects.annotate(
            job_count=models.Count('jobs', filter=models.Q(jobs__active=True))
        ).order_by('name')
        print(categories)
        data = []
        for category in categories:
            data.append({
                'id': category.id,
                'name': category.name,
                'job_count': category.job_count
            })
        
        return Response(data)

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    
    def get_queryset(self):
        queryset = Job.objects.all()
        category = self.request.query_params.get('category', None)
        category_id = self.request.query_params.get('category_id', None)
        
        if category:
            queryset = queryset.filter(category__name=category,active=True)
        elif category_id:
            queryset = queryset.filter(category_id=category_id,active=True)
        return queryset.filter(active=True)

class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        # Send confirmation email
        applicant = serializer.instance
        job = applicant.job
        
        subject = f'Application Received - {job.title}'
        message = f"""
        Dear {applicant.first_name} {applicant.last_name},
        
        Thank you for applying for the {job.title} position at NetPy. We have received your application and will review it shortly.
        
        Job Details:
        - Position: {job.title}
        - Location: {job.get_location_display()}
        - Employment Type: {job.get_employment_type_display()}
        
        We will contact you soon regarding the next steps in the hiring process.
        
        Best regards,
        NetPy HR Team
        """
        
        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [applicant.email],
                fail_silently=False,
            )
        except Exception as e:
            print(f"Failed to send email: {str(e)}")
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
