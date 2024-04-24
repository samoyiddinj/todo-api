from rest_framework import serializers
from .models import Todo, Movie
import phonenumbers
import re


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['task', 'completed', 'timestamp', 'updated', 'user']


def is_rating(value):
    if value < 1 or value > 10:
        raise serializers.ValidationError("rating 1 va 10 orasida bo'lishi kerak")


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def validate_phone(self, value):

        try:
            parsed_phone = phonenumbers.parse(value, "UZ")
            if not phonenumbers.is_valid_number(parsed_phone):
                raise serializers.ValidationError("Telefon raqam noto'g'ri")
        except phonenumbers.phonenumberutil.NumberParseException:
            raise serializers.ValidationError("Noto'g'ri telefon raqami formati")

        return value

    def validate(self, attrs):
        if attrs['uzb_gross'] > attrs['world_gross']:
            raise serializers.ValidationError("Uzb gross kichkina bo'lishi kerak")
        return attrs
