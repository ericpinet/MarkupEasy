from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from api.models import Project, File
from django import template

register = template.Library()


@login_required(login_url='/sign_in')
def index(request):
    """
    Default editor without project selection.

    :param request:
    :return:
    """
    loaded_template = loader.get_template('editor/editor.html')
    context = {
        'no_footer': True,

    }
    return HttpResponse(loaded_template.render(context, request))


@login_required(login_url='/sign_in')
def project(request, project_id, file_id=None):
    """
    Open project

    :param request:
    :param project_id:
    :param file_id:
    :return:
    """
    # get project
    editor_project = Project.objects.get(pk=project_id)
    editor_file = None
    editor_files = File.objects.filter(project=editor_project)

    if file_id:
        editor_file = File.objects.get(pk=file_id)

    if editor_file is not None:
        open_file = editor_file.file
        open_file.open(mode='rb')
        data = open_file.read()
        open_file.close()

    loaded_template = loader.get_template('editor/editor.html')

    context = {
        'no_footer': True,
        'editor_project': editor_project,
        'editor_file': editor_file,
        'editor_files': editor_files,
        'editor_data': data,
    }
    return HttpResponse(loaded_template.render(context, request))
