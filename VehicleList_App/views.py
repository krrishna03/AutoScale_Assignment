from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from VehicleList_App.models import Dealer,Vehicle,ZipList
from geopy.distance import geodesic
from django.db import connection


class GetVehicleInfo(GenericAPIView):

    def get(self, request):

        zip = request.GET.get('zipcode')
        if not zip.isnumeric():
            return render(request,'app.html',{'message':'Pincode should be a number!!!'})
        distance = request.GET.get('distance')
        if not distance:
            return render(request,'app.html',{'message':'Please choose the distance!!!'})

        obj = ZipList.objects.filter(pincode=int(zip)).first()
        if not obj:
            return render(request,'app.html',{'message':'No car nearby this pincode'})
        
        const_coord = [obj.latitude,obj.longitude]

        pin_dict = []
        objs = ZipList.objects.all()
        p_list = []
        for object in objs.iterator():
            
            latitude = object.latitude
            longitude = object.longitude
            var_coord = [latitude,longitude]
            if geodesic(const_coord, var_coord).miles < int(distance):
                near_pincode = object.pincode
                pin_dict.append({'pincode':near_pincode,'state':object.state, 'city':object.city})
                p_list.append(near_pincode)
        p_list = tuple(p_list)
        cursor = connection.cursor()
        cursor.execute('''select t1.pincode , t1.state , t1.city , t2.`year` , t2.make , t2.model , t2.price , t2.dealer_number , t3.dealer_name 
                        from autoventure.vehiclelist_app_ziplist t1 inner join autoventure.vehiclelist_app_vehicle t2 on t1.pincode = t2.pincode 
                        inner join autoventure.vehiclelist_app_dealer t3 on t2.dealer_number =t3.dealer_number 
                        where t1.pincode in {}'''.format(p_list))

        data = cursor.fetchall()

        headers=['pincode','state','city','year','make','model','price','dealer_number','dealer_name']

        return render(request,'app1.html', {'headers':headers, 'data':data})

    
class Home(GenericAPIView):

    def get(self, request):

        return render(request,'app.html',{'node':'App'})

