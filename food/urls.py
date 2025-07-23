from rest_framework.routers import DefaultRouter
from django.urls import path,include

from .views import CommetsView,CategoryView,FoodsView,BookTableView,ContactView

router = DefaultRouter()

router.register(r'comments', CommetsView, basename='commentsview')
router.register(r'category', CategoryView, basename='categoryview')
router.register(r'foods', FoodsView, basename='foodsview')
router.register(r'booktable', BookTableView, basename='booktableview')
router.register(r'contact', ContactView, basename='contactview')



urlpatterns = [
    path('', include(router.urls))
]