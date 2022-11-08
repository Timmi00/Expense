from rest_framework import serializers

from .models import Transaction, Categories, Organizations


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
