from django.http import JsonResponse
from rest_framework.decorators import api_view

# Create your views here.


def testar_bancos(request, *args, **kwargs):
    return JsonResponse({"teste": "voce conseguiu ajsdajsdasd"})


@api_view(["GET"])
def testar_api(request, *args, **kwargs):
    # request.GET "params"

    return JsonResponse({"api": "maravilha garotoo"})
