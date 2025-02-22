from django.contrib import admin
from django.urls import path
from movie_app import views
from movie_app.views import register_user, confirm_user, login_user

urlpatterns = [
    path('admin/', admin.site.urls),

    # Directors
    path('api/v1/directors/', views.director_list_view),
    path('api/v1/directors/<int:id>/', views.director_detail_view),

    # Movies
    path('api/v1/movies/', views.movie_list_view),
    path('api/v1/movies/<int:id>/', views.movie_detail_view),

    # Reviews
    path('api/v1/reviews/', views.review_list_view),
    path('api/v1/reviews/<int:id>/', views.review_detail_view),

    path("api/v1/users/register/", register_user, name="register"),
    path("api/v1/users/confirm/", confirm_user, name="confirm"),
    path("api/v1/users/login/", login_user, name="login"),
]
