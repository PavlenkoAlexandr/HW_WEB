from aiohttp import web
from models import Advertisement as Ad


class AdView(web.View):

    async def get(self):
        ad_id = int(self.request.match_info['ad_id'])
        ad = await Ad.get_or_404(ad_id)
        return web.json_response(ad.to_dict())

    async def post(self):
        ad = await self.request.json()
        new_ad = await Ad.create_instance(**ad)
        return web.json_response(new_ad.to_dict())

    async def delete(self):
        ad_id = int(self.request.match_info['ad_id'])
        ad = await Ad.description(ad_id)
        return web.json_response(web.HTTPNotFound())


class Health(web.View):

    async def get(self):
        return web.json_response({'status': 'ok'})
