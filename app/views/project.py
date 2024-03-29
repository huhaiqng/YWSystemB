from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from guardian.shortcuts import get_objects_for_user
from app.drf.viewsets import CheckPermViewSet
from app.models import Project
from app.serializers import GetProjectSerializer, ProjectSerializer


# 项目
class ProjectViewSet(CheckPermViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class GetProjectViewSet(CheckPermViewSet):
    queryset = Project.objects.all()
    serializer_class = GetProjectSerializer
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        page_size = request.GET.get('limit')
        sort = request.GET.get('sort')
        name = request.GET.get('name')
        if int(page_size) == 10000:
            PageNumberPagination.page_size = None
        else:
            PageNumberPagination.page_size = page_size
        objects = Project.objects.filter(sort__contains=sort, name__contains=name)
        queryset = get_objects_for_user(request.user, 'app.view_%s' % self.basename, objects)
        page = self.paginate_queryset(queryset)

        # 将 PageNumberPagination.page_size 设置为 None 以免影响其它查询
        PageNumberPagination.page_size = None
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
