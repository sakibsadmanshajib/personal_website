from django.urls import path
from . import views

app_name = 'finance_management'

urlpatterns = [

    path('account/', views.account, name='account'),
    path('account/add', views.add_account, name='add_account'),
    path('account/<int:account_id>', views.account_details, name='account_details'),

    path('transaction/', views.transaction, name='transaction'),
    path('transaction/add', views.add_transaction, name='add_transaction'),

]