from django.db import models
from django.urls import reverse
from django.db.models.constraints import UniqueConstraint
from django.db.models.functions import Lower

# Create your models here.

# Example of Model
class	MyModelName(models.Model):
	my_field_name = models.CharField(max_length=20, help_text="Enter field Documentation", verbose_name = 'patata')

	class	Meta:
		ordering = ["-my_field_name"]

	def	get_absolute_url(self):
		return reverse('example-model', args=[str(self.id)])

	def	__str__(self):
		return self.my_field_name

class Artist(models.Model):
    name = models.CharField(max_length=10)


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    #artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True)
    album = models.ForeignKey(Album, on_delete=models.RESTRICT)

# Genre
class	Genre(models.Model):
	name = models.CharField(max_length=200, 
		unique=True, 
		help_text="Enter a book genre")

	class	Meta:
		ordering = ["-name"]
		constraints = [
				UniqueConstraint(
					Lower('name'),
					name="genre_name_lower_unique",
					violation_error_message="Genre already exists"
				),
		]

	def	__str__(self):
		return self.name

	def	get_abosulte_url(self):
		return reverse('genre-detail', args=[str(self.id)])

# Book
#class	Book(models.Model):
#	title = models.CharField(max_length=200, 
#		help_text="Enter the title of book")
#	author = models.
#	summary = models.TextField(max_length=2000, 
#		help_text="Enter a summary of book")
#	isbn = models.
#	genre = models.
#
#	class	Meta:
#		ordering = ["title"]
#
#	def	__str__(self):
#		return self.title
#
#	def	get_abosulte_url(self):
#		return reverse('book-detail', args=[str(self.id)])
