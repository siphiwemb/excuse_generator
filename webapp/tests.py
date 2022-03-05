from django.test import TestCase
from .models import (UserExcuse, User)
from .views import ExcusesView

# Create your tests here.
class ExcuseTestCase(TestCase):
    def setUp(self):
        # create a user 
        user1 = User.objects.create(username="user1", first_name="usertest1", last_name="last1",
        password="kuytdas1s")


    def test_excuses_view(self):
        """ExcusesView methods return expected responses"""

        EV = ExcusesView()
        user1 = User.objects.get(username="user1")
        

        # 1. assert that len of UserExcuse objects is equals to req_obj.num after calling generate_excuses
        req_obj = {
                'category': 'family',
                'num': 2,
                'user': user1
            }

        gen_exc = EV.generate_excuses(req_obj)
        check_stored = UserExcuse.objects.filter(user=user1.id).values()
        self.assertEqual(len(check_stored), 2)


        # 2. assert that excuse_aggregation = expected_aggr_resp which is the expected response
        excuse_aggr = EV.excuse_aggregation(user1.id)
        expected_aggr_resp = [{
            'excuse_category': 'family',
            'excuse_id__count': 2,
            'user': 1
        }]
        self.assertEqual(list(excuse_aggr), expected_aggr_resp)

        
        
        