from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import User
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse

def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # on récupère l'objet User créé
            return redirect('bienvenue', user_id=user.id)  # on passe l'id
    else:
        form = SignUpForm()
    return render(request, 'app/form.html', {'form': form})

def bienvenue(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'app/bienvenue.html', {'user': user})

def generer_pdf_recu(request, user_id):
    user = User.objects.get(id=user_id)
    template = get_template('app/recu_inscription.html')
    html = template.render({'user': user})

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="recu_inscription.pdf"'
    pisa.CreatePDF(html, dest=response)
    return response