"""Frontend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('cars/<int:carPage>', views.home, name="homecars"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('infoItem/<int:carId>', views.getItem, name='infoitem'),
    path('search/<int:pageID>', views.search, name='searchpage'),
    path('profile/<str:edit>/', views.getProfile, name="profile"),
    path('profile/<str:edit>/', views.getProfile, name="profileedit"),
    path('updateProfile', views.updateProfile, name="updateProfile"),
    path('favourite/', views.getFavourites, name="favourite"),
    path('favourites/add/<int:favID>', views.addFavourites, name="addfavourite"),
    path('delete/favourite/<int:favID>', views.deleteFavourite, name="delfavourite"),
    path('sellerPanel/<str:typeOfPanel>/<int:page>', views.sellerPanel, name="sellerpanel"),
    path('seller/delete/<int:carID>', views.deleteCarFromSale, name="sellerdelete"),
    path('seller/edit/<int:carID>', views.editCar, name="selleredit"),
    path('seller/edit/save', views.saveEdit, name="saveedit"),
    path('seller/add/', views.addCar, name="addcar"),
    path('seller/add/save', views.saveCar, name="addcarsave"),
    path('seller/sold/<int:carID>', views.sellCarFromSale, name="sellcar"),
    path('admins/users/<str:typeUser>/<int:pageID>', views.listAllUsers, name="listallusers"),
    path('analytics/<str:typeOfChart>', views.generateAnalytics, name="analytics")
]
