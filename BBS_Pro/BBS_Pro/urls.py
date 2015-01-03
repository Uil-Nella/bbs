from django.conf.urls import include, url
from django.contrib import admin

import app01.urls


urlpatterns = [
    # Examples:
    # url(r'^$', 'BBS_Pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(app01.urls)),
]
