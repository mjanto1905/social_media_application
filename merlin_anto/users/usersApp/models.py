

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
        #show how we want it to be displayed

    def save(self):
        super().save()

        img = Image.open(self.image.path)  # Open image

        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)  # Resize image
            img.save(self.image.path)  # Save it again and override the larger image


from django.utils import timezone # Import timezone for DateTimeField
 # Import User model

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # If a user created the post is deleted, posts are deleted as well.ß

    # __str__() method returns how the Post is printed
    def __str__(self):
        return self.title

