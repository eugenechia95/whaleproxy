from django.test import TestCase

class GetViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    #tests for getview

    def test_getview_url_exists_at_desired_location(self):
        response = self.client.get('/whales', HTTP_AUTHORIZATION = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1ODMxOTkzMTQsImlkIjoiRXVnZW5lX0NoaWFAbXltYWlsLnN1dGQuZWR1LnNnIiwib3JpZ19pYXQiOjE1NTEwNTg1MTR9.kNx9zaYjQAyn6dQSxdTIQHVoy9K1h32Bm5MTxXj91Iw")
        self.assertEqual(response.status_code, 200)

    def test_getview_url_denied_noauthentication(self):
        response = self.client.get('/whales')
        self.assertEqual(response.status_code, 401)

    def test_getview_post_denied_noauthentication(self):
        response = self.client.post('/whales')
        self.assertEqual(response.status_code, 401)

    def test_getview_force_purge(self):
        response = self.client.delete('/whales', HTTP_AUTHORIZATION = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1ODMxOTkzMTQsImlkIjoiRXVnZW5lX0NoaWFAbXltYWlsLnN1dGQuZWR1LnNnIiwib3JpZ19pYXQiOjE1NTEwNTg1MTR9.kNx9zaYjQAyn6dQSxdTIQHVoy9K1h32Bm5MTxXj91Iw")
        self.assertEqual(response.status_code, 204)

    def test_getview_force_purge_denied_noauthentication(self):
        response = self.client.delete('/whales')
        self.assertEqual(response.status_code, 401)

    def test_getview_force_sync(self):
        response = self.client.put('/whales', HTTP_AUTHORIZATION = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1ODMxOTkzMTQsImlkIjoiRXVnZW5lX0NoaWFAbXltYWlsLnN1dGQuZWR1LnNnIiwib3JpZ19pYXQiOjE1NTEwNTg1MTR9.kNx9zaYjQAyn6dQSxdTIQHVoy9K1h32Bm5MTxXj91Iw")
        self.assertEqual(response.status_code, 200)

    def test_getview_force_sync_checkresponse(self):
        response = self.client.put('/whales', HTTP_AUTHORIZATION = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1ODMxOTkzMTQsImlkIjoiRXVnZW5lX0NoaWFAbXltYWlsLnN1dGQuZWR1LnNnIiwib3JpZ19pYXQiOjE1NTEwNTg1MTR9.kNx9zaYjQAyn6dQSxdTIQHVoy9K1h32Bm5MTxXj91Iw")
        self.assertEqual(response.content, b'All Whales Synced!')

    def test_getview_force_sync_denied_noauthentication(self):
        response = self.client.put('/whales')
        self.assertEqual(response.status_code, 401)

    #tests for getidview

    def test_getidview_url_exists_at_desired_location(self):
        response = self.client.get('/whales/69', HTTP_AUTHORIZATION = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1ODMxOTkzMTQsImlkIjoiRXVnZW5lX0NoaWFAbXltYWlsLnN1dGQuZWR1LnNnIiwib3JpZ19pYXQiOjE1NTEwNTg1MTR9.kNx9zaYjQAyn6dQSxdTIQHVoy9K1h32Bm5MTxXj91Iw")
        self.assertEqual(response.status_code, 200)

    def test_getidview_url_denied_noauthentication(self):
        response = self.client.get('/whales/20')
        self.assertEqual(response.status_code, 401)

    #tests for hitratio

    def test_hitratio_url_denied_noauthentication(self):
        response = self.client.get('/hitratio')
        self.assertEqual(response.status_code, 401)