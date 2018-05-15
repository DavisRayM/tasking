# -*- coding: utf-8 -*-
"""
Tasking urls module.
"""
from django.conf.urls import include, url
from rest_framework import routers

from tasking.viewsets import TaskViewSet, ProjectViewSet

router = routers.DefaultRouter(trailing_slash=False)  # pylint: disable=C0103
router.register(r'tasks', TaskViewSet)
router.register(r'tasks', ProjectViewSet)

urlpatterns = [  # pylint: disable=C0103
    url(r'^api/v1/', include(router.urls)),
]
