import hashlib

from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(verbose_name="用户名",max_length=20)
    password = models.CharField(verbose_name="密码",max_length=20)
    phone = models.IntegerField(verbose_name="手机号",max_length=11)

    def save(self, *args, **kwargs):
        self.password = hashlib.sha1(self.password.encode("utf-8")).hexdigest()
        super(User, self).save(*args, **kwargs)


