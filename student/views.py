from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here. - GET and POST


@csrf_exempt                    # Cross Site Request Forgery
def addNumbers(request):
    if (request.method == "POST"):
        getNum1 = int(request.POST.get("num1"))
        getNum2 = int(request.POST.get("num2"))
        result = getNum1 + getNum2
        mydict = {"num1": getNum1, "num2": getNum2,"operation":"addition", "result": result}
        resulttodisp = json.dumps(mydict)
        return HttpResponse(resulttodisp)
        



@csrf_exempt                    # Cross Site Request Forgery 
def studentAddPage(request):
    if (request.method == "POST"):

        #Reading
        # getName = request.POST.get("fullname")
        # getRoll = request.POST.get("rollno")
        # #Custom Dictionary Creation
        # mydict = {"name": getName,"rollno":getRoll};
        result = json.dumps(request.POST)
        return HttpResponse(result)

    else:
        return HttpResponse("No GET method Allowed")
