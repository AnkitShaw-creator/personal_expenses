from django.forms import ModelForm
from .models import user, userExpense

class userCreationform(ModelForm):
    class Meta:
        model = user
        fields = ['name', 'email']


class ExpenseForm(ModelForm):
    class Meta:
        model = userExpense
        fields = ['month', 'monthly_earning', 'monthly_expenses', 'monthly_savings', 
                  'monthly_home_rent', 'monthly_food_expenses', 'monthly_travel_expenses', 'monthly_child_care', 
                  'monthly_pet_care', 'monthly_cellphone', 'monthly_internet', 'monthly_health_care', 
                  'monthly_entertainment', 'monthly_loan', 'monthly_retirement',]