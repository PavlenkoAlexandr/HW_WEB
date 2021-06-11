import datetime
import gino
from aiohttp import web
from asyncpg.exceptions import UniqueViolationError

db = gino.Gino()


class BaseModel:

    @classmethod
    async def get_or_404(cls, id):
        instance = await cls.get(id)
        if not instance:
            raise web.HTTPNotFound()
        return instance

    @classmethod
    async def create_instance(cls, **kwargs):
        try:
            instance = await cls.create(**kwargs)
            return instance
        except UniqueViolationError:
            raise web.HTTPBadRequest()

    @classmethod
    async def delete_instance(cls, id):
        instance = await cls.delete(id)
        if not instance:
            raise web.HTTPNotFound()
        return instance


class Advertisement(db.Model, BaseModel):

    __tablename__ = 'advertisements'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    description = db.Column(db.String, nullable=True)
    created_date = db.Column(db.Date, nullable=True)
    owner = db.Column(db.String, nullable=True)

    _idx1 = db.Index('advertisements_advertisement_name', 'name', unique=True)

    @classmethod
    async def create_instance(cls, **kwargs):
        kwargs['created_date'] = datetime.datetime.strptime(kwargs['created_date'], '%Y-%m-%d')
        return await super().create_instance(**kwargs)

    def to_dict(self):
        data = super().to_dict()
        data['created_date'] = str(data['created_date'])
        return data
