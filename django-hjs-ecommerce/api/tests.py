from django.test import TestCase
import pickle

# Create your tests here.


# dev_28 시리얼라이제이션의 이해


def add_view(num1, num2):
    return num1 + num2


def suv_view(num1, num2):
    return num1 - num2


class ObjectAPITest(TestCase):
    def setUp(self):
        pass

    def test_path(self):

        dict = {
            "products": add_view,
            "categories": suv_view,
        }
        url = "products"

        print(dict[url](1, 2))

        url = "sub"
        print(dict[url](1, 2))


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from .serializers import CategorySerializer, CategorySimpleSerializer


class CategoriesAPI(APIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    simple_serializer_class = CategorySimpleSerializer

    def get_queryset(self):
        return self.queryset

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)

    def get_simple_serializer(self, *args, **kwargs):
        return self.simple_serializer_class(*args, **kwargs)

    def get(self, request):
        categories = self.get_queryset()
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_simple_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        # 예: id를 request에서 받았다고 가정
        category_id = request.data.get("id")
        try:
            category = self.get_queryset().get(id=category_id)
        except Category.DoesNotExist:
            return Response(
                {"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_simple_serializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        category_id = request.data.get("id")
        try:
            category = self.get_queryset().get(id=category_id)
            category.delete()
            return Response(
                {"message": "Category deleted"}, status=status.HTTP_204_NO_CONTENT
            )
        except Category.DoesNotExist:
            return Response(
                {"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND
            )


# class ProductRetrieveByIdOrNameView(RetrieveAPIView):
#     serializer_class = ProductSerializer

#     def get_object(self):
#         queryset = Product.objects.all()
#         lookup_id = self.kwargs.get("id")
#         lookup_name = self.kwargs.get("name")

#         if lookup_id:
#             return queryset.get(id=lookup_id)
#         elif lookup_name:
#             return queryset.get(name=lookup_name)
#         else:
#             raise NotFound("id 또는 name 파라미터가 필요합니다.")

# Create your tests here.
from django.test import TestCase
import jwt


from django.test import TestCase
from django.contrib.auth.hashers import make_password, check_password
from cryptography.fernet import Fernet

#dev_12_Fruit
class HashAndEncryptionTestCase(TestCase):

    def test_one_way_hash(self):
        """단방향 해시 테스트"""
        original_password = "my_secret_password"

        # 비밀번호 해시
        hashed_password = make_password(original_password)

        print(hashed_password)
        # 해시된 값은 원본과 다름
        self.assertNotEqual(original_password, hashed_password)

        # check_password로만 원본과 같은지 검증 가능
        self.assertTrue(check_password(original_password, hashed_password))
        self.assertFalse(check_password("wrong_password", hashed_password))

   