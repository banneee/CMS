from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.bio[:20]}'

class Grade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.CharField(max_length=100, default='100', null=True)
    grade = models.CharField(max_length=2, default='100', null=True)

    def __str__(self):
        return f'{self.user.username} - {self.course}: {self.grade}'

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default='100', null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.username} - {self.amount} on {self.date}'
