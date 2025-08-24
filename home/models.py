# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Biodata(models.Model):

    #__Biodata_FIELDS__
    noreg = models.CharField(max_length=255, null=True, blank=True)
    nama = models.CharField(max_length=255, null=True, blank=True)
    jk = models.CharField(max_length=255, null=True, blank=True)
    alamat = models.CharField(max_length=255, null=True, blank=True)
    tanggal_lahir = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status_pernikahan = models.CharField(max_length=255, null=True, blank=True)
    segmen = models.CharField(max_length=255, null=True, blank=True)
    tanggal_masuk = models.DateTimeField(blank=True, null=True, default=timezone.now)
    keterangan = models.CharField(max_length=255, null=True, blank=True)
    tanggal_update = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Biodata_FIELDS__END

    class Meta:
        verbose_name        = _("Biodata")
        verbose_name_plural = _("Biodata")


class Bina(models.Model):

    #__Bina_FIELDS__
    noreg = models.ForeignKey(biodata, on_delete=models.CASCADE)
    keterangan = models.CharField(max_length=255, null=True, blank=True)
    tanggal_update = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Bina_FIELDS__END

    class Meta:
        verbose_name        = _("Bina")
        verbose_name_plural = _("Bina")


class Kelulusan(models.Model):

    #__Kelulusan_FIELDS__
    noreg = models.ForeignKey(biodata, on_delete=models.CASCADE)
    jenjang = models.CharField(max_length=255, null=True, blank=True)
    tanggal_lulus = models.DateTimeField(blank=True, null=True, default=timezone.now)
    keterangan = models.CharField(max_length=255, null=True, blank=True)
    tanggal_update = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Kelulusan_FIELDS__END

    class Meta:
        verbose_name        = _("Kelulusan")
        verbose_name_plural = _("Kelulusan")


class Keuangan(models.Model):

    #__Keuangan_FIELDS__
    noreg = models.ForeignKey(biodata, on_delete=models.CASCADE)
    wi = models.BooleanField()
    wz = models.BooleanField()
    infis = models.BooleanField()
    st = models.BooleanField()
    keterangan = models.CharField(max_length=255, null=True, blank=True)
    tanggal_update = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Keuangan_FIELDS__END

    class Meta:
        verbose_name        = _("Keuangan")
        verbose_name_plural = _("Keuangan")


class Arisan(models.Model):

    #__Arisan_FIELDS__
    noreg = models.ForeignKey(biodata, on_delete=models.CASCADE)
    jenis_setoran = models.CharField(max_length=255, null=True, blank=True)
    nilai_setoran = models.IntegerField(null=True, blank=True)
    tanggal_setor = models.DateTimeField(blank=True, null=True, default=timezone.now)
    keterangan = models.CharField(max_length=255, null=True, blank=True)
    tanggal_update = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Arisan_FIELDS__END

    class Meta:
        verbose_name        = _("Arisan")
        verbose_name_plural = _("Arisan")



#__MODELS__END
