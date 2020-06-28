from django.shortcuts import render
from .forms import *
# Create your views here.
def homefun(request):
    respond_form = Create()
    respond_form.fields['customer_name'].widget.attrs = {'class' : 'form-control' ,'placeholder' : 'Name','id':'name'}
    respond_form.fields['customer_mail'].widget.attrs = {'class' : 'form-control' ,'placeholder' : 'mail id','id':'email'}
    respond_form.fields['message'].widget.attrs = {'class' : 'form-control' ,'placeholder' : 'your message','id':'message', 'rows': 6}
    context = {'form':respond_form,}
    if request.method == 'POST':
        #print('printing POST:',request.POST)
        form = Create(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home/index.html',context)

    return render(request,'home/index.html',context)

def contactfun(request):
    respond_form = Create()
    respond_form.fields['customer_name'].widget.attrs = {'class' : 'form-control' ,'placeholder' : 'Name','id':'name'}
    respond_form.fields['customer_mail'].widget.attrs = {'class' : 'form-control' ,'placeholder' : 'mail id','id':'email'}
    respond_form.fields['message'].widget.attrs = {'class' : 'form-control' ,'placeholder' : 'your message','id':'message', 'rows': 6}
    context = {'form':respond_form,}
    if request.method == 'POST':
        #print('printing POST:',request.POST)
        form = Create(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'contact/contact.html',context)

    return render(request,'contact/contact.html',context)
