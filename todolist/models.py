
from django.db import models



    
class UserData(models.Model):
    user_nam=models.CharField(max_length=200)
    pass_wd = models.CharField(max_length=200)
    taskdata=models.TextField(null=True)
    def __str__(self):
        return "%s %s %s" % (self.user_nam,self.pass_wd,self.taskdata)
# Create your models here.
