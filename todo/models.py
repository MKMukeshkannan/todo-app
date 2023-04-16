from django.db import models
from user.models import User

class todoDB(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    taskDesc = models.CharField(max_length=200)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.taskDesc[:7] + self.user.first_name
    