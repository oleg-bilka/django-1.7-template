import time
from .models import HTTPRequest


class ViewTimingMiddleware(object):
    def process_request(self, request):
        request.start = time.time()

    def process_response(self, request, response):
        duration = int(round((time.time() - request.start ) * 1000))
        person, created = HTTPRequest.objects.get_or_create(url=request.path,
                                                            defaults={'duration': duration, 'method': request.method})
        return response