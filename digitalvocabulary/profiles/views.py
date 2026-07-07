from rest_framework.views import APIView
from profiles.serializers import RegisterSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import permissions

# Create your views here.
class RegisterView(APIView):
    permission_classes = [permissions.AllowAny] # allow any user to access this view without authentication

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True) # validate the data and raise an exception if invalid
        user = serializer.save() # save the validated data to the database
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)

