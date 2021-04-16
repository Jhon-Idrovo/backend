import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import get_user
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import ExpenseSerializer, DescriptionSerializer, TypeSerializer
from .models import Expense,ExpenseDescription, ExpenseType
from .utils import generate_color
class CreateExpenses(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        user = request.user
        for expense in request.data:
            print(expense)
            #try to get the type, if it doesn't exist we create it 
            try: 
                exp_type =ExpenseType.objects.get(expense_type=expense['expType'], user=user)
            except:
                #generate a unique color
                color = generate_color(user)
                exp_type=ExpenseType.objects.create(expense_type=expense['expType'], user=user, color=color)
            description,created = ExpenseDescription.objects.get_or_create(expense_type=exp_type,description=expense['description'],user=user)
            expense = Expense.objects.create(user= user, exp_type=exp_type, description= description, amount = expense['amount'], date=datetime.date.today())
        return Response(status=status.HTTP_201_CREATED)

class NewColors(APIView):
    def post(self, request):
        user = request.user
        exp_types = user.expensetype_set.all()

        for exp_type in exp_types:
            exp_type.color = generate_color(user)
            exp_type.save()

        return Response(status=status.HTTP_201_CREATED)
         