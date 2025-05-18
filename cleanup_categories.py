import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job_portal.settings')
django.setup()

from job_portal_app.models import JobCategory, Job

def cleanup_categories():
    # Get all categories
    categories = JobCategory.objects.all()
    
    # Dictionary to store unique categories
    unique_categories = {}
    
    # First pass: collect all unique category names
    for category in categories:
        if category.name not in unique_categories:
            unique_categories[category.name] = category
        else:
            # If we find a duplicate, move all jobs to the first category
            old_category = unique_categories[category.name]
            jobs = Job.objects.filter(category=category)
            for job in jobs:
                job.category = old_category
                job.save()
            # Delete the duplicate category
            category.delete()
            print(f"Merged duplicate category: {category.name}")

if __name__ == "__main__":
    print("Cleaning up duplicate categories...")
    cleanup_categories()
    print("Cleanup complete!") 