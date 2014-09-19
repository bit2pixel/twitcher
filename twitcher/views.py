from django.shortcuts import render_to_response

def home(request, template_name='twitcher/home.html'):
    return render_to_response(template_name=template_name)