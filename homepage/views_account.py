from django.shortcuts import render, redirect

def v_sign_up(request):
    return  render(request, 'homepage/account/sign_up.html')

def v_sign_up_create(request):
    if request.method == 'POST':
        data = request.POST.copy()
        print('=>>>>>>>', data)

        import os
        import resend
        resend.api_key = 're_Kn78HRwU_F7uK8HejaweGxsExXpUxqpnE'
        params: resend.Emails.SendParams = {
            'from': 'Bichito <robot@resend.equisd.com>',
            'to': [data['email']],
            'subject': 'Patitas te da la bienvenida!!',
            'html': '<h2>Ya eres parte de Patitas!</h2>'
        }
        email_id = resend.Emails.send(params)



        return redirect('/sign_up/thank_you')
    return redirect('/')

def v_sign_up_thank_you(request):
    return render(request, 'homepage/account/thank_you.html')

def v_sign_in(request):
    return render(request, 'homepage/account/sign_in.html')

def v_sign_in_login(request):
    if request.method == 'POST':
        data = request.POST.copy()
        print('=>>>>>>>', data)

        return redirect('/sign_in/welcome')
    return redirect('/')

def v_welcome(request):
    return render(request, 'homepage/account/sign_in_welcome.html')