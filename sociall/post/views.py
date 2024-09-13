from .serializers import Postserializers
from .models import Post
from account.models import Profile
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework.views import APIView
from .permission import IsOwner



class Postcreate(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializers
    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

class PostList(ListAPIView):
    serializer_class = Postserializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        author = self.request.user
        following_ids = author.profile.followers.values_list('id', flat=True)
        return Post.objects.filter(author__profile__id__in=following_ids)


class DeletePost(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializers
    permission_classes = [IsAuthenticated, IsOwner]
