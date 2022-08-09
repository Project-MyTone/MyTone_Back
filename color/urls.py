from django.urls import path

from color.views import (
    ColorListDetailViewSet,
    CosmeticListDetailViewSet
)


color_list = ColorListDetailViewSet.as_view({
    'get': 'list'
})

color_detail = ColorListDetailViewSet.as_view({
    'get': 'retrieve'
})

cosmetic_list = CosmeticListDetailViewSet.as_view({
    'get': 'list'
})


urlpatterns = [
    path('', color_list),
    path('<int:color_id>/', color_detail),
    path('<int:color_id>/cosmetic/', cosmetic_list),
]