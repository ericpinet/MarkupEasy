from rest_framework.routers import DefaultRouter

from api.projects import ProjectViewSet
from api.users import UserViewSet

# router REST api
router = DefaultRouter()
router.register(r'users', UserViewSet, base_name='user')
router.register(r'projects', ProjectViewSet, base_name='project')

# Mix router with URLS
urlpatterns = router.urls
