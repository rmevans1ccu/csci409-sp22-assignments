from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello from routes');

def route_search(request, origin, destination):
    return HttpResponse('Showing routes from ' + origin + ' to ' + destination)