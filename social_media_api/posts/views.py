from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly

# ViewSet for Post CRUD operations
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# ViewSet for Comment CRUD operations
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        post_pk = self.kwargs.get('post_pk')
        if post_pk:
            return Comment.objects.all().filter(post__pk=post_pk)
        return Comment.objects.all()

    def perform_create(self, serializer):
        post_pk = self.kwargs.get('post_pk')
        post = Post.objects.get(pk=post_pk)
        serializer.save(author=self.request.user, post=post)

# Feed view using permissions.IsAuthenticated
class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get users the current user follows
        following_users = request.user.following.all()
        # Filter posts from followed users, ordered by creation date
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=200)