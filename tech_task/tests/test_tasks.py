from django.test import TestCase
from unittest.mock import patch, Mock
from users.models import User, Address, CreditCard
from users.tasks import fetch_users, fetch_addresses, fetch_credit_cards


class FetchDataTests(TestCase):

    @patch("users.tasks.requests.get")
    def test_fetch_users_creates_users(self, mock_get):
        mocked_data = [
            {
                "id": 1,
                "name": "John Doe",
                "username": "johndoe",
                "email": "john@example.com",
                "phone": "123-456-7890 x123",
                "website": "example.com"
            }
        ]
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = mocked_data

        fetch_users()

        user = User.objects.filter(username="johndoe").first()
        self.assertIsNotNone(user)
        self.assertEqual(user.email, "john@example.com")
        self.assertEqual(user.phone, "123-456-7890")

    @patch("users.tasks.requests.get")
    def test_fetch_addresses_creates_address(self, mock_get):
        user = User.objects.create(username="johndoe", name="John Doe", email="john@example.com")

        fake_address = [{
            "street": "Main Street",
            "city": "Testville",
            "zipcode": "12345"
        }]
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = {"data": fake_address}

        fetch_addresses()

        address = Address.objects.filter(user=user).first()
        self.assertIsNotNone(address)
        self.assertEqual(address.city, "Testville")
        self.assertEqual(address.street, "Main Street")

    @patch("users.tasks.requests.get")
    def test_fetch_credit_cards_creates_card(self, mock_get):
        user = User.objects.create(username="johndoe", name="John Doe", email="john@example.com")

        fake_card = [{
            "type": "Visa",
            "number": "4111111111111111",
            "expiration": "12/2030",
            "owner": "John Doe"
        }]
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = {"data": fake_card}

        fetch_credit_cards()

        card = CreditCard.objects.filter(user=user).first()
        self.assertIsNotNone(card)
        self.assertEqual(card.card_type, "Visa")
        self.assertEqual(card.card_number, "4111111111111111")
        self.assertEqual(card.owner_name, "John Doe")
        self.assertEqual(card.expiration_date, "12/2030")