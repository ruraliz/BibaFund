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
    path('user/<username>', views.profile, name="profile"),
    # path('fund/<int:pk>/update', views.FundUpdate.as_view(), name='funds_update'),
    # path('fund/<int:pk>/delete', views.FundDelete.as_view(), name='funds_delete'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup_view, name='signup'),
 ]