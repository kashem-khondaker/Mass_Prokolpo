from django.db import models
from accounts.models import CustomUser as User
from mess.models import Mess

# Create your models here.


class MessPost(models.Model):
    mess = models.ForeignKey(Mess, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='mess_posts/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_vacancy = models.BooleanField(default=False)
    vacancy_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.title} - {self.mess.name}"


class Comment(models.Model):
    post = models.ForeignKey(MessPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"

