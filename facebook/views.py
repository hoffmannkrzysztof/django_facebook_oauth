import urllib

from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils.translation import ugettext as _

def login(request):
    """ First step of process, redirects user to facebook, which redirects to authentication_callback. """

    redirect_uri = request.GET.get('redirect_uri','/')

    if not redirect_uri:
        redirect_uri = '/'

    args = {
        'client_id': settings.FACEBOOK_APP_ID,
        'scope': settings.FACEBOOK_SCOPE,
        'redirect_uri': request.build_absolute_uri(redirect_uri),
    }
    return HttpResponseRedirect('https://www.facebook.com/dialog/oauth?' + urllib.urlencode(args))
