from rest_framework import viewsets

from .serializers import TransactionSerializer, CategoriesSerializer, OrganizationsSerializer
from .models import Transaction, Categories, Organizations


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by('amount')
    serializer_class = TransactionSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all().order_by('category_name')
    serializer_class = CategoriesSerializer


class OrganizationsViewSet(viewsets.ModelViewSet):
    queryset = Organizations.objects.all().order_by('organization_name')
    serializer_class = OrganizationsSerializer
