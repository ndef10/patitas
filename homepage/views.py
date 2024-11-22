from django.shortcuts import render

# Create your views here.
def v_index(request):
    context = {
        'providers': [
            {
                'first_name': 'Marta',
                'last_name': 'Rojas',
                'photo': 'https://whoofpoint.com/media/images/card_id/profile_40442120.png '
            },
            {
                'first_name': 'Mariana',
                'last_name': 'Mora',
                'photo': 'https://whoofpoint.com/media/images/card_id/profile__z9pMJfk.png'
            },
            {
                'first_name': 'Felicia',
                'last_name': 'Hidalgo',
                'photo': 'https://whoofpoint.com/media/images/card_id/profile__Bxs38Zm.png'
            },
            {
                'first_name': 'Daniela',
                'last_name': 'Valdivieso',
                'photo': 'https://whoofpoint.com/media/images/card_id/profile__Hbemmoz.png'
            },
            {
                'first_name': 'Juana',
                'last_name': 'Lagos',
                'photo': 'https://whoofpoint.com/media/images/card_id/profile_75449101.png'
            },
            {
                'first_name': 'Rafaela',
                'last_name': 'Arana',
                'photo': 'https://whoofpoint.com/media/images/card_id/profile_74944414_nzUOEwk.png'
            },
            {
                'first_name': 'Pablo',
                'last_name': 'Acevedo',
                'photo': 'https://whoofpoint.com/media/images/card_id/profile_73870520.png'
            },
            {
                'first_name': 'Carla',
                'last_name': 'Rojas',
                'photo': 'https://whoofpoint.com/media/images/card_id/profile_40442120.png '
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