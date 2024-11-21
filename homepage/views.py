from django.shortcuts import render

# Create your views here.
def v_index(request):
    context = {
        'providers': [
            {
                'first_name': 'Pepito',
                'last_name': 'Rojas'
            },
            {
                'first_name': 'Carlos',
                'last_name': 'Mora'
            },
            {
                'first_name': 'Felix',
                'last_name': 'Hidalgo',
                'photo': 'https://whoofpoint.com/media/images/card_id/profile_73870520.png'
            },
            {
                'first_name': 'Daniel',
                'last_name': 'Valdivieso'
            },
            {
                'first_name': 'Juana',
                'last_name': 'Lagos'
            },
            {
                'first_name': 'Rene',
                'last_name': 'Arana'
            },
            {
                'first_name': 'Paula',
                'last_name': 'Acevedo',
                'photo': 'https://whoofpoint.com/media/images/card_id/profile_73870520.png'
            }
        ]
    }
    return render(request, 'homepage/index.html', context)

def v_feedback_gracias(request):
    return render(request,  'homepage/feedback_gracias.html')

from django.shortcuts import redirect
def v_feedback_create(request):
    if request.method == "POST":
        data = request.POST.copy()
        print('++', data)
        # guardar base de datos
        # guardar en csv, excel....
        return redirect('/feedback/gracias')
    return redirect('/')