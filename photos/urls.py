from . import views
from .views import BasicUploadView, ProgressBarUploadView, DragAndDropUploadView
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('clear/', views.clear_database, name='clear_database'),
    path('photos/basic-upload/', BasicUploadView.as_view(), name='basic_upload'),
    path('photos/progress-bar-upload/', ProgressBarUploadView.as_view(), name='progress_bar_upload'),
    path('photos/drag-and-drop-upload/', DragAndDropUploadView.as_view(), name='drag_and_drop_upload'),

]