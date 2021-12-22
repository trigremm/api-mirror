from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET", "POST"])
def mirror(request):
    data = {
        "data": request.data if request.method == "POST" else request.query_params,
        "headers": str(request.headers),
        "meta": str(request.META),
    }
    status_code = status.HTTP_200_OK
    return Response(data=data, status=status_code, content_type=None)
