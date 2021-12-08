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
         response = ""
         #main menu
         if text =='':
         response = "CON Muhitemo ururimi\n"
         response +=I"1.kinyarwanda\n"
         response +="2.English\n"
         elif text =='1':
             response = "CON murakaza neza Hunikapp\n "
             response +="1.Umuhinzi\n"
             response +="2.Umucuruzi\n"
             if text =='1*1':
                 response = "CON Umuhinzi, Mwiyandikishe\n "
                 response += "Amazina yanyu\n"
                 response += "Numero y irangamuntu yanyu\n"
                 response += "Mushyiremo Umubare w ibanga\n"
                 response = "CON  kwiyandisha byagenze neza\n"
                 if text == '1':
                     response += "Mukomeze\n"
                     response == "CON  muhitemo igihingwa Hunikapp\n"
                     response += "1.Imbuto\n"
                     response += "2.Ibinyampeke(umuceri,ingano....)\n"
                     response += "3.Ibirayi,Ibijumba,Imyumbati...\n"
                     elif text =="1*1":
                         response = "CON  Imbuto\n"
                         response += "1.izina"
                         response +=" ubwoko"
                         response +=""

                 


         else:
             response = " CON mwongere mukanya"
         return HttpResponse(response)
     else:
         return HttpResponse('we are on ussd app')
