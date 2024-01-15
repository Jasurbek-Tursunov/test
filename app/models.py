from django.db import models
# from django.contrib.postgres.fields import ArrayField


class Question(models.Model):
    text = models.CharField(max_length=1500)
    # answers = ArrayField(models.TextField())

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    text = models.CharField(max_length=1000)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

