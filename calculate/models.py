from django.db import models
from django.core.validators import FileExtensionValidator
import os

# Create your models here.
class FileUpload(models.Model):
    upload = models.FileField(
        upload_to='file/%Y/%m/%d',
        validators=[FileExtensionValidator(['csv', 'pdf', 'txt'])]
        )

    """ -----file_name属性として作成----- """
    def file_name(self):
        path = os.path.basename(self.upload.name)  # ファイル名のみ抽出
        return path