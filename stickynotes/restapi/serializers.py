from rest_framework import serializers
from restapi.models import Note
class NoteSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    note_title = serializers.CharField()
    note_body = serializers.CharField()
    note_tags = serializers.JSONField()
    def create(self, validated_data):
        return Note.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.note_title = validated_data.get('note_title',instance.note_title)
        instance.note_body = validated_data.get('note_body',instance.note_body)
        instance.note_tags = validated_data.get('note_tags',instance.note_tags)
        instance.save()
        return instance