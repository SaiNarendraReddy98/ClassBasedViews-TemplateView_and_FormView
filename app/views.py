from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from app.forms import *
from django.http import HttpResponse
# Create your views here.

class TV_displaying_data(TemplateView):
    template_name = 'TV_displaying_data.html'
    def get_context_data(self, **kwargs):
        ECDO = super().get_context_data(**kwargs)
        ECDO['name'] = 'K.Narendra sai reddy'
        ECDO['age'] = 25
        ECDO['mobile'] = 9581063642
        return ECDO
    
class Inserting_data_by_TV(TemplateView):
    template_name = 'Inserting_data_by_TV.html'
    def get_context_data(self, **kwargs):
        ECDO = super().get_context_data(**kwargs)
        ECDO['IFO'] = IndiaForm
        return ECDO
    def post(self,request):
        IDO = IndiaForm(request.POST)
        if IDO.is_valid():
            IDO.save()
            return HttpResponse('<center><h1>inserting data is successfully completed')
        

class inserting_data_by_FV(FormView):
    template_name = 'inserting_data_by_FV.html'
    form_class = IndiaForm
    def form_valid(self,form):
        form.save()
        return HttpResponse('<center><h1>inserting data is successfully completed')
    
