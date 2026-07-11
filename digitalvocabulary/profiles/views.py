from rest_framework.views import APIView
from profiles.serializers import RegisterSerializer, UserSerializer , ProfileSerializer
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from profiles.models import Profile

# Create your views here.
class RegisterView(APIView):
    permission_classes = [permissions.AllowAny] # allow any user to access this view without authentication

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True) # validate the data and raise an exception if invalid
        user = serializer.save() # save the validated data to the database
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)

class ProfileSearchView(ListAPIView):
    serializer_class = ProfileSerializer
    def get_queryset(self):
        username = self.request.query_params.get('username', '')
        if username:
            return Profile.objects.filter(user__username__icontains=username)
        return Profile.objects.none()  # Return an empty queryset if no username is provided