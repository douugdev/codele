from blog.models import Post
from .serializers import PostSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class PostsList(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


    # def post(self, request):
    #     serializer = PostSerializer(data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetail(APIView):

    def get_object(self, id):
        try:    
            return Post.objects.get(id=id)
        except Post.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        serializer = PostSerializer(self.get_object(id))
        return Response(serializer.data)
    
    # def put(self, request, id):
    #     serializer = PostSerializer(self.get_object(id), data=data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, id):
    #     self.get_object(id).delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
