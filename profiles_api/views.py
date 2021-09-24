from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test Api view"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
        'uses HTTP methods as function (get, post, patch, put, delete)',
        'Is similar to traditational Django view',
        'Gives you most control over your logic',
        'Is mapped manually to URLs',

        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})
