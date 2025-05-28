from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='address')
    street = models.CharField(max_length=255)
    suite = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.street}, {self.city}"


class CreditCard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="credit_card")
    card_type = models.CharField(max_length=50)  # Тип картки (Visa, MasterCard, JCB тощо)
    card_number = models.CharField(max_length=20)  # Номер картки
    expiration_date = models.CharField(max_length=7)  # MM/YY
    owner_name = models.CharField(max_length=255)  # Ім'я власника

    def __str__(self):
        return f"{self.card_type} **** {self.card_number[-4:]}"

