from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/sign_in')
def dashboard(request):
    """
    Main page of project management

    :param request: Client HTTP request
    :return: Page of the project management for the user connected
    """
    template = loader.get_template('dashboard/dashboard.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

