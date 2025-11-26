from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import logout

class DisableClientCacheMiddleware(MiddlewareMixin):
    

    def process_request(self, request):
        
        if request.user.is_authenticated and not request.session.session_key:
            logout(request)
            request.session.flush()

    def process_response(self, request, response):
        
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate, max-age=0'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'

        
        response['Vary'] = 'Cookie'
        return response
