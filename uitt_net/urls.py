"""uitt_net URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from landing import views
from landing.views import send_message

if settings.UNDER_CONSTRUCTION:
    urlpatterns=[
    url(r'^$', views.undr_const, name='const'),
    ]
else:
    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^$', views.home_view, name='home'),
        url(r'^about/$', views.about_view, name='about'),
        url(r'^contacts/$', views.contacts_view, name='contacts'),
        url(r'^send-message/$', send_message, name='message'),
        url(r'^summernote/', include('django_summernote.urls')),
        url(r'^option/(?P<option_slug>[-\w]+)/$', views.options_view, name='options'),
        url(r'^feature/(?P<feature_slug>[-\w]+)/$', views.features_view, name='features'),
    ]

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()

