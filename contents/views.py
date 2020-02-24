import json

from django.contrib.auth import logout, authenticate, login
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_http_methods
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Template
from api.serializers import UserSerializer, TemplateDetailSerializer


@require_http_methods(["GET", "POST"])
def logout_view(request):
    logout(request)
    return JsonResponse({})


@require_http_methods(["POST"])
def login_view(request):
    data = json.loads(request.body)
    user = authenticate(username=data['email'], password=data['password'])
    if user is not None:
        if user.is_active and user.is_staff:
            login(request, user)
            return user_state(request)
    return JsonResponse({'error': u'Неверные логин или пароль'})


@require_http_methods(["GET", "POST"])
def user_state(request):
    if request.user.is_active:
        return JsonResponse({'user': UserSerializer(request.user).data})
    return JsonResponse({'user': False})


class TemplateViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post']
    queryset = Template.objects.all().order_by('-created_at')
    serializer_class = TemplateDetailSerializer
    #
    # @action(detail=True, methods=['post'])
    # def rating(self, request, pk=None):
    #     stage = self.get_object()
    #     stat, create = PitchStatistic.objects.get_or_create(user=self.request.user, command_id=request.data['id'],
    #                                                         stage=stage)
    #     if request.data.get('comment', False):
    #         stat.comment = request.data['comment']
    #
    #     for char in request.data['characters']:
    #         character, created = PitchStatisticPoint.objects.get_or_create(stat=stat, character_id=char['id'])
    #         character.point = char['current']
    #         character.save()
    #     stat.total = stat.points.aggregate(sum=Sum('point'))['sum']
    #     stat.ended = True
    #     stat.save()
    #     return Response(CommandStageSerializer(stat.command, context={'stage': stage, 'request': request}).data)
    #
    # @action(detail=True, methods=['get'])
    # def filters(self, request, pk=None):
    #     stage = self.get_object()
    #     return Response({'stage': {'pitch_name': stage.pitch.name, 'ended': stage.ended, 'accept': not stage.stats.filter(accept=False).exists()},
    #                      'command': CommandSerializer(self.request.user.command).data,
    #                      'criteria': stage.characters.values('id', 'name')
    #                      })
    #
    # @action(detail=True, methods=['post'])
    # def change(self, request, pk=None):
    #     stage = self.get_object()
    #     stage.ended = request.data['ended']
    #     # stage.accept = request.data['accept']
    #     stage.save()
    #     return Response('Ok')
    #
    # @action(detail=True, methods=['post'])
    # def save_points(self, request, pk=None):
    #     stage = self.get_object()
    #
    #     for command in request.data:
    #         for char in command['characters']:
    #             stat = PitchStatistic.objects.get(id=char['id'])
    #             stat.accept = True
    #             for point in char['points']:
    #                 p_obj = stat.points.get(id=point['id'])
    #                 p_obj.point = point['current']
    #                 p_obj.save()
    #             stat.save()
    #     stage.accept = True
    #     stage.save()
    #     return Response('Ok')
    #
    # @action(detail=True, methods=['get'])
    # def admin(self, request, pk=None):
    #     stage = self.get_object()
    #
    #     return Response(StageDetailAdminSerializer(stage, context={'stage': stage, 'request': request}).data)
