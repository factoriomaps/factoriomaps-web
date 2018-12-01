from rest_framework import routers

import maps.views

router = routers.SimpleRouter()
router.register(r'map', maps.views.MapViewSet)
router.register(r'mod', maps.views.ModViewSet)

urlpatterns = router.urls
