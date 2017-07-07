# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
def index(request):
    return render(request,'index.html')
# Create your views here.


def pic_query(request):
    f=open('/tmp/pic_query.txt')
    data = f.read()
    print data
    data=[x for x in data.split('.') if " " in x]
    new_data=[]
    final_data=[]
    for line in data:
        for word in line.split(" "):
            if len(word) < 20:
                new_data.append(word)

        final_data.append(' '.join(new_data))
        new_data=[]
    context ={
        'data':final_data
    }
    return render(request,'index.html',context)