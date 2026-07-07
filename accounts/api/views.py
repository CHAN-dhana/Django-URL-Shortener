from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LoginSerializer, RegisterSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework import status


class LogoutApiView(APIView):
    def get(self, request, *args, **kwargs):
        """
        Logout class
        """
        logout(request)
        return Response(
            {"non_field_errors": "successfully logged out"},
            status=status.HTTP_200_OK,
        )


class RegisterApiView(APIView):

    def post(self, request):

        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():

            User.objects.create_user(
                username=serializer.validated_data["username"],
                password=serializer.validated_data["password1"],
            )

            return Response(
                {
                    "success": True,
                    "message": "Account created successfully."
                },
                status=status.HTTP_201_CREATED,
            )

        # Return first validation error
        errors = serializer.errors

        first_error = "Registration failed."

        for key in errors:
            first_error = errors[key][0]
            break

        return Response(
            {
                "success": False,
                "message": first_error
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
class LoginApiView(APIView):

    def post(self, request, *args, **kwargs):

        serializer = LoginSerializer(
            data=request.data,
            context={"request": request}
        )
        if not serializer.is_valid():
            return Response(
                {
                    "message": serializer.errors.get(
                        "non_field_errors",
                        ["Invalid username or password."]
                    )[0]
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = serializer.validated_data["user"]

        if not user.is_active:
            return Response(
                {"message": "This account is inactive."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        login(request, user)

        return Response(
            {"message": "Login successful"},
            status=status.HTTP_200_OK,
        )