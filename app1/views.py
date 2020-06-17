import json

from django.db.models import Count,Avg,Sum
from django.http import JsonResponse
from django.shortcuts import render
from .models import Salaries

# Create your views here.
# def ec(request):
#     Number=number.objects.all()
#     name = list(number.objects.values_list('name', flat=True))
#     nub= list(number.objects.values_list('nub', flat=True))
#     print(name)
#     print(nub)
#     jsondata = {
#         ' Number': Number,
#         'name':name,
#         'nub':nub
#     }
#     return render(request,'ec.html',context=jsondata)


def rg(request):
    list1=[]
    list2=[]
    dict ={}
    dict['list'] = []
    salaries=Salaries.objects.values('emp_no').annotate(avg=Avg('salary'))[:20]

    emp_no=list(Salaries.objects.values_list('emp_no').annotate())
    for i in salaries:
        # print([i["emp_no"]])
        dict['list'].append([i["emp_no"],i["avg"]])

    for x in dict['list']:
        print(x)
    print("_________________________")
    # print(dict['list'][-5:])
        # dict['list'].remove(dict['list'][0][0])

    context={
        'dict':dict['list']
    }

    return render(request,'Regression graph.html',context=context)
def per(request):
    salaries = Salaries.objects.values('emp_no').annotate(sum=Sum('salary'))[:20]
    data = {}
    for k in salaries:
        data.update({k["emp_no"]:k["sum"]})
    print(data)
    print(json.dumps(data))
    test = []
    for logKey in data:
        test.append({'value': data[logKey], 'name': logKey})
    print(test)

    return render(request,'per.html',{'data': test})

def line(request):
    dict = {}
    dict['list'] = []
    salaries = Salaries.objects.values('emp_no').annotate(avg=Avg('salary'))[:12]

    emp_no = list(Salaries.objects.values_list('emp_no').annotate())
    for i in salaries:
        # print([i["emp_no"]])
        dict['list'].append( i["avg"])

    for x in dict['list']:
        print(x)
    print("_________________________")
    # print(dict['list'][-5:])
    # dict['list'].remove(dict['list'][0][0])

    context = {
        'dict': dict['list']
    }

    return render(request, 'line.html', context=context)
