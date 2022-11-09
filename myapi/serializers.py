from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Transaction, Categories, Organizations


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "__all__"
        )


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            "__all__"
        )


class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = (
            "__all__"
        )


class OrganizationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organizations
        fields = (
            "__all__"
        )
