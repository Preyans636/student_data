from django.http import HttpResponse
from django.shortcuts import render
import pandas
s_name = []
s_age = []
s_std = []
s_ph = []
s_address = []
def homepage(request):
    global s_name , s_age , s_std , s_ph , s_address
    name = request.POST.get('s_name')
    age = request.POST.get('s_age')
    std = request.POST.get('s_std')
    ph = request.POST.get('s_ph')
    address = request.POST.get('s_address')
    s_name.append(name)
    s_age.append(age)
    s_std.append(std)
    s_ph.append(ph)
    s_address.append(address)
    dic_data = {
        'name':s_name,
        'age':s_age,
        'std':s_std,
        'ph':s_ph,
        'address':s_address
    }
    pd_data = pandas.DataFrame(dic_data)
    pd_data.to_csv('data.csv')
    return render(request,'index.html')