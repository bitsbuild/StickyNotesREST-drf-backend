from django.db import models
import uuid
class Note(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    note_title = models.CharField(max_length=70)
    note_body = models.CharField(max_length=210)
    note_tags = models.JSONField(default=list)
    