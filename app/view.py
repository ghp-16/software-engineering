from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect
from django.shortcuts import render

import requests
import uuid


def login(request):
    if request.method == 'GET':
        code = request.GET.get('code')
        if code:
            # Here is the callback of the oauth server
            state = request.GET.get('state', None)
            if state != request.session.get('state'):
                # Under attack!
                return HttpResponseBadRequest()
            else:
                status_code = fetch_userinfo(request, code)
                if status_code != 200:
                    return HttpResponse(status_code)
                else:
                    return redirect('/')
        else:
            # Before login
            request.session['state'] = str(uuid.uuid4())
            context = {'OAUTH_AUTH_URL': getattr(settings, 'OAUTH_AUTH_URL'),
                       'CLIENT_ID': getattr(settings, 'CLIENT_ID')}
            return render(request, 'index.html', context)
    else:
        return HttpResponseNotAllowed(['GET'])


def logout(request):
    if 'user' in request.session:
        del request.session['user']
    return redirect('/')


def fetch_userinfo(req, code):
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'client_id': getattr(settings, 'CLIENT_ID'),
        'client_secret': getattr(settings, 'CLIENT_SECRET'),
    }
    '''
    status_code:
      - 401: unauthorized
      - 200: {
          'access_token': 'An access token',
          'expires_in': 3600,  # seconds later, this token will expire
    '''
    response = requests.post(getattr(settings, 'OAUTH_TOKEN_URL'), data=data)
    if response.status_code == 200:
        token = response.json()['access_token']
    else:
        return response.status_code
    headers = {
        'Authorization': 'Bearer ' + token,
    }
    '''
    expect result: {
        'data': {
            'provider': 'sepi',
            'id': 'user id',
            'user': {
                'type': 'Student',  # or 'Admin'
                'name': 'student id',  # shown on the student card
                'email': 'a fake email',
            }
        }
    }
    '''
    response = requests.get(getattr(settings, 'OAUTH_USERINFO_URL'),
                            headers=headers)
    if response.status_code == 200:
        data = response.json()['data']
        user = {
            'id': data['id'],
            'name': data['user']['name'],
        }
        req.session['user'] = user
    return response.status_code
