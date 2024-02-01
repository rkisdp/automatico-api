from drf_spectacular.utils import extend_schema

from core.generics import GenericAPIView
from core.mixins import MultipleFieldLookupMixin
from workshops.models import ReviewResponseModel

SCHEMA_TAGS = ("reviews",)


@extend_schema(tags=SCHEMA_TAGS)
class ReviewResponseView(
    MultipleFieldLookupMixin,
    GenericAPIView,
):
    queryset = ReviewResponseModel.objects.all()
    lookup_fields = ("review_id", "id")
    lookup_url_kwargs = ("review_id", "response_id")
    ordering = ("id",)
    filterset_fields = ("review", "response")
    search_fields = ("review", "response")
    ordering_fields = ("review", "response")

    @extend_schema()
    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema()
    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get_serializer_class(self):
        version = self._get_version()
        return self._get_versioned_serializer_class(version)

    def _get_version(self):
        try:
            version = self.request.version
        except Exception:
            version, _ = self.determine_version(self.request)
        return version

    def _get_versioned_serializer_class(self, version):
        module = self._get_serializer_module(version)
        return getattr(module, "ReviewResponseSerializer")
