from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=20, help_text="first name")
    last_name = models.CharField(max_length=20, help_text="last name")
    email = models.EmailField(help_text="email address")
    phone = models.CharField(max_length=15, help_text="phone number")

    def __str__(self):
        return self.first_name


class Story(models.Model):
    # Title is necessary for story
    story = models.TextField(help_text="story")
    title = models.CharField(max_length=60, help_text="Title of story")
    photo = models.FileField(help_text="file example photo or video", blank= True)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    story_date = models.DateField(verbose_name="data story was recorded")
    type = models.CharField(max_length=50, help_text="type of story")

    def __str__(self):
        return self.story


class Comment(models.Model):
    comment = models.TextField(help_text="comment given to the story")
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    comment_date = models.DateField(verbose_name="date comment was given")

    def __str__(self):
        return self.comment
