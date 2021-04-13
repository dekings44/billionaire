from django.urls import path
from .views import BillionairesView, CreateBillionaireView, UpdateBillionaireView, DeleteBillionaireView

urlpatterns = [
    path('', BillionairesView.as_view(), name='billionaires'),
    path('update/<int:pk>', UpdateBillionaireView.as_view(), name='update'),
    path('add', CreateBillionaireView.as_view(), name='create-bill'),
    
    path('delete/<int:pk>', DeleteBillionaireView.as_view(), name='delete'),
]