# Django
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt import views as jwt_views
from django.urls import path

# Local modules
from .views import views

# technical/
urlpatterns = [ 
    # CRUD patterns
    path('', views.ApiView, name="all-views"),
    path('create/', views.add_items, name="add-items"),
    path('all/', views.view_cars, name="view-cars"),
    path('update/<int:pk>/', views.update_cars, name='update-cars'),
    path('delete/<int:pk>/', views.delete_cars, name='delete-cars'),
    

# JWT patterns
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
