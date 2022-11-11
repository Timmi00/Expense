from datetime import datetime, timedelta
import pytz
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import TransactionSerializer, CategoriesSerializer, OrganizationsSerializer, UserSerializer
from .models import Transaction, Categories, Organizations


class ExpiredTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        user, token = super(ExpiredTokenAuthentication, self).authenticate_credentials(key=key)
        utc_now = datetime.utcnow()
        utc_now = utc_now.replace(tzinfo=pytz.utc)
        if token.created + timedelta(minutes=14440) < utc_now:
            raise AuthenticationFailed('token has expired')
        return user, token


class ExpiredObtainAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        try:
            token = Token.objects.get(user=user)
        except Token.DoesNotExist:
            pass
        else:
            token.delete()
        token = Token(
            user=user,
        )
        token.save()
        return Response({'token': token.key})


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by('amount')
    serializer_class = TransactionSerializer
    authentication_classes = [ExpiredTokenAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'amount', 'my_user', 'date_of_payment']
    # permission_classes = [IsAuthenticatedOrReadOnly]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all().order_by('category_name')
    serializer_class = CategoriesSerializer


class OrganizationsViewSet(viewsets.ModelViewSet):
    queryset = Organizations.objects.all().order_by('organization_name')
    serializer_class = OrganizationsSerializer


expired_obtain_auth_token = ExpiredObtainAuthToken.as_view()
