from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from . models import Attempts

# Create your views here.

def Index(request):
    return render(request,"index.html")

def ERR(request):
    return render(request,"ERR.html")

def handlecredentials(request):
    if request.method=="POST":
        dictionary = {
            "Anubhav Singh":{
                "CVV":102,
                "Credit_Card_number":101010101011,
                "EXP_Date":"01/25"
            }
    ,
            "Anupam Chaudhary":{
                "CVV":101,
                "Credit_Card_number":101010101010,
                "EXP_Date":"01/25"
            }
    ,
            "Arpit Mishra":{
                "CVV":103,
                "Credit_Card_number":101010101012,
                "EXP_Date":"01/25"
            }
    ,
            "Bharat Prajapati":{
                "CVV":104,
                "Credit_Card_number":101010101013,
                "EXP_Date":"01/25"
            }
    ,
            "Jagannath Pandey":{
                "CVV":105,
                "Credit_Card_number":101010101014,
                "EXP_Date":"01/25"
            }
        }
        attempts = Attempts.objects.all()
        attemptList = list(attempts.values())
        print(attemptList)
        attemptData = attemptList[0].get("attempts")
        print(attemptData)
        cardNum = request.POST['cardNum']
        holderName = request.POST['holderName']
        cvv = request.POST['cvv']
        expDate = request.POST['expDate']
        nameVerifier = dictionary.get(holderName,"notPresent")  
        if(attemptData<2):
            if(nameVerifier!="notPresent"):
                if(nameVerifier.get("CVV")==int(cvv)):
                    if(nameVerifier.get("Credit_Card_number")==int(cardNum)):
                        if(nameVerifier.get("EXP_Date")==expDate):
                            messages.success(request,"Successfully Submitted")    
                            return redirect("/processed")
                        else:
                            attemptData+=1
                            edit = Attempts(attempts=attemptData)
                            edit.save()
                            (Attempts.objects.filter(attempts=attemptData-1)).delete()
                            messages.success(request,"Expiry Date is not valid")    
                            return redirect("/")
                    else:
                        attemptData+=1
                        edit = Attempts(attempts=attemptData)
                        edit.save()
                        (Attempts.objects.filter(attempts=attemptData-1)).delete()
                        messages.success(request,"Card Number not valid")    
                        return redirect("/")
                else:
                    attemptData+=1
                    edit = Attempts(attempts=attemptData)
                    edit.save()
                    (Attempts.objects.filter(attempts=attemptData-1)).delete()
                    messages.success(request,"CVV Not recognised")    
                    return redirect("/")
            messages.success(request,"Card does not exist")    
            return redirect("/")
        else:
            messages.success(request,"OUT OF ATTEMPTS, Your IP Has been blocked by the admin")    
            return redirect("/ERR")

def processed(request):
    return render(request,"processed.html")