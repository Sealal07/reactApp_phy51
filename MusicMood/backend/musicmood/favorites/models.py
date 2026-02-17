from django.db import models

class FavoriteTrack(models.Model):
    user_id = models.CharField(max_length=255)
    track_id = models.CharField(max_length=255)

    name_track = models.CharField(max_length=512)
    artist_name = models.CharField(max_length=255)
    audio_url = models.URLField()
    album_image = models.URLField()

    class Meta:
        verbose_name = 'Избранный трек'
        verbose_name_plural = 'Избранные треки'
    def __str__(self):
        return self.name_track 
