from django.urls import path
from .views import ItemView, ItemCreateView, item_list_create, ItemReveiwView, SingleItemCreateView, GetItemReviewsView

urlpatterns = [
    path('item-list/', item_list_create),
    path('item-create/<int:pk>/', ItemCreateView.as_view()),
    path('get-reviews/', ItemReveiwView.as_view()),
    path('get-single-rewiew/<int:pk>/', SingleItemCreateView.as_view()),
    path('get-item-reviews/<int:pk>/', GetItemReviewsView.as_view(),)
]
