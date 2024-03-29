from django.contrib import admin
from django.urls import path, include
from .views import ClassroomInsert

urlpatterns = [
    # path('classrooms/', admin.site.urls, name='classrooms'),
    # path('classrooms/classroom/<int:class_id>/', admin.site.urls, name='classroom'),
    path('classrooms/classroom/post/', ClassroomInsert.as_view(), name='post_classroom'),
    # path('classrooms/classroom/<int:class_id>/update/', admin.site.urls, name='update_classroom'),
    # path('classrooms/classroom/<int:class_id>/delete/', admin.site.urls, name='delete_classroom'),
    # path('classrooms/classroom/<int:class_id>/hours/', admin.site.urls, name='free_periods'),
    # path('classrooms/classroom/<int:class_id>/reservate/', admin.site.urls, name='reservate'),
    # path('classrooms/classroom/<int:class_id>/cancel/', admin.site.urls, name='cancel_reservation'),
]
