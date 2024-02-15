from rest_framework.views import APIView
from rest_framework.response import Response
import requests


class CustomAPIView(APIView):


    def post(self, request):
        url = 'http://tts.ulut.kg/api/tts'
        token = '8Yj2gma3fu13mOG6PV9OLu8k8QoBeOVVEzfrpDy6qzEk1bHQdpK9K9M5XZcacKo5'
        data = request.data

        headers = {'Authorization': f'Bearer {token}'}

        response = requests.post(url, headers=headers, data=data)

        if response.status_code == 200:
            return Response(response.json())
        else:
            return Response(response.text, status=response.status_code)








