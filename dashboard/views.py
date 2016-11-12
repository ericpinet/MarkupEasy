from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.response import Response

from dashboard.models import Project
import json

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


@login_required(login_url='/sign_in')
def save_personal_information(request):
    """
    Save the user personal information from the POST data.

    :param request: Client HTTP request
    :return: Status request in json
    """
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        response_data = {}

        # do not save user data with no email
        if email is None or email is "":
            response_data['result'] = '500'
            response_data['msg'] = 'Email is empty!'

        else:
            try:
                request.user.first_name = first_name
                request.user.last_name = last_name
                request.user.email = email

                request.user.save()

                response_data['result'] = '200'
                response_data['msg'] = 'Save successful!'

            except Exception as err:
                response_data['result'] = '500'
                response_data['msg'] = "Unexpected error:" + err


        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"result": "Work only in POST methode."}),
            content_type="application/json"
        )


class ProjectInputSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=1)


class ProjectOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'creation_date')



class ProjectViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Project.objects.all()
        serializer = ProjectOutputSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Project.objects.all()
        project = get_object_or_404(queryset, pk=pk)
        serializer = ProjectOutputSerializer(project)
        return Response(serializer.data)
