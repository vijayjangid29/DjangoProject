from django.urls import path
from django.conf.urls.static import static
from .views import index,Category,ProductDetail,category_title
from app import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from .forms import LoginForm,Password_Change_form,Rest_password_form,set_password_form
# from app import admin
from django.contrib import admin

urlpatterns = [
    path('',index),
    #
    path('category/<slug:val>',Category,name="category"),
    # 
    path('product-detail/<int:pk>/',ProductDetail.as_view(),name='product-details'),
    #
    path('category-title/<val>',category_title,name='category-title'),
    #
    path('about/',views.about,name='about'),
    #
    path('contact/',views.contact,name='contact'),
    #
    path('profile/',views.profileview.as_view(),name='profile'),
    #
    path('updateAddress/<int:pk>',views.update_Address.as_view(),name='updateaddress'),
    ##
    path('add-to-cart/',views.add_to_cart,name="cart"),
    path('cart-show/',views.show_cart,name='Showcart'),
    #

    path('checkout/',views.checkout.as_view(),name="checkout"),

    path('pluscart/',views.pluscart), 
    #
    path('minuscart/',views.minus_cart), 
    #
    path('removecart/',views.remove_cart), 
    
    # WishList:-
    path('pluswishlist/',views.plus_wishList_view),
    #
    path('minuswishlist/',views.minus_wishList_view),
    #
    #=============================================================
    #
    #  Payment Methods
    #
    path('paymentdone/',views.payment_done,name="paymentdone"),    
    #
    path('order/',views.order,name='order'),




    #---------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------
    
    # login Authentications
    path('registration/',views.RegistrationView.as_view(),name='registration'),
    path('accounts/login/',auth_view.LoginView.as_view(template_name = 'app/login.html',authentication_form=LoginForm),name='login'),
    # path('password-rest/',auth_view.PasswordResetView.as_view(template_name='app/password_rest.html',form_class=Password_Change_form),name='password_rest'),
    path('address/',views.address,name='address'),
    path('changepassword/',auth_view.PasswordChangeView.as_view(template_name = 'app/passwordchange.html',form_class=Password_Change_form,success_url='/passwordchagedone'),name='passwordchange'),
    path('passwordchagedone/',auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='passwordchagedone'),
    path('logout/',auth_view.LogoutView.as_view(next_page='login'),name='logout'),
    
    
    # Password Reset 
    #
    #  
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name = 'app/password_reset.html',form_class=Rest_password_form),name='password_reset'),
    #
    #                                                                                                                     '  '          #
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='app/password_rest_done.html'), name='password_reset_done'),
    #
    #
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='app/password_rest_confirm.html', form_class=set_password_form), name='password_reset_confirm'),
    #
    #
    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name='app/password_rest_complete.html'),name='password_reset_complete'),
    #
    #   Search URL 
    #
    path('search/',views.search,name="search")
]+static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)


admin.site.site_header = "Vijay Dairy"
admin.site.site_title = "Vijay Dairy"
admin.site.index_title  = "Welcome to the Vijay Dairy Shop"