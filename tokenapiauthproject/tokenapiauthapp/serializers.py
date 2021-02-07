from rest_framework import serializers
from .models import CountryRecord, CityRecord, Account


class CountryRecordSerializer(serializers.ModelSerializer):
    cities = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = CountryRecord
        fields = ('name', 'cities')


class CityRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityRecord
        fields = ('name', 'pincode', 'country')

    def create(self, validated_data):
        country = CountryRecord.objects.filter(
            name=validated_data['country']
        )[0]

        if not country:
            country = CountryRecord.objects.create(
                name=validated_data['country']
            )

        return CityRecord.objects.create(
            name=validated_data['name'],
            pincode=validated_data['pincode'],
            country=country
        )

    def update(self, instance, validated_data):
        country = CountryRecord.objects.filter(
            name=validated_data['country']
        )[0]

        instance.name = validated_data['name']
        instance.pincode = validated_data['pincode']
        instance.country = country
        instance.save()
        return instance


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Account(
                    email=self.validated_data['email'],
                    username=self.validated_data['username'],
            )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'error': 'Passwords are not matching!'})

        account.set_password(password)
        account.save()
        return account