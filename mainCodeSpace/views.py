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
            "Anubhav":{
                "CVV":101,
                "Credit_Card_number":9876543298765432,
                "EXP_Date":"01/25"
            }
    ,
            "Anpuam":{
                "CVV":386,
                "Credit_Card_number":1234567812345678,
                "EXP_Date":"01/25"
            }
    ,
            "Tanishq":{
                "CVV":141,
                "Credit_Card_number":1234567891234567,
                "EXP_Date":"01/25"
            }
    ,
            "Shubh":{
                "CVV":242,
                "Credit_Card_number":4152789636521452,
                "EXP_Date":"01/25"
            }
    ,
            "Shreyas":{
                "CVV":382,
                "Credit_Card_number":7845895645125623,
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