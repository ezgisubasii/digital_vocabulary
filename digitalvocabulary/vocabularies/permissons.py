from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: # SAFE_METHODS is a tuple containing the HTTP methods that are considered "safe" (i.e., read-only) in RESTful APIs. These methods are GET, HEAD, and OPTIONS. The idea behind this check is that if the request method is one of these safe methods, then the user should be allowed to access the object without any further permission checks.
            return True

        return obj.profile.user == request.user
    
class IsOwnerOfVocabularyOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.vocabulary.profile.user == request.user