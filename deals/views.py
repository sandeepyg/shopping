from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from deals.models import Deals, Inventory, Customer
from datetime import datetime, timedelta


# Create your views here.

class CreateDeal(GenericAPIView):
    def post(self, request):
        try:
            request_data = request.data
            for deal in request_data.get("deals"):
                item_id = deal.get('id')
                deal_price = deal.get('price')
                deal_qty = deal.get('quantity')
                deal_time = deal.get('time')
                deal_time = datetime.now()+timedelta(hours = deal_time)
                deal_obj = Deals.objects.create(quantity=deal_qty, price=deal_price, expiry=deal_time)
                invent_obj = Inventory.objects.get(id=item_id)
                invent_obj.deal_id = deal_obj
                invent_obj.save()
            resp_data = {"msg": "Deal created"}
            return Response(data=resp_data, status=status.HTTP_200_OK)
        except Exception as e:
            resp_data = {"msg": "Something went wrong"}
            return Response(data=resp_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EndDeal(GenericAPIView):
    def delete(self, request):
        try:
            request_data = request.data
            for deal in request_data.get("deals"):
                item_id = deal.get('id')
                invent_obj = Inventory.objects.get(id=item_id)
                deal_obj = Deals.objects.get(id=invent_obj.deal_id.id)
                invent_obj.deal_id = None
                deal_obj.delete()
                invent_obj.save()
            resp_data = {"msg": "Deal deleted"}
            return Response(data=resp_data, status=status.HTTP_200_OK)
        except Exception as e:
            resp_data = {"msg": "Something went wrong"}
            return Response(data=resp_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UpdateDeal(GenericAPIView):
    def put(self, request):
        try:
            request_data = request.data
            for deal in request_data.get("deals"):
                item_id = deal.get('id')
                deal_qty = deal.get('quantity')
                deal_time = deal.get('time')

                invent_obj = Inventory.objects.get(id=item_id)
                deal_obj = Deals.objects.get(id=invent_obj.deal_id.id)
                deal_time = deal_obj.expiry + timedelta(hours=deal_time)
                deal_obj.quantity = deal_qty
                deal_obj.expiry = deal_time
                deal_obj.save()
            resp_data = {"msg": "Deal Updated"}
            return Response(data=resp_data, status=status.HTTP_200_OK)
        except Exception as e:
            resp_data = {"msg": "Something went wrong"}
            return Response(data=resp_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
