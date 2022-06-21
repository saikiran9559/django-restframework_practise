from django.urls import path,include
from .views import article_list, article_detail, ArticleAPIView, ArticleDetail
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    # path('viewset/',include(router.urls)),
    # path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    # path('detail/<int:pk>/', article_detail),
    path('detail/<int:id>/', ArticleDetail.as_view()),
]