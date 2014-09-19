from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

@login_required
def home(request, template_name='twitcher/home.html'):
    return render_to_response(template_name=template_name)