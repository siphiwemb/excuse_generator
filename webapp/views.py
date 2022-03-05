from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .service_endpoints import excuses_url
from .forms import ExcusesForm
import requests
from .models import UserExcuse
from .serializers import UserExcuseSerializer
from django.db.models import Count
from .excuse_choices import categories


# Create your views here.

class ExcusesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, func):
        if func == 'generate':
            req_obj = {
                'category':request.query_params.get('category'),
                'num':request.query_params.get('num'),
                'user':request.user
            }
            return Response(self.generate_excuses(req_obj))
        elif func == 'user-excuses':
            user_id = request.user.id
            return Response(self.user_excuses(user_id))
        elif func == 'stats':
            user_id = request.user.id
            return Response(self.excuse_aggregation(user_id))
        elif func == 'categories':
            return Response(self.categories())


    def generate_excuses(self, req_obj):
        category, num = req_obj['category'], req_obj['num']

        form = ExcusesForm({
            'category': category,
            'number': num
        })

        if form.is_valid():
            try:
                resp = requests.get(excuses_url + f'/{category}/{num}')
                excuses = resp.json()
                user = req_obj['user']
                
                user_excuses_bulk = [
                    UserExcuse(
                        user = user,
                        excuse_category = item['category'],
                        excuse_id = item['id'],
                        excuse = item['excuse']
                    )

                    for item in excuses
                ]

                UserExcuse.objects.bulk_create(user_excuses_bulk)

                return excuses
            except Exception as err:
                return {'error': 'Exception error occured, please contact administrator.'}
        else:
            return {'error': form.errors}

    
    def user_excuses(self, user):
        user_excuses_qs = UserExcuse.objects.filter(user=user)
        serializer = UserExcuseSerializer(user_excuses_qs, many=True)
        return serializer.data

    
    def excuse_aggregation(self, user):
        user_excuses_qs = UserExcuse.objects.filter(user=user).values("user", "excuse_category").annotate(Count("excuse_id"))
        return user_excuses_qs

    
    def categories(self):
        categories_lst = [item[0] for item in categories]
        return categories_lst


