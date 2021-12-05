from django.http.response import HttpResponse
from django.shortcuts import render
import africastalking
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .iteganya import *
# Create your views here.
def  welcome(request):
    return render(request, 'index.html')

#  python3 -m pip install africastalking
AfricasUsername='turabayoimmacule@gmail.com'
api_key ='8b35e1c240f35404b50bb00bf8f46833e5f6dbefeef81fe811c5c3301780b914'
africastalking.initialize(AfricasUsername,api_key)

@csrf_exempt
def ussdApp(request):

    if request.method == 'POST':

        session_id = request.POST.get("sessionId")
        service_code = request.POST.get("serviceCode")
        phone_number =request.POST.get("phoneNumber")
        text = request.POST['text']
        level = text.split('*')
        category = text[:3]
        response =""
        #  main menu for our application
        if text == '':
            response =  "Murakaza neza ku Kigegapp \n"
            response += "1. Kubitsa  igihingwa \n"
            response += "2. kureba igihe bizacururizwa \n"
        elif text == '1':

            response = "Hitamo igihingwa ushaka kubitsa \n"
            response += "1. imbuto \n"
            response += "2. Imboga\n"
            response+= "3. Ibinyameke\n"
        elif text == '1*1':
            product="imbuto"
            response = " shyiramo ingano zazo' "+str(product)+"\n"
        elif category =='1*1' and int(len(level)) == 3 and str(level[2]) in  str(level):
            response = "shyiramo igihe zizamara \n"
        elif category =='1*1' and int(len(level)) == 4 and str(level[3]) in  str(level):
            response = "shyiramo code \n"
        elif category =='1*1' and int(len(level)) == 5 and str(level[4]) in  str(level):
            # save the data into the database
            category='Ibinyomoro'
            sizeOfland=level[2]
            names= level[3]
            idnumber = level[4]
            insert = Idafarmuser(sessiondId=session_id,
            serviceCode = service_code,
            phoneNumber=phone_number,
            level=level,
            category=category,
            sizeOfland=sizeOfland,
            names=names,
            idnumber=idnumber,
            )
            insert.save()
            response = "END Murakoze kwiyandikisha kuri Ida farm \n"
        
        #  ======================== INGENGABIHE==================
        elif text == '2':
            response = " Hitamo igihe bizacururizwa \n "
            response += "1.  ukwezi \n"
            response += "2. umwaka \n"
    
        elif text == '2*1':
            # save the data
            insertData(
                category='Rimwe',
                sessionID=session_id,
                phoneNumber=phone_number
            )
            response =" Murakoze , tuzajya tunbamenyesha aho igihe kigeze"
        elif text == '2*2':
            insertData(
                category='Kabiri',
                sessionID=session_id,
                phoneNumber=phone_number
            )
            response =" Murakoze , tuzajya tubamenyesha igihe gisigaye"
        elif text == '2*3':
            insertData(
                category='Burigihe',
                sessionID=session_id,
                phoneNumber=phone_number
            )
            response ="END Murakoze , tuzajya tubagezaho amakuru ku iteganyagihe Buri munsi"

        else:
            response = "mwongere mukanya"
        return HttpResponse(response)
    else:
        return HttpResponse('we are on ussd app')
