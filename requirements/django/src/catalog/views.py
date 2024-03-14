from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.
def printHeaders(request):
	res = HttpResponse(content_type="text/plain")
	res.write('\n'.join([f'{key}: {value}' for key, value in request.META.items()]));
	res.write("\n\nHttpResponse\n")
	res.write('\n'.join([f'{key}: {value}' for key, value in res.headers.items()]))
	res.write(f"\nserver gateway interface: {os.environ.get('SERVER_GATEWAY_INTERFACE')}\n")
	print("NEW REQUEST:\n{0}\n\n".format('\n'.join([f'{key}: {value}' for key, value in request.META.items()])))
	return res