from django.db import models


class Person(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    full_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=100)
    relationship_status = models.CharField(max_length=255)
    birthday = models.DateField()
    hometown = models.CharField(max_length=255)
    current_location = models.CharField(max_length=255)
    facebook_profile = models.URLField()
    picture = models.ImageField()

    class Meta:
        ordering = ('created',)


class Conversation(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    person1 = models.ForeignKey(Person, on_delete=models.CASCADE, related_name=u'+')
    person2 = models.ForeignKey(Person, on_delete=models.CASCADE, related_name=u'+')

    class Meta:
        unique_together = (('person1', 'person2'),)
        ordering = ('created',)


class Message(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    body = models.CharField(max_length=255)

    class Meta:
        ordering = ('created',)


