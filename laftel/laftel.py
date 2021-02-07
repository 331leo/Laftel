from . import objects
async def get_AnimeInfo_obj(data: dict):
    obj = objects.AnimeInfo(data)
    obj.id = data.get("id", None)
    obj.id = data.get("id",None)
