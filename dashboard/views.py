from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User

from markupeasy import settings
from api.models import Project
from api.models import ProjectFile

@login_required(login_url='/sign_in')
def dashboard(request):
    return redirect('%s%s' % (settings.LOGGED_URL, request.user.username))

@login_required(login_url='/sign_in')
def user_dashboard(request, username):
    """
    Main page of project management

    :param request: Client HTTP request
    :return: Page of the project management for the user connected
    """
    # get project list
    try:
        user = User.objects.get(username__iexact=username)
        projects = Project.objects.filter(user=user)

        # location
        project_page = get_param(request, 'project_page')
        if project_page == 'add':
            project_page = "dashboard/project_add.html"
        elif projects.count() == 0:
            project_page = "dashboard/project_empty.html"
        else:
            project_page = "dashboard/project_list.html"

        # load template with context
        template = loader.get_template('dashboard/dashboard.html')
        context = {
            'open_user': user,
            'projects': projects,
            'project_page': project_page
        }
        return HttpResponse(template.render(context, request))

    except User.DoesNotExist:
        template = loader.get_template('dashboard/404.html')
        context = {
            'username': username
        }
        return HttpResponse(template.render(context, request))


@login_required(login_url='/sign_in')
def project(request, username, project_id):
    """
    Project open page

    :param username: username owner of the project
    :param request: Client HTTP request
    :param project_id: Project Id
    :return: Page of the project details
    """
    # get project and files
    project = Project.objects.get(pk=project_id)

    # get all files in projects
    files = project.get_files()

    # load template with context
    template = loader.get_template('dashboard/project.html')
    context = {
        'project': project,
        'files': files,
        'username': username,
        'user_url': '%s%s' % (settings.LOGGED_URL, username)
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/sign_in')
def project_editor(request, username, project_id, file_name):
    """
    Project file open

    :param username: username owner of the project
    :param request: Client HTTP request
    :param project_id: Project Id
    :param file_name: File name to open in editor
    :return: Page of the project file editor
    """
    # get project and files
    project = Project.objects.get(pk=project_id)

    # get all files in projects
    files = project.get_files()

    it = iter(files)
    for file in it:
        if file.name == file_name:
            file_content = file.get_content()

    # load template with context
    template = loader.get_template('dashboard/project.html')
    context = {
        'project': project,
        'file_name': file_name,
        'file_content': file_content,
        'username': username,
        'user_url': '%s%s' % (settings.LOGGED_URL, username)
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
