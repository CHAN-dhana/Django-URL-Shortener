from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(
        label=_("Password"),
        style={"input_type": "password"},
        trim_whitespace=False,
        max_length=128,
        write_only=True,
    )

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if username and password:
            user = authenticate(
                request=self.context.get("request"),
                username=username,
                password=password,
            )
            if not user:
              msg = "Invalid username or password."               
              raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code="authorization")
        data["user"] = user
        return data


import re

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password1 = serializers.CharField(
        write_only=True,
        min_length=8
    )
    password2 = serializers.CharField(
        write_only=True,
        min_length=8
    )

    def validate(self, data):
        username = data["username"].strip()
        password1 = data["password1"]
        password2 = data["password2"]

        # Username validation
        if len(username) < 4:
            raise serializers.ValidationError({
                "username": ["Username must be at least 4 characters."]
            })

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({
                "username": ["Username already exists."]
            })

        # Password match
        if password1 != password2:
            raise serializers.ValidationError({
                "password2": ["Passwords do not match."]
            })

        # Password length
        if len(password1) < 8:
            raise serializers.ValidationError({
                "password1": ["Password must contain at least 8 characters."]
            })

        # Cannot be only numbers
        if password1.isdigit():
            raise serializers.ValidationError({
                "password1": ["Password cannot contain only numbers."]
            })

        # -------- ADD THESE LINES HERE --------

        if not re.search(r"[A-Z]", password1):
            raise serializers.ValidationError({
                "password1": ["Password must contain at least one uppercase letter."]
            })

        if not re.search(r"[a-z]", password1):
            raise serializers.ValidationError({
                "password1": ["Password must contain at least one lowercase letter."]
            })

        if not re.search(r"\d", password1):
            raise serializers.ValidationError({
                "password1": ["Password must contain at least one number."]
            })

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password1):
            raise serializers.ValidationError({
                "password1": ["Password must contain at least one special character."]
            })

        # -------- END --------

        return data