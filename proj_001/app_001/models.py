from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=200)


class Album(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=200)
    release_date = models.DateField(blank=True, null=True)


class Playlist(models.Model):
    name = models.CharField(max_length=200)


class Song(models.Model):
    name = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    playlist = models.ManyToManyField(Playlist)



# author = Author(name='John', date_created='2020-10-10')
# author.save()
# song = Song(title='1', author=author)
# song.save()
# song = Song.objects.filter(author=author)