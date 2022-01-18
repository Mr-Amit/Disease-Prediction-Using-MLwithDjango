from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
import json 
from . import Clean
from .forms import SymptomForm
from .store import getsymptoms

# Create your views here.
def home(request):
    # return HttpResponse('<h1> Hey!' + string + '</h1>')
    return render(request, 'main/home.html')

class AjaxHandler(View):
    def get(self, request):
        text = request.GET.get('values')
        is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
        
        if is_ajax:
            # print("\nSSSS",text,"\n")
            sympts = text.split(',')
            
            # print(sympts)
            sympts = [int(e) for e in sympts[:-1]]
            # print(sympts)
            mainList = getsymptoms()
            mainList.sort()
            
            symptoms = [mainList[i] for i in sympts]
            diseases = Clean.runApp(symptoms)
            dis = ', '.join(diseases)
            
            # return HttpResponse('<h1> NOOOOOOOO </h1>')
            return JsonResponse({'ans':dis, 'dis1': diseases[0], 'dis2':diseases[1], 'dis3':diseases[2]}, status=200)
        
        return render(request, 'main/trial.html')

# def create(self,request):
#     array_data = request.POST['arr']
#     data = json.loads(array_data)
#     print(data)
#     return HttpResponse('Success')

