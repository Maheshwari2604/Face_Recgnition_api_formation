from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100,null=False,unique=True,primary_key=True)
    #name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    img = models.ManyToManyField('Image',related_name='img')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Image(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    user_img = models.ImageField(upload_to='user_images/')

    def __str__(self):
        return '%s %s' % (self.user,self.user_img)


