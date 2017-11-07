from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from firstapp.forms import Payment
# from firstapp.models import Home

# Create your views here.
def payment(request):
    
    context = {'form': payment}
    if request.method == "POST":
        form = payment(request.POST)
        if form.is_valid():
                form.save()
                return redirect('payment_index.html')
        else :
            return render(request, 'payment_index.html', 
                          {'form': form})
    else :
        return render(
            request,
            'payment_index.html',
            context
        )


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    