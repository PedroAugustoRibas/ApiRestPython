from marshmallow import Schema, fields


class HotelRequestSchema(Schema):
    api_type = fields.String(required=True, description="Teste")


class HotelResponseSchema(Schema):
    message = fields.Str(default='Success')
