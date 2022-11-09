from django.urls import include, path
from rest_framework import routers
from . import views

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
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
