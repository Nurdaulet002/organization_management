# views.py
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import get_free_slots_for_specializations_in_date_range

class FreeSlotsForSpecializationsInDateRangeView(APIView):

    def get(self, request):
        specializations = request.query_params.getlist('specialization')
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')

        if not start_date_str or not end_date_str:
            return Response({'error': 'Both start_date and end_date are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        except ValueError:
            return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)

        slots = get_free_slots_for_specializations_in_date_range(specializations, start_date, end_date)
        return Response(slots, status=status.HTTP_200_OK)


