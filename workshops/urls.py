from django.urls import re_path

from . import views

app_name = "workshops"

urlpatterns = (
    re_path(
        r"^/?$",
        views.WorkshopListView.as_view(),
        name="list",
    ),
    re_path(
        r"^/(?P<workshop_id>\d+)/?$",
        views.WorkshopDetailView.as_view(),
        name="detail",
    ),
    re_path(
        r"^/(?P<workshop_id>\d+)/brands/?$",
        views.WorkshopBrandListView.as_view(),
        name="brands",
    ),
    re_path(
        r"^/(?P<workshop_id>\d+)/contacts/?$",
        views.WorkshopContactListView.as_view(),
        name="contacts",
    ),
    re_path(
        r"^/(?P<workshop_id>\d+)/employees/?$",
        views.WorkshopEmployeeListView.as_view(),
        name="employees",
    ),
    re_path(
        r"^/(?P<workshop_id>\d+)/services/?$",
        views.WorkshopServiceView.as_view(),
        name="services",
    ),
    re_path(
        r"^/(?P<workshop_id>\d+)/specialities/?$",
        views.WorkshopSpecialityView.as_view(),
        name="specialities",
    ),
    re_path(
        r"^/(?P<workshop_id>\d+)/vehicles/?$",
        views.WorkshopVehicleView.as_view(),
        name="vehicles",
    ),
    re_path(
        r"^/(?P<workshop_id>\d+)/contacts/(?P<contact_id>\d+)/?$",
        views.WorkshopContactDetailView.as_view(),
        name="contact-detail",
    ),
    re_path(
        r"^/(?P<workshop_id>\d+)/reviews/?$",
        views.ReviewListView.as_view(),
        name="reviews",
    ),
    re_path(
        r"^/(?P<workshop_id>\d+)/reviews/(?P<review_id>\d+)/responses/?$",
        views.ReviewResponseView.as_view(),
        name="review-responses",
    ),
    re_path(
        r"^/(?P<workshop_id>\d+)/reviews/(?P<review_id>\d+)/photos/?$",
        views.ReviewPhotoView.as_view(),
        name="review-photos",
    ),
    re_path(
        r"^/specialities/?$",
        views.SpecialityListView.as_view(),
        name="speciality-list",
    ),
    re_path(
        r"^/specialities/(?P<speciality_id>\d+)/?$",
        views.SpecialityDetailView.as_view(),
        name="speciality-detail",
    ),
)
