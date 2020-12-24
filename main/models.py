from django.db import models


class StoriesCategory(models.Model):
    story_category = models.CharField(max_length=200)
    story_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.story_category


class StoriesSeries(models.Model):
    story_series = models.CharField(max_length=200)
    story_category = models.ForeignKey(StoriesCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    story_summary = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Series"

    def __str__(self):
        return self.story_series


class Stories(models.Model):
    story_title = models.CharField(max_length=200)
    story_intro = models.CharField(max_length=200, default="")
    story_description = models.TextField()
    story_published = models.DateTimeField("Date Published")
    data = models.TextField(default="")

    story_series = models.ForeignKey(StoriesSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
    story_slug = models.CharField(max_length=200, default=1)

    def __str__(self):
        return self.story_title


class Dataa(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(default="")

    def __str__(self):
        return self.title


class telling(models.Model):
    title = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title



