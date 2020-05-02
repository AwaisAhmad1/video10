from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def staff_home(request):
    return render(request, "staff_template/staff_home_template.html")

