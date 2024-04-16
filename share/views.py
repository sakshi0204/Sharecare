from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import MaterialForm
# relative import of forms 
from .models import Material

from django.shortcuts import (get_object_or_404, 
                              render, 
                              HttpResponseRedirect) 


#Create your views here.
def index(request):
    context ={} 

    # add the dictionary during initialization 
    context["dataset"] = Material.objects.all() 
   # context["datavolt"] = Volt.objects.all()     
    return render(request, "share/index.html", context)
def explore(request):
    return render(request,"share/ExploreallButton.html")

def contact(request):
    
    return render(request, "share/contact.html")
def book_image(request): 
  
    if request.method == 'POST': 
        form = MaterialForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('/share/more')
            
    else: 
        form = MaterialForm() 
    return render(request, 'share/uploadimage.html', {'form' : form}) 
    
  
def success(request): 
    return HttpResponse('successfully uploaded') 



from django.shortcuts import render 

# relative import of forms 
from .models import Material 



def create_view(request): 
    # dictionary for initial data with 
    # field names as keys 
    context ={} 

    # add the dictionary during initialization 
    form = MaterialForm(request.POST or None) 
    if form.is_valid(): 
        form.save() 
        
    context['form']= form 
    return render(request, "share/insert.html", context) 


from django.shortcuts import render 

# relative import of forms 
from .models import Material


def book_view(request): 
    # dictionary for initial data with 
    # field names as keys 
    context ={} 

    # add the dictionary during initialization 
    context["dataset"] = Material.objects.all() 
        
    return render(request, "share/book_view.html", context) 

from django.shortcuts import (get_object_or_404, 
                            render, 
                            HttpResponseRedirect) 

from .models import Material


# delete view for details 
def delete_material(request, id): 
    # dictionary for initial data with 
    # field names as keys 
    context ={} 

    # fetch the object related to passed id 
    obj = get_object_or_404(Material, id = id) 


    if request.method =="POST": 
        # delete object 
        obj.delete() 
        # after deleting redirect to 
        # home page 
        return HttpResponseRedirect("/") 

    return render(request, "share/delete_material.html", context) 



#Link Update---------------------
def update_material(request, id):
    if request.method == 'POST': 
        material = Material.objects.get(id=id)  
        form = MaterialForm(request.POST, instance = material)  
        if form.is_valid():  
            form.save()  
        return redirect("/share/more") 
    else:
        material = Material.objects.get(id=id)
        form = MaterialForm(instance = material)
    return render(request, 'share/edit.html', {'form':form})  

#Link Delete-------------
def delete_material(request, id):
    material = Material.objects.get(id=id)
    material.delete()
    return redirect('/share/more')

#Volunteers ============================================




