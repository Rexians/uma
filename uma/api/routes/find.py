from fastapi import HTTPException, APIRouter
from ..models.mcoc_find import Finder

router = APIRouter()


@router.get("/find/")
def find_champ(champ: str):

    """
    Find and tells the locations where a specific champ can be found
    """

    champ_info = Finder()
    try:
        champ_info.get_data(champ)
        champs_dict = {
            "name": f"{champ_info.name}",
            "class": champ_info.class_type,
            "url_page": f"{champ_info.url_page}",
            "img_portrait": f"{champ_info.img_portrait}",
            "champid": f"{champ_info.champid}",
            "find": champ_info.find,
        }

        champs_dict.update({"status": 200, "detail": "Successful"})

        return champs_dict

    except Exception as e:
        if isinstance(e, FileNotFoundError):
            raise HTTPException(status_code=404, detail="404: " + champ_info.error)
        else:
            raise e
