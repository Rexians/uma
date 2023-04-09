from fastapi import FastAPI, HTTPException, APIRouter
from ..models.mcoc_war import War

router = APIRouter()


@router.get("/war/{tier}")
def get_war_info(tier):

    """
    Get information of war based on tier
    """

    war = War()
    war.read_tier(tier)
    if war.error == None:
        war_dict = {
            "season": war.season,
            "start": war.start,
            "difficulty": war.difficulty,
            "bans": war.bans,
            "tier": war.tier,
            "nodes": war.nodes,
            "tier_multiplier": war.tier_multiplier,
            "tier_rank": war.tier_rank,
            "status": 200,
            "detail": "Successful",
        }
        return war_dict
    else:
        raise HTTPException(400, war.error)
