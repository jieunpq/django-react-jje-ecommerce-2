from rest_framework import serializers
from store.models import Category, Product



# dev_34
# nested 전용 시리얼 라이져
class ProductSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    from api.serializers.category_serializers import CategorySimpleSerializer
    category = CategorySimpleSerializer()
    image = serializers.SerializerMethodField()  # 💡 여기에 정의

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'category', 'image']  # ✅ 명시적으로 포함해야 함

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None
    
    def create(self, validated_data):
        category_data = validated_data.pop("category")
        category, _ = Category.objects.get_or_create(**category_data)
        product = Product.objects.create(**validated_data, category=category)
        return product
