from django.shortcuts import render
from members.models import member
from django.http import JsonResponse,HttpResponse

# Create your views here.
def show_all_members(request):
    all_members = member.objects.all()
    #return HttpResponse(all_members)
    context = {
        "all_members" : all_members,
    }
    return render(request,'all_members.html',context)

def member_detail(request,id):
    req_member = member.objects.get(id=id)
    context = {
        "req_member" : req_member
    }
    return render(request,"member_detail.html",context)