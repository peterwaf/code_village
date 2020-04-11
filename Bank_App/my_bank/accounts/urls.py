from django.contrib import admin
from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('accounts/',views.show_accounts,name='accounts'),
    path('accounts/add/',views.AddCustomerAccounts,name="add_account"),
    path('sendmoney/<int:customer_id>/',views.sendMOney,name="sendmoney"),
    path('profile/balance/<int:customer_id>/',views.CheckBalance,name="balance"),
    path('withdraw/',views.WithdrawMoney,name="withdraw")
    
]