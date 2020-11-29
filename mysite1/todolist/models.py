from django.db import models


class Diary(models.Model):
    subject=models.CharField(max_length=100)
    content=models.TextField()
    create_date=models.DateTimeField()

    def __str__(self):
        return self.subject

class Comment(models.Model):
    diary=models.ForeignKey(Diary, on_delete=models.CASCADE)
    content=models.TextField()
    create_date=models.DateTimeField()

