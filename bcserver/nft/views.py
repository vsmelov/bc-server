from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from nft.w3 import nft


def has_nft_handler(request):
    try:
        nftId = request.GET['nftId']
        wallet = request.GET['wallet']
        nftId = int(nftId)
        owner = nft.functions.ownerOf(nftId).call()
        result = owner.lower() == wallet.lower()
        return JsonResponse({"result": result})
    except Exception as exc:
        error = f'error: {type(exc)=} {exc=}'
        return JsonResponse({"error": error}, status=500)
