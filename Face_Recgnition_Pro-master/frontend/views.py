from django.shortcuts import render ,redirect
from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .forms import UserForm
from .models import User ,Image
from rest_framework import viewsets
from .serializers import UserSerializer
import os

# class userview(ListModelMixin , GenericAPIView):
#     print('hey')
#     serializer_class = UserSerializer
#     queryset = Users.objects.all()
#     print(queryset)
#     #return Response({"User": User})

#     def perform_create(self, serializer):
#         Users = get_object_or_404(Users, id=self.request.data.get('Users_id'))
#         return serializer.save(Users=Users)

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
def register(request):  
    #print(os.system(pwd))
    return render(request, 'register.html', {'msg':'Fill the Form','status':'warning'})


def upload(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            email = request.POST['email']
            user = User(name=name,email=email)
            user.save()
            for file in request.FILES.getlist('user_img'):
                img = Image( user=user,user_img=file)
                img.save()
                user.img.add(img)
            user.save()
            return render(request,'register.html',{'msg':'Data Uploaded Successfully','status':'success'})
        except Exception as e:
            return render(request,'register.html',{'msg':"User already exists! Try again with different name.",'status':'danger'})
    return HttpResponseRedirect('/')



from rest_framework.views import APIView
from .serializers import LoginSerializer
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import generics
from .serializers import UserSerializer,ImageSerializer
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import OrderingFilter, SearchFilter
# from django_filters import FilterSet
# from django_filters import rest_framework as filters


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key,"message":"User Successfully Logged in."}, status=200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication)

    def post(self, request):
        django_logout(request)
        return Response(status=204)


from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView
from django.db.models import Q

from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework.decorators import action

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets


class PollListView(generics.GenericAPIView,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]



    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def put(self, request, id=None):
        return self.update(request, id)

    def perform_update(self, serializer):
        print(self.request.user)
        serializer.save(created_by=self.request.user)        

    def delete(self, request, id=None):
        return self.destroy(request, id)



class userviewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer





