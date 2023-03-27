from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("hp")
    frnds=[
        'a',
        'b',
        'c'
    ]
    return JsonResponse(frnds,safe=False)