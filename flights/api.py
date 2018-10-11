from tastypie.resources import ModelResource
from .models import Flight
from tastypie import fields
from tastypie.api import Api


class FlightResource(ModelResource):
    class Meta:
        queryset = Flight.objects.all()
        resource_name = 'flights'


#v1_api = Api(api_name='v1')
#v1_api.register(FlightResource)