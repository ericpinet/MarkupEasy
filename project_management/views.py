from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/sign_in')
def projects_dashboard(request):
    template = loader.get_template('project_management/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))