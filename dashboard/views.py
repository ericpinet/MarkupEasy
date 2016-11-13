from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

from api.models import Project


@login_required(login_url='/sign_in')
def dashboard(request):
    """
    Main page of project management

    :param request: Client HTTP request
    :return: Page of the project management for the user connected
    """

    projects = Project.objects.filter(user=request.user)
    projects_page = get_param(request, 'projects_page')

    if projects_page == 'add':
        projects_page = "dashboard/projects_add.html"
    elif projects.count() == 0:
        projects_page = "dashboard/projects_empty.html"
    else:
        projects_page = "dashboard/projects_list.html"

    template = loader.get_template('dashboard/dashboard.html')
    context = {
        'projects': projects,
        'projects_page': projects_page
    }
    return HttpResponse(template.render(context, request))


def get_param(request, param_name):
    """
    Return the GET or POST parameter value.

    :param request: Client http request
    :param param_name: Parameter name to return
    :return: None if not found
    """
    if request.method == 'GET':
        ret = request.GET.get(param_name)
    elif request.method == 'POST':
        ret = request.POST.get(param_name)

    return ret;