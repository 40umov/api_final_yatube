from datetime import datetime

from django.shortcuts import get_object_or_404
from posts.models import Comment, Follow, Group, Post
from rest_framework import filters
from rest_framework.exceptions import PermissionDenied
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .permissions import FollowPermissions, IsAuthorOrReadOnly
from .serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer,
)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthorOrReadOnly,)

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied(
                "You must be authenticated to create a posts."
            )
        serializer.save(author=self.request.user,
                        pub_date=datetime.now())


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs["post_id"])
        return Comment.objects.filter(post=post)

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied(
                "You must be authenticated to create a comment."
            )
        post = get_object_or_404(Post, id=self.kwargs["post_id"])
        serializer.save(author=self.request.user,
                        created=datetime.now(), post=post)


class FollowViewSet(ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated, FollowPermissions)
    filter_backends = (filters.SearchFilter,)
    filterset_fields = ("following", "user")
    search_fields = ("following__username", "user__username")

    def get_queryset(self):
        user = self.request.user
        return Follow.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthorOrReadOnly,)
