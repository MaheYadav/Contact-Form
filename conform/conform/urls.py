from django.conf.urls import include, url
from django.contrib import admin
from conapp import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'conform.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.contactview)
]
