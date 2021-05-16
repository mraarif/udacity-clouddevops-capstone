from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from .models import Article
from .serializers import ArticleSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 1000


class ArticleApiView(ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.order_by("published_at")
    pagination_class = StandardResultsSetPagination
