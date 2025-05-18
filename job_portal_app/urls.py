from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobCategoryViewSet, JobViewSet, ApplicantViewSet

router = DefaultRouter()
router.register(r'categories', JobCategoryViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'applicants', ApplicantViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 