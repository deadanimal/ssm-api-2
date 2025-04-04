from datetime import datetime, timedelta

from django.conf import settings
from django.conf.urls import include, url
from django.contrib.gis import admin

from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from users.views import (
    MyTokenObtainPairView
)

class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass

router = NestedDefaultRouter()

# Carts app

from carts.views import (
    CartViewSet
)

carts_router = router.register(
    'carts', CartViewSet
)

# Entities app

from entities.views import (
    EntityViewSet
)

entities_router = router.register(
    'entities', EntityViewSet
)

# Organisations app

from organisations.views import (
    OrganisationViewSet
)

organisations_router = router.register(
    'organisations', OrganisationViewSet
)


# Products app

from products.views import (
    ProductViewSet
)

products_router = router.register(
    'products', ProductViewSet
)

# Services app

from services.views import (
    ServiceViewSet
)

services_router = router.register(
    'services', ServiceViewSet
)

# Tickets app

from tickets.views import (
    TicketTopicViewSet,
    TicketSubjectViewSet,
    TicketViewSet,
    TicketCBIDViewSet,
    TicketInvestigationViewSet
)

tickets_router = router.register(
    'tickets', TicketViewSet
)


# Transactions app

from transactions.views import (
    TransactionViewSet,
)

transactions_router = router.register(
    'transactions', TransactionViewSet
)
# Users app

from users.views import (
    CustomUserViewSet
)

users_router = router.register(
    'users', CustomUserViewSet
)

urlpatterns = [
    url(r'v1/', include(router.urls)),
    url(r'auth/', include('rest_auth.urls')),
    url(r'auth/registration/', include('rest_auth.registration.urls')),

    url('auth/obtain/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    url('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url('auth/verify/', TokenVerifyView.as_view(), name='token_verify')
]