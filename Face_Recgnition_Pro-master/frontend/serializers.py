from rest_framework import serializers
from .models import User , Image
from django.contrib.auth.models import User as UserA
from django.contrib.auth import authenticate
from rest_framework import exceptions


class ImageSerializer(serializers.ModelSerializer):
    #user = UserSerializer()
    class Meta:
        model = Image
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    img = ImageSerializer(many=True)
    class Meta:
        model = User
        fields = ('name','email','created_at','updated_at','img')



# class QuestionSerializer(serializers.ModelSerializer):
#     choices = ChoiceSerializer(many=True)
#     tags = TagSerializer(many=True)

#     class Meta:
#         model = Question
#         fields = [
#             "id",
#             "title",
#             "status",
#             "created_by",
#             "choices",
#             "tags"
#         ]
# read_only_fields = ["tags"]



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "User is deactivated."
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Unable to login with given credentials."
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide username and password both."
            raise exceptions.ValidationError(msg)
        return data

