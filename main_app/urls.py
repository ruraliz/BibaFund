from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('investment/', views.investment, name='investment'),
    path('team/', views.team, name='team'),
    path('fund/', views.fund, name='fund'),
    path('job/', views.job, name='job'),
    path('fund/<int:fund_id>', views.fund_apply, name='fund_apply'),
    path('job/<int:job_id>', views.job_apply, name='job_apply'),
    path('user/<username>/', views.profile, name="profile"),
    path('activity/<username>/', views.activity, name="activity"),
    path('activity/create', views.ActivityCreate.as_view(), name='activity_create'),
    path('activity/<int:pk>/update', views.ActivityUpdate.as_view(), name='activity_update'),
    path('activity/<int:pk>/delete', views.ActivityDelete.as_view(), name='activity_delete'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup_view, name='signup'),
 ]