from django.urls import path

from .api_view import (CategoryAPIView, CustomersAPIView,
                       SmartphoneListAPIView, SmartphoneDetailAPIView,
                       NotebookListAPIView, NotebookDetailAPIView)


urlpatterns = [
    path('categories/', CategoryAPIView.as_view(), name = 'categories'),
    path('customers/', CustomersAPIView.as_view(), name = 'customers'),
    path('smartphones/', SmartphoneListAPIView.as_view(), name = 'smartphones_list'),
    path('smartphones/<str:pk>/', SmartphoneDetailAPIView.as_view(), name = 'smartphone_detail'),
    path('notebooks/', NotebookListAPIView.as_view(), name = 'notebooks_list'),
    path('notebooks/<str:pk>/', NotebookDetailAPIView.as_view(), name = 'notebook_detail')
]
