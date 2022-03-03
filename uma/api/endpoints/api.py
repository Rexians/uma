from fastapi import APIRouter
from ..endpoints import champ_info, roster

# router is to add all routes into 1 and import this into the application
# To add more, import the specific router from endpoints, then include it in this main router
router = APIRouter()
router.include_router(champ_info.router)
router.include_router(roster.router)