from django.shortcuts import render,HttpResponseRedirect

# Create your views here.
from joins.forms import EmailForm
from joins.forms import JoinForm
from joins.models import Join

def get_ip(request):
    try:
        x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forward:
            ip = x_forward.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
    except:
        ip=""
    return ip
import uuid
def get_ref_id():
     ref_id= str(uuid.uuid4())[:11].replace('-','').lower()
     try :
         id_exists=Join.objects.get(ref_id=ref_id)
         get_ref_id()
     except:
         return ref_id

def home(request):


    form = JoinForm(request.POST or None)
    if form.is_valid():
        new_join = form.save(commit=False)
        email = form.cleaned_data['email']
        new_join_old, created = Join.objects.get_or_create(email=email)
        if created:
            new_join_old.ref_id=get_ref_id()
            new_join_old.ip_address=get_ip(request)
            new_join_old.save()
        return HttpResponseRedirect("/%s" %(new_join_old.ref_id))
    context = {"form":form}
    template = "home.html"
    return render(request,template,context)

def share(request,ref_id):
    print(ref_id)
    context = {'ref_id':ref_id}
    template = "share.html"
    return render(request,template,context)