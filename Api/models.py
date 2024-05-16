from django.db import models


SIZE_CHOICES = [
    ('ST', 'Studio'),
    ('1BR', '1 bedroom'),
    ('2BR', '2 bedrooms'),
    ('3BR', '3 bedrooms'),
    ('MBR', '3+ bedrooms'),]
TYPE_CHOICES = [
    ('H', 'house'),
    ('APT', 'apartment'),]

class House(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', related_name='houses', on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True, default='')
    size = models.CharField(choices=SIZE_CHOICES, default='1BR', max_length=100)
    type = models.CharField(choices=TYPE_CHOICES, default='APT', max_length=100)
    price = models.PositiveIntegerField(default=0)
    sharing = models.BooleanField(default=False)
    text = models.TextField(default='')
    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.text
    
  



# Create your models here.
