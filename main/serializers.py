from rest_framework import serializers
from .models import *


class ProductSerializerModel(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return ProductModel.objects.create(**validated_data)

    class Meta:
        model = ProductModel
        fields = '__all__'


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=6, decimal_places=2)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

    def create(self, validated_data):
        return ProductModel.objects.create(**validated_data)


class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=25)
    product =ProductSerializer()

    def create(self, validated_data):
        product = ProductModel.objects.get_or_create(**dict(validated_data['product']))
        validated_data['product'] = product[0]
        # product=ProductModel(**dict(validated_data['product']))
        # check = ProductModel.objects.filter(title = product.title, price = product.price)
        # print('eto check 0')
        # print(check[0])
        # print(check)
        # if check:
        #     validated_data['product'] = check[0]
        # else:
        #     product.save()
        #     validated_data['product'] = product
        return User.objects.create(**validated_data)


class CitySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=25)
    population = serializers.IntegerField()


class CountrySerializer(serializers.Serializer):
    name =serializers.CharField(max_length=25)
    city = CitySerializer()

    def create(self, validated_data):
        city = City.objects.get_or_create(**dict(validated_data['city']))
        validated_data['city'] = city[0]
        return Country.objects.create(**validated_data)


class MaterialSerializer(serializers.Serializer):
    title = ProductSerializer(many=True)
    model = serializers.CharField(max_length=100)
    user = UserSerializer()

    def create(self, validated_data):
        product_list = []
        if validated_data.get('title'):
            for i in validated_data['title']:
                prod = ProductModel.objects.get_or_create(**i)
                product_list.append(prod[0])
        if validated_data.get('user'):
            prod_user = ProductModel.objects.get_or_create(**validated_data['user']['product'])[0]
            user = User.objects.create(name = validated_data['user']['name'], product = prod_user)
        if validated_data.get('model'):
            material = Material.objects.create(model = validated_data['model'], user=user)
            material.title.set(product_list)
            return material