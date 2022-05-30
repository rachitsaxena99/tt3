
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('article.urls')),
    path('accounts/' , include('accounts.urls')),
    path('doubt/' , include('doubt.urls')),
    path('question/' , include('question.urls')),
    path('notes/', include('notes.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

