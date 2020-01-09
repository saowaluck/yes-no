from django.test import TestCase
from django.urls import reverse

from answers.models import Answer


# Create your tests here.
class CreateAnswerViewTest(TestCase):
    def test_create_answer_should_save_model(self):
        response = self.client.post(reverse('create_answer_class_views'), data={
            'text': 'Yes',
            'image': 'image_url'
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/answer/')

        answer = Answer.objects.last()

        self.assertEqual(answer.text, 'Yes')
        self.assertEqual(answer.image, 'image_url')
