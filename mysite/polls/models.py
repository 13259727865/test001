import datetime
import hashlib

import uuid as uuid
from django.db import models

# Create your models here.
from django.utils import timezone


class User(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=20)
    password = models.CharField(verbose_name="密码", max_length=100)
    phone = models.CharField(verbose_name="手机号", max_length=20)
    create_time = models.DateTimeField(auto_now=True,blank=True)

    def save(self, *args, **kwargs):
        self.password = hashlib.sha1(self.password.encode("utf-8")).hexdigest()
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.username}-{self.phone}"


class Address(models.Model):
    userid = models.ForeignKey("User", on_delete=models.CASCADE)
    address = models.CharField(verbose_name="收货地址", max_length=50)
    phone = models.CharField(verbose_name="收货电话", max_length=20)
    name = models.CharField(verbose_name="收货姓名", max_length=20)
    def __str__(self):
        return f"{self.userid}-{self.address}-{self.name}"
