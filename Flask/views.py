from flask import Flask, jsonify, request
from flask.views import MethodView

from app import app
from models import Advertisement
from validator import validate
from schema import AD_CREATE


class AdvertisementView(MethodView):

    def get(self, id):
        ad = Advertisement.by_id(id)
        return jsonify(ad.to_dict())

    @validate('json', AD_CREATE)
    def post(self):
        ad = Advertisement(**request.json)
        ad.add()
        response = jsonify(ad.to_dict())
        response.status_code = 201
        return response

    def delete(self, id):
        ad = Advertisement.by_id(id)
        ad.delete()
        response = jsonify({'status': 'NO CONTENT'})
        response.status_code = 204
        return response


app.add_url_rule(
    '/api/v1/advertisements/<int:id>',
    view_func=AdvertisementView.as_view('advertisements_get'),
    methods=['GET', ],
)

app.add_url_rule(
    '/api/v1/advertisements',
    view_func=AdvertisementView.as_view('advertisements_create'),
    methods=['POST', ],
)

app.add_url_rule(
    '/api/v1/advertisements/<int:id>',
    view_func=AdvertisementView.as_view('advertisements_dlete'),
    methods=['DELETE', ],
)