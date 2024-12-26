from django.shortcuts import render
from home.models import Hommode
from bypass.models import Bypassmode
from byreject.models import Byrejectmode
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import base64
from django.shortcuts import render


def index(request):
    search_query = request.GET.get('search', '')
    item = Hommode.objects.filter(name__icontains=search_query)
    return render(request, 'index.html', {'item': item})


def Helo(request):
    return HttpResponse("<h1> Hello </h1>")


def bypass(request):
    search_query = request.GET.get('search', '')
    items = Bypassmode.objects.filter(name__icontains=search_query)
    
    for item in items:
        if item.image:  
            item.image_base64 = base64.b64encode(item.image).decode('utf-8')
        else:
            item.image_base64 = None
    
    return render(request, 'pass/pass.html', {'items': items})


def byreject(request):
    search_query = request.GET.get('search', '')
    items = Byrejectmode.objects.filter(name__icontains=search_query)

    for item in items:
        if item.image:  
            item.image_base64 = base64.b64encode(item.image).decode('utf-8')
        else:
            item.image_base64 = None
    
    return render(request, 'reject/reject.html', {'items': items})


def DetailPass(request):
    if request.method == "GET":
        item_id = request.GET.get('id')  
        try:
            item = Bypassmode.objects.get(id=item_id) 
            if item.image:  
                item.image_base64 = base64.b64encode(item.image).decode('utf-8')
            else:
                item.image_base64 = None
            
            return render(request, 'pass/detail.html', {'item': item})

        except Bypassmode.DoesNotExist:
            return JsonResponse({'error': 'Item tidak ditemukan.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


def DetailReject(request):
    if request.method == "GET":
        item_id = request.GET.get('id')  
        try:
            item = Byrejectmode.objects.get(id=item_id)  
            if item.image:  
                item.image_base64 = base64.b64encode(item.image).decode('utf-8')
            else:
                item.image_base64 = None
            
            return render(request, 'reject/detail.html', {'item': item})

        except Byrejectmode.DoesNotExist:
            return JsonResponse({'error': 'Item tidak ditemukan.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
