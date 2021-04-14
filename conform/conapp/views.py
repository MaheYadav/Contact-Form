from django.shortcuts import render
from .models import ContactData
from .forms import Contactform
def contactview(request):
    if request.method == "POST":
        cform = Contactform(request.POST)
        if cform.is_valid():
            first_name = request.POST.get('first_name', '')
            last_name = request.POST.get('last_name', '')
            salary = request.POST.get('salary', '')
            location = request.POST.get('location', '')
            mobile = request.POST.get('mobile', '')

            data = ContactData(
                first_name=first_name,
                last_name=last_name,
                salary=salary,
                location=location,
                mobile=mobile
            )
            data.save()
            cform = Contactform()
            return render(request, 'contactform.html', {'cform': cform})

    else:
        cform = Contactform()
        return render(request, 'contactform.html', {'cform': cform})

