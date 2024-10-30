from django.urls import path
from .views import chat_view, log_view, reset_log_view, deletion_complete_view 

urlpatterns = [
    path('', chat_view, name='chat'),
    path('log/', log_view, name='log'),
    path('reset_log/', reset_log_view, name='reset_log'), 
    path('deletion_complete/', deletion_complete_view, name='deletion_complete'), 
]