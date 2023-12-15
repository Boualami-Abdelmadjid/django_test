from django.urls import path
from django.contrib.auth.views import LogoutView
from main.views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    #Auth endpoints
    path('register/',RegisterView.as_view(), name="register"),
    path('login/',LoginView.as_view(), name="login"),
    path('logout/',login_required(LogoutView.as_view()), name="logout"),
    # Views
    path('',login_required(ReceiptView.as_view()), name="receipts"),
    path('receipts/<int:pk>/',login_required(ReceiptDetailView.as_view()), name="receipts-details"),
    path('receipts/add/',login_required(AddReceiptView.as_view()), name="add-receipt"),
    path('receipts/edit/<int:pk>/',login_required(EditReceiptView.as_view()), name="edit-receipt"),
]
