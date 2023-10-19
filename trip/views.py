
from django.shortcuts import render
from trip.models import table1, table2


# Create your views here.
def db_fun(request):
    obj1 = table1.objects.all()
    #return render(request,'index.html', {'key1': obj1})

    #def fun2Team(request):
    obj2 = table2.objects.all()
    return render(request,"index.html",{'key1':obj1, 'key2':obj2})