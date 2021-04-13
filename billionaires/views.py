from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Avg, Max, Min, Count
from .models import Billionaires
from .forms import PostForm

# Create your views here.


class BillionairesView(ListView):
    model = Billionaires
    template_name = 'billionaires/chart.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['av'] = Billionaires.objects.all().aggregate(Avg('money'), Max('money'), Min('money'), Count('money'))
        return context
        
class CreateBillionaireView(CreateView): 
  
    # specify the model for create view 
    model = Billionaires 
    form_class = PostForm
    template_name = 'billionaires/add_bill.html'
    
    # specify the fields to be displayed 
  
    # fields = ['name', 'money', 'source', 'description']
    
    # def get_success_url(self):
    #     return reverse('create-bill')
        
        

        
        
class UpdateBillionaireView(UpdateView):
    # specify the model you want to use
    model = Billionaires 
    template_name = 'billionaires/update_bill.html'
    form_class = PostForm
  
    # specify the fields
    # fields = [
    #     "name",
    #     "money",
    #     "source",
    #     "description"
    # ]
  
    # can specify success url
    # url to redirect after successfully
    # updating details
    # success_url ="/"
   

class DeleteBillionaireView(DeleteView):
    model = Billionaires
    template_name = 'billionaires/confirm_delete.html'

    success_url ="/"
    # def get_success_url(self):
    #     return reverse('billionaires')
    