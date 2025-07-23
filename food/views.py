from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny

from .models import Comments,Category,Foods,BookTable,Contact
from .serializers import CommentsSerializers,CategorySerializers,FoodsSerializers,BookTableSerializers,ContactSerializers



class CommetsView(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializers
    # permission_classes = [IsAuthenticated]


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    # permission_classes = [IsAdminUser]


class FoodsView(viewsets.ModelViewSet):
    queryset = Foods.objects.all()
    serializer_class = FoodsSerializers
    # permission_classes = [IsAdminUser]


class BookTableView(viewsets.ModelViewSet):
    queryset = BookTable.objects.all()
    serializer_class = BookTableSerializers
    # permission_classes = [AllowAny]


class ContactView(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers
