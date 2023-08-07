from django.contrib import admin
from django.urls import path, include
from .views import FeedbackForm


urlpatterns = [
    path('', FeedbackForm.send_email  ),

]
