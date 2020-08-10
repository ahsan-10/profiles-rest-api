from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """testing APIViews """

    def get(self, request, format = None):
        """ Returns a list of APIView features """

        an_apiview = [
            'Uses HTTP methods as function(get,post,patch,put,delete)',
            'Is similar to a traditional django views',
            'Gives us the most control over application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello', 'an_apiview': an_apiview})
