from django.shortcuts import render
from rest_framework import generics, status
from .models import ItemModel, ItemReveiw
from .serializers import ItemSerializer, ItemReveiwSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.pagination import PageNumberPagination

# Create your views here.


class CustomNumberPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'


@api_view(['GET', 'POST'])
def item_list_create(request):
    if request.method == 'GET':
        items = ItemModel.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        item = ItemModel.objects.all()
        serializer = ItemSerializer(data=request.data)
        print(request.user.id)
        serializer.initial_data["user"] = request.user.id
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemView(generics.ListCreateAPIView):
    queryset = ItemModel.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = request.user
        print(user.id)
        print(request)
        return self.create(request, *args, **kwargs)


class ItemCreateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemModel.objects.all()
    serializer_class = ItemSerializer


class ItemReveiwView(generics.ListCreateAPIView):
    queryset = ItemReveiw.objects.all()
    serializer_class = ItemReveiwSerializer

    def create(self, request, *args, **kwargs):
        print(request.user.email)

        serializer = self.get_serializer(data=request.data)

        print(serializer.initial_data["rating_description"])
        serializer.initial_data["user"] = request.user.id

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class SingleItemCreateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemReveiw.objects.all()
    serializer_class = ItemReveiwSerializer


class GetItemReviewsView(generics.ListAPIView):
    queryset = ItemReveiw.objects.all()
    serializer_class = ItemReveiwSerializer
    pagination_class = CustomNumberPagination

    def get_queryset(self):
        item_id = self.kwargs["pk"]
        print(item_id)
        return ItemReveiw.objects.filter(item=item_id)
