from rest_framework.generics import ListAPIView

from .models import Article
from .serializers import ArticleSerializer


class ArticleApiView(ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
