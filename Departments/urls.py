from django.urls import path

from .views import DepartmentListView, DepartmentDetailView

urlpatterns = [
    path('', DepartmentListView.as_view()),
    path('<int:pk>/', DepartmentDetailView.as_view())
]
