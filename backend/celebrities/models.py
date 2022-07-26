import os
import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


User = get_user_model()


def get_photo_upload_path(instance, full_name=None):
    return os.path.join(
        "celeb/",
        datetime.datetime.now().strftime("%Y/%m/%d"),
        full_name,
    )


class Celebrity(models.Model):
    full_name = models.CharField(_("full name"), max_length=100)
    # avatar = models.ImageField(_("avatar"), upload_to="celeb/avatar", null=True, blank=True)
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    update = models.DateTimeField(_("Update"), auto_now=True)
    created_by = models.ForeignKey(
        User, verbose_name=_("Created By"), on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Celebrity")
        verbose_name_plural = _("Celebrities")

    @property
    def num_of_photos(self):
        return Photo.objects.filter(celebrity=self.pk).count()

    def __str__(self):
        return self.full_name


class Photo(models.Model):
    photo = models.ImageField(
        _("Photo"), upload_to=get_photo_upload_path, null=True, blank=True
    )
    celebrity = models.ForeignKey(
        Celebrity, verbose_name=_("Celebrity"), on_delete=models.CASCADE
    )
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Celeb Photo")
        verbose_name_plural = _("Celeb Photos")

    @property
    def ratings(self):
        return Rating.objects.filter(photo=self.pk).count()

    def __str__(self):
        return self.celebrity.full_name


class Rating(models.Model):
    RATE_CHOICES = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    stars = models.IntegerField(choices=RATE_CHOICES)
    comment = models.TextField(_("comment"))
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    update = models.DateTimeField(_("Update"), auto_now=True)
    created_by = models.ForeignKey(
        User, verbose_name=_("Created By"), on_delete=models.CASCADE
    )
    photo = models.ForeignKey(Photo, verbose_name=_("Photo"), on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.photo} - {self.stars}"
