from django.shortcuts import render

def jinja_print(request):
    
    return render(request,'jinja_print.html',context=d)
d={'name':'chandu','age':21,'Gender':'male'}