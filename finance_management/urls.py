from django.urls import path
from . import views

app_name = 'finance_management'

urlpatterns = [

    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('account/', views.account, name='account'),
    path('account/add', views.add_account, name='add_account'),

    path('transaction/', views.transaction, name='transaction'),
    path('transaction/add', views.add_transaction, name='add_transaction'),

]