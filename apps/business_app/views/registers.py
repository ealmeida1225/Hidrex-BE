from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets
from rest_framework.generics import GenericAPIView


from apps.business_app.models.registers import Registers
from apps.business_app.serializers.registers import RegistersSerializer
from apps.common.mixins.common_view_mixin import CommonOrderingFilter


# Create your views here.


class RegistersViewSet(viewsets.ModelViewSet, GenericAPIView):
    """
    API endpoint that allows file upload extensions added or edited.
    """

    queryset = Registers.objects.all()
    serializer_class = RegistersSerializer
    ordering_fields = "__all__"
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        CommonOrderingFilter,
    ]

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
