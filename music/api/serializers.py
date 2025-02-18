from rest_framework import serializers

from .models import Room


class RoomSerializers(serializers.ModelSerializers):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause',
                   'vote_to_skip', 'created_at')
