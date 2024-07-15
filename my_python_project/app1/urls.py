from django.contrib import admin
from django.urls import path,include 
from. import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
path('index1',views.index1),
path('adddoctor',views.adddoctor),
path('doctoradviews',views.doctoradviews),
path('doctordelete/<int:id>',views.doctordelete,name="doctordelete"),
path('doctorupdate/<int:id>',views.doctorupdate,name="doctorupdate"),
path('doctorupdate/doctor_update/<int:id>',views.doctor_update,name="doctor_update"),
path('adminprofile',views.adminprofile),

]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)