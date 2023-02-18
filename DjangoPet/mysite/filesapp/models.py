from django.db import models

# Create your models here.
class FileUploaded(models.Model):
    upload = models.ImageField(upload_to="uploadedfiles/")
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-date']

    def __str__(self):
        return str(self.date) + str(self.upload)