from django.db import models

# Create your models here.
class Book(models.Model):
    class Book(models.Model):
        title = models.CharField('书名', unique=True, max_length=50)
        pub = models.CharField('出版社', max_length=100)
        price = models.DecimalField('定价', max_digits=5, decimal_places=2)
        market_price = models.DecimalField('零售价', max_digits=5, decimal_places=2)

        def __str__(self):
            return '<%s %s %s %s>' % (self.title, self.pub, self.price, self.market_price)