from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import Context, loader
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.gchart import PieChart
from graphos.renderers.gchart import LineChart
from graphos.renderers.gchart import BarChart
# Create your views here.
from beeSite.forms import BusinessForm, BusinessResultForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
import json
from django.http import JsonResponse
def busybee(request):
    return HttpResponse("You're at the busybee page.")

def business(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            result = calc_result(cd)
            _, expenses = result.popitem()
            _, income = result.popitem()
            result= income - expenses  
            xdata = ["Activity", "income", "expenses", "result"]
            ydata = [11,income, expenses, result]

            rawdata = [xdata,ydata]
            chart = BarChart(SimpleDataSource(data=rawdata))
            context = {'chart': chart}
            if request.is_ajax():
                #return HttpResponse("1:1")    
                array =[
                    ['Activity', 'Parcel'],
                    ['income',     income],
                    ['expenses',      expenses],
                    ['result',  result]
                    ];         
                #return HttpResponse(json.dumps(to_json), content_type='application/json')           
                #return JsonResponse({"data":"1","dat":"2"})
                return render(request, 'queryresponse.html', {'array':array})
            else:
                return HttpResponse("Still not an ajax request")               
# Chart object
        else:    
            return HttpResponse("Please provide valid values.")
    else:
        form = BusinessForm()
        return render(request, 'business_form.html', {'form':form})



def calc_result(cd):

    subj = cd['subject']
    email = cd.get('email', 'noreply@example.com')
    
    #Expenses
    rent = cd['rent']
    staff = cd['staff_salary']    
    staff_count = cd['staff_count']
    electricity = cd['electricity']
    tax = cd['tax']

    
    #Incomes
    sales = cd['income']
    final_tax = tax*sales/100
    #Result
    expenses = rent + staff*staff_count + electricity + final_tax
    result = {'exp':expenses, 'inc': sales}
    return result    