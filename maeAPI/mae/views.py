from django.http import JsonResponse

# Create your views here.

def testar_bancos(request, *args, **kwargs):
    return JsonResponse({"teste":"voce conseguiu ajsdajsdasd"})

def testar_api(request, *args, **kwargs):
    return JsonResponse({"api":"maravilha garotoo"})