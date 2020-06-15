from django.views.generic import View
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from django.core.serializers.json import DjangoJSONEncoder

from .models import Results


class MobileAppApiView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(MobileAppApiView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        results = Results.objects.values('id', 'name', 'measdate', 'comment', 'data',
                                         'setid__name', 'setid__description',
                                         'typeid__description')

        return HttpResponse(json.dumps(list(results), cls=DjangoJSONEncoder))

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        experiments_ids = data.get('id')

        result = Results.objects.filter(id=int(experiments_ids)).first()

        result.name = data.get('name')
        result.measdate = data.get('measdate')
        result.comment = data.get('comment')
        result.data = data.get('data')

        # save changes (it's better to replace this to bulk_update
        result.save()

        # Prepare data for json response
        # res = result.values('id', 'name', 'measdate', 'comment', 'data',
        #                      'setid__name', 'setid__description',
        #                      'typeid__description')
        res = {'id': result.id, 'name': result.name, 'measdate': result.measdate, 'comment': result.data}

        return HttpResponse(json.dumps(list(res), cls=DjangoJSONEncoder))
