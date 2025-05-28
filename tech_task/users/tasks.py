import logging
import requests
from celery import shared_task
from users.models import Address, CreditCard, User

logger = logging.getLogger(__name__)

@shared_task
def fetch_users():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    if response.status_code == 200:
        users_data = response.json()
        for user_data in users_data:
            phone_number = user_data["phone"].split(" x")[0]
            user, created = User.objects.update_or_create(
                user_id=user_data["id"],
                defaults={
                    "name": user_data["name"],
                    "username": user_data["username"],
                    "email": user_data["email"],
                    "phone": phone_number[:50],
                    "website": user_data["website"]
                }
            )
            if created:
                logger.info(f"Created new user: {user.username}")
            else:
                logger.info(f"Updated user: {user.username}")

@shared_task
def fetch_addresses():
    response = requests.get('https://fakerapi.it/api/v2/addresses?_quantity=10')
    if response.status_code == 200:
        addresses_data = response.json()["data"]
        users = list(User.objects.all())

        for address_data in addresses_data:
            user = users.pop() if users else None
            if user:
                Address.objects.update_or_create(
                    user=user,
                    defaults={
                        "street": address_data["street"],
                        "city": address_data["city"],
                        "zipcode": address_data["zipcode"]
                    }
                )
                logger.info(f"Created address for {user.username}")
            else:
                logger.warning("Failed to create address - no available users!")

@shared_task
def fetch_credit_cards():
    response = requests.get('https://fakerapi.it/api/v2/creditCards?_quantity=10')
    if response.status_code == 200:
        cards_data = response.json()["data"]
        users = list(User.objects.all())

        for card_data in cards_data:
            user = users.pop() if users else None
            if user:
                logger.info(f"Assigning card {card_data['number']} to {user.username}")
                CreditCard.objects.update_or_create(
                    user=user,
                    defaults={
                        "card_type": card_data["type"],
                        "card_number": card_data["number"],
                        "expiration_date": card_data["expiration"],
                        "owner_name": card_data["owner"]
                    }
                )
                logger.info(f"Created credit card for {user.username}")
            else:
                logger.warning("Failed to create credit card - no available users!")
