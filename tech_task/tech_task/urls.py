from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, AddressViewSet, CreditCardViewSet, get_users, get_addresses, get_credit_cards

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'creditcards', CreditCardViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(router.urls)),
    path('get_users/', get_users),
    path('get_addresses/', get_addresses),
    path('get_credit_cards/', get_credit_cards),
]
