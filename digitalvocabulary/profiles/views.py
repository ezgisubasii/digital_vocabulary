from rest_framework.views import APIView
from profiles.serializers import RegisterSerializer, UserSerializer , ProfileSerializer
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from profiles.models import Profile, FollowRelation

from django.shortcuts import get_object_or_404
from rest_framework import status

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

class FollowProfileView(APIView):
    def post(self, request, username):
        user_to_foolow = get_object_or_404(Profile, user__username= username)

        if request.user.profile == profile_to_follow:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        
        FollowRelation.objects.get_or_create(follower=request.user.profile, following=profile_to_follow)
        return Response({"success": f"You are now following succesfully"})
    
class UnfollowProfileView(APIView):

    def post(self, request, username):
        profile_to_unfollow = get_object_or_404(Profile, user__username=username)

        follow_relation = FollowRelation.objects.filter(follower=request.user.profile, following=profile_to_unfollow)
        if follow_relation.exists():
           follow_relation.delete()
           return Response({"success": "User unfollowed succesfully."})
        else:
            return Response({"error": "You are not following this user."}, status=status.HTTP_400_BAD_REQUEST)
        
class FollowedListView(ListAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        user_profile =self.request.user.profile.following.all()  # Get the profiles that the user is following
        return user_profile.followers.all()  # Return the followers of those profiles
