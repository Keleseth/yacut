from http import HTTPStatus

from flask import jsonify, request

from . import app
from settings import (
    API_ERROR_MESSAGE
)
from yacut.exceptions import InvalidAPIUsage
from yacut.models import URLMap
from yacut.serializers import (
    GetOriginalURLSchema,
    URLMapSChema,
)


@app.route('/api/id/', methods=['POST'])
def api_short_link():
    if not request.data:
        raise InvalidAPIUsage(str(API_ERROR_MESSAGE['emty_body']))
    data = request.get_json()
    schema = URLMapSChema()
    validated_data = schema.load(data)
    urlmap_obj = URLMap.link_object_create(validated_data)
    serialized_object = schema.dump(urlmap_obj)
    return jsonify(serialized_object), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_full_link(short_id):
    original_link = URLMap.get_link_object(short_id)
    if not original_link:
        raise InvalidAPIUsage(
            API_ERROR_MESSAGE['object_is_missing'], HTTPStatus.NOT_FOUND
        )
    schema = GetOriginalURLSchema()
    serializer_object = schema.dump(original_link)
    return jsonify(serializer_object), HTTPStatus.OK