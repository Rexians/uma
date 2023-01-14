def champurl_getter(champ):

    champ_urls = {
        "bwcv" : "blackwidow_timely",
        "redgoblin": "red_goblin",
        "bwdo": "blackwidow_movie",
        "ultron": "ultron_prime",
        "bwdo": "blackwidow_movie",
        "ultron": "ultron_prime",    
        "ultronlol": "ultron",        
        "spidersymbiote": "spiderman_black",
        "mordo": "karlmordo",   
        "sorcerersupreme": "drstrange_realm",  
        "oml": "wolverine_oldman",          
        "hulkbuster": "hulkbuster_movie",
        "ironfistimmortal": "ironfist_white",        
        "cyclops_blue": "cyclops_90s",        
        "cmm": "captainmarvel_movie",
        "caiw": "captainamerica_movie",
        "casw": "captainamerica_samwilson",   
        "caww2": "captainamerica_ww2",       
        "imiw": "ironman_movie",
        "jabaripanther": "blackpanther_realm",
        "kinggroot": "groot_king",
        "misterfantastic": "mrfantastic",
        "bpcw": "blackpanther_cw",
        "punisher2099": "punisher_2099",
        "rocketracoon": "rocket",
        "spiderman2099": "spiderman_2099",
        "overseer": "maestro_overseer",
        "unstoppablecolossus": "colossus_unstoppable",
        "visionaarkus": "vision_timely",
        "visionmovie": "vision_movie",
        "vulture": "vulture_movie",
        "wolverinex": "wolverine_weaponx",
        "spidermorales": "spiderman_morales",
        "starkspiderman": "spiderman_movie",
        "spiderstealth": "spiderman_stealth",
        "redmagneto": "magneto",
        "magnetowhite": "magneto_marvelnow", 
        "kamalakhan": "msmarvel_kamala",
        "platinumpool": "deadpool_platinumpool",
        "scarletwitchnew": "scarletwitch_current",
        "silvercenturion": "ironman_silvercenturion",
        "stormpyramidx": "storm_realm",
        "superskrull": "skrull_super",
        "superiorironman": "ironman_superior",
        "janefoster": "thor_janefoster" ,                                       
        "thorragnarok": "thor_ragnarok",
        "ibom": "abomination_immortal",
        "doctorvoodoo": "brothervoodoo",
        "daredevil netflix": "daredevil_netflix",
        "goldpool": "deadpool_goldpool",
        "cgr": "ghostrider_cosmic",
        "docock": "doc_ock",
        "greengoblin": "green_goblin",
        "howard": "howardmech",
        "jessicajones":"jessicajones_current",
        "spidermansupreme":"spiderman_supreme",
        "infamousironman":"ironman_infamous",
    }

    try:
        champurl = champ_urls[champ]
        return champurl
    except:
        return champ
