from django.urls import path
from todo_app.views import add_view, detail_view, update_view, delete_view, confirm_delete_view, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', add_view, name='add_task'),
    path('task/<int:pk>/', detail_view, name='detailed_task'),
    path('task/', IndexView.as_view(), name='task_no_pk'),
    path('task/<int:pk>/update/', update_view, name='update_task'),
    path('task/<int:pk>/delete', delete_view, name='delete_task'),
    path('task/<int:pk>/confirm-delete', confirm_delete_view, name='confirm_delete_task')
]
