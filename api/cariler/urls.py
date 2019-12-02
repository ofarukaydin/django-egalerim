from rest_framework.routers import DefaultRouter
from api.views import CarilerViewSet

router = DefaultRouter()
router.register(r'', CarilerViewSet, base_name='cariler')
urlpatterns = router.urls
