from rest_framework import serializers
from .models import ItemModel, ItemReveiw


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = ('__all__')

    def validate_user(self, user):
        if (user is None):
            raise serializers.ValidationError(
                "U have to be authenticated to post , please log in.")
        return user


class ItemReveiwSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemReveiw
        fields = ('__all__')
