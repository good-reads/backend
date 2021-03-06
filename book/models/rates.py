from django.db import models
from django.core.validators import (
    MinValueValidator, MaxValueValidator,
)

# from .books import Book
from user.models import Account


class Rate(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Account, to_field='id', on_delete=models.CASCADE)
    book_isbn = models.ForeignKey('Book', to_field='isbn', on_delete=models.CASCADE)
    score = models.FloatField(default=5., validators=[MinValueValidator(0.), MaxValueValidator(5.)])

    class Meta:
        db_table = 'rates'

    @classmethod
    def calculate_rate(cls, book):
        return cls.objects.filter(book=book).saggregate(
            models.Avg('score')
        )['score__avg'] or 0

    # @classmethod
    # def create(cls, params):
    #     rate = cls.objects.create(**params)
    #     rate.book.rate = cls.calculate_rate(rate.book)
    #     rate.book.save()
    #     rate.rate_avg = rate.book.rate
    #     return rate

    # def update_score(self, params):
    #     self.score = params['score']
    #     self.save(update_fields=['score'])
    #     self.book.rate = self.calculate_rate(self.book)
    #     self.book.save(update_fields=['rate'])
    #     self.rate_avg = self.book.rate
    #     return self

    # def cancel(self):
    #     self.delete()
    #     self.book.rate = self.calculate_rate(self.book)
    #     self.book.save(update_fields=['rate'])
    #     return {
    #         'rate_avg': self.book.rate
    #     }
