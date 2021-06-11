from views import AdView, Health
from models import db
from aiohttp import web
from config import URI


async def set_connection():
    return await db.set_bind(URI)


async def disconnect():
    return await db.pop_bind().close()


async def orm_engine(app):
    app['db'] = db
    await set_connection()
    await db.gino.create_all()
    yield
    await disconnect()


app = web.Application()
app.cleanup_ctx.append(orm_engine)
app.add_routes([web.get('/api/v1/advertisements/{ad_id:\d+}', AdView)])
app.add_routes([web.post('/api/v1/advertisements/', AdView)])
app.add_routes([web.delete('/api/v1/advertisements/{ad_id:\d+}', AdView)])
app.add_routes([web.get('/', Health)])


if __name__ == '__main__':
    web.run_app(app, port=8082)

