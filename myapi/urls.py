from django.urls import include, path
from rest_framework import routers
from . import views
from .views import expired_obtain_auth_token

router = routers.DefaultRouter()
router.register(
    r'transaction',
    views.TransactionViewSet
)
router.register(
    r'categories',
    views.CategoriesViewSet
)
router.register(
    r'organizations',
    views.OrganizationsViewSet
)
router.register(
    r'user',
    views.UserViewSet
)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', expired_obtain_auth_token)
]
