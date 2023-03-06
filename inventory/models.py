from django.db import models

class TrackerDevice(models.Model):
    model_number = models.CharField(max_length=255)
    vendor = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    imei = models.CharField(max_length=255)

    def __str__(self):
        return self.model_number

class Sim(models.Model):
    MSISDN = models.CharField(max_length=50)
    ICC_ID = models.CharField(max_length=50)
    OPERATOR_CHOICES = [
        ('zong', 'Zong'),
        ('ufone', 'Ufone'),
        ('warid', 'Warid'),
        ('mobilink', 'Mobilink'),
        ('telenor', 'Telenor'),
    ]
    OPERATOR = models.CharField(max_length=50, choices=OPERATOR_CHOICES)
    PACKAGE = models.CharField(max_length=50)

    def __str__(self):
        return self.MSISDN
