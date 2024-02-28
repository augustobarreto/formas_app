from http import HTTPStatus
from unittest import TestCase

from django.test import Client


class HealthCheckTestCase(TestCase):
    def test_status_ok(self):
        c = Client()
        response = c.get('/api/v1/healthcheck/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.json(), {'status': 'ok'})
