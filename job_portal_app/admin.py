from django.contrib import admin
from .models import JobCategory, Job, Applicant

@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location', 'employment_type', 'experience_level')
    list_filter = ('category', 'location', 'employment_type', 'experience_level')
    search_fields = ('title', 'description', 'about_role', 'key_responsibilities')
    ordering = ('-created_at',)
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'category', 'location','active', 'employment_type', 'experience_level')
        }),
        ('Job Details', {
            'fields': ('about_role', 'key_responsibilities', 'required_skills', 'good_to_have', 'what_we_offer')
        }),
        ('Application Process', {
            'fields': ('how_to_apply',)
        }),
    )

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'job', 'gender', 'available', 'created_at')
    list_filter = ('job', 'gender', 'available','disability', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'gender')
        }),
        ('Application Details', {
            'fields': ('job', 'resume', 'cover_letter', 'linkedin', 'disability_detail','disability','available')
        }),
        ('Additional Information', {
            'fields': ('created_at',)
        }),
    )
