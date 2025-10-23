from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets
from rest_framework.generics import GenericAPIView


from apps.business_app.models.pluviometer_area import PluviometerArea
from apps.business_app.serializers.pluviometer_area import PluviometerAreaSerializer
from apps.common.mixins.common_view_mixin import CommonOrderingFilter


# Create your views here.


class PluviometerAreaViewSet(viewsets.ModelViewSet, GenericAPIView):
    """
    API endpoint that allows file upload extensions added or edited.
    """

    queryset = PluviometerArea.objects.all()
    serializer_class = PluviometerAreaSerializer
    ordering_fields = "__all__"
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        CommonOrderingFilter,
    ]

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
