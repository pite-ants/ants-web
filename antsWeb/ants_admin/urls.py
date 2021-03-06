from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^admin/$', views.admin_students, name='admin'),
    url(r'^admin/students/$', views.admin_students, name='admin_students'),
    url(r'^admin/student/reset/(?P<student_id>[0-9]+)/$', views.admin_student_reset, name='admin_student_reset'),
    url(r'^admin/student/promote/(?P<student_id>[0-9]+)/$', views.admin_student_reset, name='admin_student_promote'),
    url(r'^admin/student/demote/(?P<student_id>[0-9]+)/$', views.admin_student_reset, name='admin_student_demote'),
    url(r'^admin/course/delete/(?P<course_id>[0-9]+)/$', views.admin_course_delete, name='admin_course_delete'),
    url(r'^admin/term/delete/(?P<term_id>[0-9]+)/$', views.admin_term_delete, name='admin_term_delete'),
    url(r'^admin/terms/$', views.admin_terms, name='admin_terms'),
    url(r'^admin/unavailable_terms/$', views.admin_unavailable_terms, name='admin_unavailable_terms'),
    url(r'^admin/unavailable_terms/(?P<selection_id>[0-9]+)/$', views.admin_unavailable_terms,
        name='admin_unavailable_terms'),
    url(r'^admin/settings/$', views.admin_settings, name='admin_settings'),
]
