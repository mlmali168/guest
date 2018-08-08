

# Create your tests here.
from django.test import TestCase
from guest.sign.models import Event
from guest.sign.models import Guest


# Create your tests here.
class ModelTest(TestCase):

    def setUp(self):
        Event.objects.create(id=18, name="one_plus 3 event", status=True, limit=2000, address='深圳',
                             start_time='2016-08-31 02:18:22')
        Guest.objects.create(id=20, event_id=18, real_name='a_len', phone='13711001110',
                             email='alen@163.com', sign=False)

    def test_event_models(self):
        result = Event.objects.get(name="one_plus 3 event")
        self.assertEqual(result.address, "深圳")
        self.assertTrue(result.status)

    def test_guest_models(self):
        result = Guest.objects.get(phone='13711001110')
        self.assertEqual(result.real_name, "a_len")
        self.assertFalse(result.sign)


