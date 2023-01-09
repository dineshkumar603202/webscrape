from django.shortcuts import render
from django import forms
from copy import deepcopy
from bs4 import BeautifulSoup
import requests
from test_app.models import FetchModel

class FetchForm(forms.Form):
    url = forms.URLField( label='URL : ',required=True,widget=forms.TextInput(attrs={'size': '40','value':'https://www.flipkart.com/srpm-wayfarer-sunglasses/p/itmaf19ae5820c06'}),validators=())

def fetch_scrap(request):
    if request.method == 'POST':
        new_data = deepcopy(request.POST)
        form = FetchForm(new_data) 
        if form.is_valid():
            url= new_data.get('url','')
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            lists = soup.find_all('div',class_="_1YokD2 _3Mn1Gg col-8-12")
            url = new_data.get('url','')
            for page in lists:
                price = page.find('div',class_='_30jeq3 _16Jk6d').text
                title  = page.find('span',class_='B_NuCI').text
                description  = page.find('div',class_='_1AN87F').text
                size  = page.find('div',class_='_3Oikkn _3_ezix _2KarXJ _31hAvz').text
                if price and title and description and size:
                    fetch_data = FetchModel.objects.create(url=new_data.get('url',''),price= price,title=title,description=description,size=size)
            data = FetchModel.objects.all()
        return render(request,'index.html',{'form':form,'data':data})
    form = FetchForm()
    data = FetchModel.objects.all()
    return render(request,'index.html',{'form':form,'data':data})