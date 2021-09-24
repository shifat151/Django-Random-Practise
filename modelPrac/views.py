from django.shortcuts import render, redirect, get_object_or_404
from .forms import DocumentForm
from account.models import Parent

# Create your views here.

def testModel(request):
    if request.method == 'POST':
        signupform = DocumentForm(request.POST)
        if signupform.is_valid():
            print('yes')
            return render(request, 'modelPrac/formPractise.html', {'form':signupform})
        else:
            return render(request, 'modelPrac/formPractise.html', {'form':signupform})


        
        
    else:
        parents=get_object_or_404(Parent, id=2)
        child=parents.padres.all()

        signupform = DocumentForm(request.POST)
        return render(request, 'modelPrac/formPractise.html', {'form':signupform, 'childs':child})



    


