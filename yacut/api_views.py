from flask import jsonify, request
from marshmallow import ValidationError

from . import app, db
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
    try:
        validated_data = schema.load(data)
    except ValidationError as error:
        return jsonify(error.messages), 400
    urlmap_obj = URLMap(**validated_data)
    db.session.add(urlmap_obj)
    db.session.commit()
    serialized_object = schema.dump(urlmap_obj)
    return jsonify(serialized_object), 201


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_full_link(short_id):
    original_link = URLMap.query.filter_by(short=short_id).first()
    if not original_link:
        raise InvalidAPIUsage(API_ERROR_MESSAGE['object_is_missing'], 404)
    schema = GetOriginalURLSchema()
    serializer_object = schema.dump(original_link)
    return jsonify(serializer_object), 200