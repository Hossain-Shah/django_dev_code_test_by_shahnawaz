from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from BalanceTransfer.models import balance
from django.contrib.auth.models import User
from rest_framework import status
import json
from django.db.models import Q
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from rest_framework import generics
from BalanceTransfer.serializers import RegistrationLoginSerializer, balanceSerializer


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request, user)
            instance = balance(user = request.user, balance = 0)
            instance.save()
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def profile(request):
    msg=""
    if request.method == "POST":
        try:
            username = request.POST["username"]
            amount = request.POST["amount"]
            senderUser= User.objects.get(username=request.user.username)
            receiverUser=User.objects.get(username=username)
            sender = balance.objects.get(user = senderUser)
            receiver = balance.objects.get(user = receiverUser)           
            sender.balance = sender.balance - int(amount)
            receiver.balance = receiver.balance + int(amount)
            sender.save()
            receiver.save()
            msg = "Transaction Success"
        except Exception as e:
            print(e)
            msg = "Transaction Failure, Please check and try again"
    user = balance.objects.get(user=request.user)
    return render(request,'registration/profile.html', {"balance":user.balance, "msg":msg})


class RegistrationLogin(generics.ListCreateAPIView):
    def post(self, request, format=None):
        username = request.data.get("username")
        password = request.data.get("password")   
        queryset = User.objects.filter(Q(username__icontains=username)|Q(password__icontains=password))
        serializer_class = RegistrationLoginSerializer(instance=queryset, many=True, context={"request": request})
        if not serializer_class.data:
            return_data = {
                "message": "User not found",
                "status":status.HTTP_200_OK,
                "data": [],
            }
        else:
            return_data = {
                "message": "User found",
                "status": status.HTTP_200_OK,
                "data": serializer_class.data,
        }
        return HttpResponse(json.dumps(return_data, cls=DjangoJSONEncoder), content_type="application/json; charset=utf-8")


class BalanceList(generics.ListCreateAPIView):
    def post(self, request, format=None):
        queryset = balance.objects.all()
        serializer_class = balanceSerializer(instance=queryset, many=True, context={"request": request})
        if not serializer_class.data:
            return_data = {
                "message": "Transaction information not found",
                "status":status.HTTP_200_OK,
                "data": [],
            }
        else:
            return_data = {
                "message": "Transaction information found",
                "status": status.HTTP_200_OK,
                "data": serializer_class.data,
            }
        return HttpResponse(json.dumps(return_data, cls=DjangoJSONEncoder), content_type="application/json; charset=utf-8")