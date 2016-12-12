from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

from dashboard.views import get_param
from markupeasy import settings


# Create your views here.


@csrf_protect
def index(request):
    """
    Main page

    :type request: Request
    :param request: Client http request
    :return: Main page
    """
    home_page = get_param(request, 'home_page')

    if home_page != 'True':
        if request.user.is_authenticated:
            return redirect('%s%s' % (settings.LOGGED_URL, request.user.username))

    template = loader.get_template('homepage/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def join(request):
    """
    API request to create new user
    :param request: Client http request
    :return:
    """

    join_request = False
    username_error = None
    email_error = None
    password_error = None
    user = None

    # check for the creation of the new account
    if request.POST:

        username = request.POST['user_login']
        email = request.POST['user_email']
        password = request.POST['user_password']

        if username is None or username == '':
            username_error = 'Enter a username!'

        if email is None or email == '':
            email_error = 'Enter a valid email!'

        if password is None or password == '':
            password_error = 'Enter a valid password!'

        if username_error is None and email_error is None and password_error is None:

            # check if username already exist
            user_count = User.objects.filter(username=username).count()
            if user_count > 0:
                username_error = 'Username is already used.'

            # check if email already exist
            email_count = User.objects.filter(email=email).count()
            if email_count > 0:
                email_error = 'Email is already used.'

            if user_count == 0 and email_count == 0:
                # create the new user
                user = User.objects.create_user(username, email, password)

        if user is not None:
            user.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('%s%s' % (settings.LOGGED_URL, request.user.username))

    template = loader.get_template('homepage/index.html')
    context = {
        'join_request': join_request,
        'username_error': username_error,
        'email_error': email_error,
        'password_error': password_error,
    }
    return HttpResponse(template.render(context, request))


def sign_in(request):
    """
    Sign in page

    :param request: Client http request
    :return: Sign in page
    """

    username_error = None
    password_error = None
    login_error = None

    # check login
    if request.POST:

        username = request.POST['user_login']
        password = request.POST['user_password']

        if username is None or username == '':
            username_error = 'Enter a username!'

        if password is None or password == '':
            password_error = 'Enter a valid password!'

        if username_error is None and password_error is None:
            user = authenticate(username=username, password=password)

            if user is None:
                login_error = 'Invalid username or password!'
            else:
                login(request, user)
                return redirect('%s%s' % (settings.LOGGED_URL, request.user.username))

    template = loader.get_template('homepage/index.html')
    context = {
        'sign_in': True,
        'login_error': login_error,
    }
    return HttpResponse(template.render(context, request))


def sign_out(request):
    """
    Sign out page. Logout user and redirect to home.

    :param request: Client http request.
    :return: Home page
    """

    # Logout current user
    if request.user.is_authenticated:
        logout(request)

    template = loader.get_template('homepage/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
