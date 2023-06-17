from api.models.base import Serializable


def serialize_all(data: list[Serializable]) -> list:
    return [item.serialize() for item in data]
