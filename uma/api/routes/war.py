from fastapi import FastAPI, HTTPException, APIRouter
from ..models.mcoc_war import War

router = APIRouter()

@router.get('/war/{tier}')
def get_war_info(tier):

    """
    Get information of war based on tier
    """

    war = War()
    war.read_tier(tier)
    if war.error == None:
        war_dict = {
                    "tier": war.tier,
                    "nodes": war.nodes,
                    "difficulty": war.difficulty,
                    "tier_multiplier": war.tier_multiplier,
                    "tier_rank": war.tier_rank
                }
        return war_dict
    else:
        raise HTTPException(400, war.error)
