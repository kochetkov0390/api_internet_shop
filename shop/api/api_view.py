from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                     ListCreateAPIView, RetrieveUpdateAPIView)
from rest_framework.filters import SearchFilter

from .serializers import (CategorySerializer, SmartphoneSerializer, 
                          CustomerSerializer, NotebookSerializer)
from ..models import Category, Smartphone, Notebook, Customer


class CategoryAPIView(ListCreateAPIView, RetrieveUpdateAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    

class SmartphoneListAPIView(ListAPIView):

    serializer_class = SmartphoneSerializer
    queryset = Smartphone.objects.all()
    filter_backends = [SearchFilter]
    search_fields = '__all__'


class SmartphoneDetailAPIView(RetrieveAPIView):

    serializer_class = SmartphoneSerializer
    queryset = Smartphone.objects.all()


class NotebookListAPIView(ListAPIView):

    serializer_class = NotebookSerializer
    queryset = Notebook.objects.all()
    filter_backends = [SearchFilter]
    search_fields = '__all__'


class NotebookDetailAPIView(RetrieveAPIView):

    serializer_class = NotebookSerializer
    queryset = Notebook.objects.all()


class CustomersAPIView(ListAPIView):

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
