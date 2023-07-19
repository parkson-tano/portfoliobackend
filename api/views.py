from rest_framework import viewsets
from .models import Portfolio
from .serializer import PortfolioSerializer
from rest_framework.response import Response
from rest_framework import status


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)

            # Generate and assign the modification_key
            instance = serializer.instance
            modification_key = instance.modification_key

            instance.save()

            return Response({"status": "success", "key": modification_key}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def update_data(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        modification_key = request.data.get('modification_key', None)

        # Check if the provided modification_key matches the one in the database
        if instance.modification_key == modification_key:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            return Response({"status": "success"}, status=status.HTTP_200_OK)
        else:
            raise Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        if 'modification_key' in request.data:
            return self.update_data(request, *args, **kwargs)
        else:
            return super().update(request, *args, **kwargs)


