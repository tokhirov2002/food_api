from rest_framework import serializers

from .models import Comments,Category,Foods,BookTable,Contact


class CommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class FoodsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Foods
        fields = '__all__'


class BookTableSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookTable
        fields = '__all__'


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'