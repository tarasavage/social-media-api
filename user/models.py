from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import CheckConstraint, Q
from django.utils import timezone


class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    picture = models.ImageField(null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r"^\d+$",
                message="Phone number must contain only digits.",
                code="invalid_phone_number",
            )
        ],
    )

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(
                    date_of_birth__lte=(
                        timezone.now().date() - timezone.timedelta(days=365.25 * 12)
                    )
                ),
                name="age_constraint",
            )
        ]
