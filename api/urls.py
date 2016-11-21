from rest_framework.routers import DefaultRouter

from api.projects import ProjectViewSet
from api.users import UserViewSet
from api.files import FileViewSet

# router REST api
router = DefaultRouter()
router.register(r'users', UserViewSet, base_name='user')
router.register(r'projects', ProjectViewSet, base_name='project')
router.register(r'files', FileViewSet, base_name='file')

# Mix router with URLS
urlpatterns = router.urls
