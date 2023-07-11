from django.shortcuts import render
from .models import Orders


# Create your views here.
def index(request):
    unique_code = request.GET.get('uniquecode')
    uni_code = Orders.objects.get(uni_code=unique_code)
    return render(request, 'main/index.html', {'order': uni_code})
