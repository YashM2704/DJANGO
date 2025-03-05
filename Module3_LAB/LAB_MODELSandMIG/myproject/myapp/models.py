from django.db import models  # Ensure this line is present

class Drinks(models.Model):
    drink_name = models.CharField(max_length=200)  # Updated field name
    price = models.IntegerField()

    def __str__(self):
        return self.drink_name  # Ensure this method returns the updated field
