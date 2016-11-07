from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/sign_in')
def index(request):
    title = "MarkupEasy"
    template = loader.get_template('editor/index.html')
    context = {
        'title': title,
    }
    return HttpResponse(template.render(context, request))
