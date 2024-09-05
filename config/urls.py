"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path

from pybo import views
from pybo.views import base_views

# url안에 views는 기본
# 근데 pybo url안에 views를 쓰는게낫지
# config url안에 pybo views를 쓰는건 좀아님
# 그렇기때문에 pybo url안에 views를 쓰고 그 pybo url을 include하는게 적함
# pybo앱관련은 pybo앱 디렉터리하위에있어야하므로
# url 매핑할때마다 config/urls를 수정하면안되니 그냥 알아서 추가되게 include써줌
urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/',include('pybo.urls')),
    path('common/',include('common.urls')),
    path('',base_views.index,name='index')
    #  '/' 에해당는 path
    # views를 가져와서 연결시켜야함
    # admin/은 원ㄹ래이씀
]
