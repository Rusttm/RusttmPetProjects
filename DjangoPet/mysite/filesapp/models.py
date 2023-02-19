from django.db import models
import os
# Create your models here.
class FileUploaded(models.Model):
    """ model for uploaded image files """
    upload = models.ImageField(upload_to="uploadedfiles/")
    date = models.DateTimeField(auto_now_add=True)
    def filename(self):
        return os.path.basename(self.upload.name)
    class Meta:
        ordering=['-date']

    def __str__(self):
        return str(self.date) + str(self.upload)


class DocumentUploaded(models.Model):
    """ model for uploaded document files """
    upload = models.FileField(upload_to='documents/')
    date = models.DateTimeField(auto_now_add=True)

    def filename(self):
        return os.path.basename(self.upload.name)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.date) + str(self.upload)