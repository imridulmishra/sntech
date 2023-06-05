"""
URL configuration for Snoffle_tech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import email_page,home_page,service_page,about_page
from career.views import career_page,jobDetailsPage,job_apply_form
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page,name='home'),
    path('contact/',email_page,name='email_page'),
    path('service/',service_page,name='service'),
    path('about/',about_page,name='about'),
    path('career/',career_page,name='career'),
    path('career/job/<int:job_id>',jobDetailsPage,name='jobdetail'),
    path('career/job/jobapply/<int:job_id>',job_apply_form,name='jobapply'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
