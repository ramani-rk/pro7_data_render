from django.shortcuts import render

# Create your views here.

def data_render(request):
    data = 'India Enter into the worldcup finals after 12 years'
    d = {'cricket': data}
    return render (request,'data_render.html',context=d)
