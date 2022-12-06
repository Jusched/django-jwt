# Django

from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView
from rest_framework_simplejwt import views as jwt_views
from django.urls import path

# Local modules
from .views import cars

# technical/
urlpatterns = [ 
    # CRUD patterns
    path('', cars.ApiView, name="all-views"),
    path('create/', cars.add_cars, name="add-cars"),
    path('all/', cars.view_cars, name="view-cars"),
    path('update/<int:pk>/', cars.update_cars, name='update-cars'),
    path('delete/<int:pk>/', cars.delete_cars, name='delete-cars'),
    

    # JWT patterns
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
