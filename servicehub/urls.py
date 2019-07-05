from django.urls import path
from .import views

urlpatterns = [
	path('registrationpage/',views.registerPage,name="registrationpage"),
    path('login/',views.LoginPage,name="login"),
    path('index/',views.index,name="index"),
    path('registration/',views.registration,name="registration"),
    path('login_evaluation/',views.login_evaluation,name="login_evaluation"),
    path('forgotPage/' ,views.forgotPage,name="forgotPage"),
    path('forgotPassword/',views.forgotPassword,name="forgotPassword"),
    path('reset_password/',views.ResetPassword,name="reset_password"),
    path('homepage/',views.Homepage,name="homepage"),
    path('logout/',views.logout,name="logout"),
    path('service_list/',views.Service_list,name="servicelist"),
    path('feedbacks/',views.feedbacks,name="feedbacks"),
    path('getfeedback/',views.getfeedback,name="getfeedback"),
	path('subcat/<int:pk>',views.sub_cat,name="sub_cat"),
	path('service3/',views.service3,name="service3"),
    path('service1/',views.service1,name="service1"),
    path('service2/',views.service2,name="service2"),
    path('service4/',views.service4,name="service4"),
    path('service5/',views.service5,name="service5"),
    path('booking1/',views.booking1,name="booking1"),
    path('finalbooking/',views.finalbooking,name="finalbooking"),
    path('Profile/',views.Profile,name="Profile"),
    path('view_profile/',views.view_profile,name="view_profile"),
    path('provider_order/',views.provider_order,name="provider_order"),
    path('our_service/',views.our_service,name="our_service"),
    path('con/',views.con,name="con"),
   
    path('order/',views.order,name="order"),
    path('show_order/',views.show_order,name="show_order"),
    path('delete/<int:oid>/',views.delete,name="delete"),
    path('update_status/<int:oid>/',views.update_status,name="update_status"),
    path('aboutus/',views.aboutus,name="aboutus"),
    

    



]
