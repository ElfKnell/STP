from rest_framework import generics
from .serializers import SectionDetailSerializer, SectionsListSerializer
from .models import Section
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class SectionCreateView(generics.CreateAPIView):
    serializer_class = SectionDetailSerializer
    permission_classes = (IsAuthenticated, )


class SectionsListView(generics.ListAPIView):
    serializer_class = SectionsListSerializer
    queryset = Section.objects.all()


class SectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SectionDetailSerializer
    queryset = Section.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
