from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=200)
    test_field = models.TextField(blank=True)

    def __str__(self):
        return str(self.name)


class Album(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=200)
    release_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.name) + str(self.release_date) + str(self.author)


class Playlist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Song(models.Model):
    name = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    playlist = models.ManyToManyField(Playlist)

    def __str__(self):
        return str(self.name) + str(self.album)



# author = Author(name='John', date_created='2020-10-10')
# author.save()
# song = Song(title='1', author=author)
# song.save()
# song = Song.objects.filter(author=author)