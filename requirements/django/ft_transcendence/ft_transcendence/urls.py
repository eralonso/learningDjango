"""
URL configuration for ft_transcendence project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from views import path

#view only for testing
from django.http import HttpResponse

def printHeaders(request):
	res = HttpResponse(content_type="text/plain")
	res.write('\n'.join([f'{key}: {value}' for key, value in request.META.items()]));
	res.write("\n\nHttpResponse\n")
	res.write('\n'.join([f'{key}: {value}' for key, value in res.headers.items()]))
	print("NEW REQUEST:\n{0}\n\n".format('\n'.join([f'{key}: {value}' for key, value in request.META.items()])))
	return res

urlpatterns = [
    path('', printHeaders, name="printHeaders"),
    path('admin/', admin.site.urls),
]
