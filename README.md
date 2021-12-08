# UMA (Unofficial MCOC API)

![UMA Banner](blob/UMA_Banner.png)

## Overview

UMA is a API created for the developers who like and play MCOC(Marvel Contest of Champions).
It gives various information about champs like for ex- their PI, Prestige etc...

## URI 

The base URI for the API is currently- `http://mcoc-api.herokuapp.com` and all the requests are to be made on this.

## Working

The working of this API is kind-of different from others. Rather than always accessing from a Database, it has to choose whether to do the same or scrape from a website.
So, as UMA is in beta phase, It's database isn't still complete. Whenever a user requests data from the endpoints, the API checks if the information is available in the database, if it isn't, It actually live scrapes the data from the [auntm.ai website](https://auntm.ai/) and then sends you the information while putting it in the database too. Even though, This makes the API Slow, this is the best method I have come up with. 

A flow chart is shown below to explain it better-

![Diagram](blob/flowchart.png)

## Endpoints

- ### champs

    - **Base URL**-> `https://mcoc-api.herokuapp.com/champs`

    - **Query Params**-> 
        - 1- `champ`
        - 2- `tier`

    - **Overview**
        - This endpoint is used to get basic information about champs like HP, Prestige etc...
        - The `champs` endpoint needs two query parameters- `champ` which is a specific code for each champ, and `tier` which is the tier or star for the champ.
        - The `champ` list can be found [here](champnames.md)
        - The `tier` should be from 1 to 6
        - Ex. To get the info on 6 star Abomination, the URI will be `https://mcoc-api.herokuapp.com/champs/?champ=abomination&tier=6`

    - **Response**
        - Example of Successful response of 6 star Abomination(200 OK)
           - ```json
                {	
                "name":"ABOMINATION",
                "prestige":"9882",
                "hp":"49894",
                "attack":"3859",
                "crit_rate":"359",
                "crit_dmge":"550",
                "armor":"621",
                "block_prof":"2801",
                "energy_resist":"0",
                "physical_resist":"0",
                "crit_resist":"0",
                "sig_info":"Contact with the Abomination's gamma-irradiated body has a 5.29 to 25.03% chance to Poison the target, reducing their Health recovery by 30% and dealing 3087.2 Direct Damage over 12 seconds.",
                "url_page":"https://auntm.ai/champions/abomination/tier/6",
                "img_potrait":"https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_abomination.png",
                "champid":"abomination+6",
                "status":200,
                "detail":"Successful"
                }
                ```
        - Example of Unsuccessful response(404 Not Found)
            - ```json
                {"detail":"Error on Finding Champ/Element on AUNTM.ai and/or Database"}
              ```       

- ### find

    - **Base URL**-> `https://mcoc-api.herokuapp.com/find`

    - **Query Params**-> 
        - 1- `champ`

    - **Overview**
        - This endpoint is used to get the info where a specific champ can be found like in Story quest or where.
        - The `find` endpoint needs one query parameters- `champ` which is a specific code for each champ.
        - The `champ` list can be found [here](champnames.md)
        - Ex. To get the info on where a Abomination can be found, the URI will be `https://mcoc-api.herokuapp.com/find/?champ=abomination`
        - This Endpoint is slower than the previous one because there is not a Database for this one.

    - **Response**
        - Example of Successful response of  Abomination(200 OK)
           - ```json
                {"name":"ABOMINATION",
                "url_page":"https://auntm.ai/champions/abomination",
                "img_potrait":"https://auntm.ai/resources/ui/uigacha/featured/gachachaseprize_256x256_abomination.png",
                "quests":{
                    "story_quests":"2.1.3, 3.2.2, 3.2.6, 4.1.1, 4.1.2, 4.2.1, 4.2.2, 4.3.1, 4.3.2, 4.3.5, 4.3.6, 4.4.1, 4.4.2, 4.4.3, 4.4.4, 4.4.5, 4.4.6, 5.1.4, 5.2.3, 5.2.6, 5.3.1, 5.3.3, 5.3.5, 5.3.6, 5.4.1, 5.4.2, 5.4.4, 5.4.5, 5.4.6, 6.1.1, 6.1.4, 6.1.5, 6.1.6, 6.2.3, 6.2.5, 6.2.6, 6.3.4, 6.3.5, 6.4.3, 7.1.4, 7.1.5",
                    "event_quests":"KINGS OF THE JUNGLE, 1.1, 1.2, 2.1, 2.2, 3.1, 3.2",
                    "alliance_quests":"MAP 6: Futuristic Termination, MAP 7: Suited Destruction, MAP 8: Supernova",
                    "incursions":"SCIENCE SLAUGHTER, Easy, SCIENCE SLAUGHTER, Medium, SCIENCE SLAUGHTER, Hard, SCIENCE SLAUGHTER, Expert",
                    "daily_quests":"SCIENCE SLAUGHTER, Easy, SCIENCE SLAUGHTER, Medium, SCIENCE SLAUGHTER, Hard, SCIENCE SLAUGHTER, Expert",
                    "special_quests":"ROAD TO THE LABYRINTH, 1.1, 2.4, 3.2, 4.2, 4.6, LABYRINTH OF LEGENDS",
                    "back_quests":"DEADPOOLOOZA, 2.1, 3.2, ARACHNID ACTION, 1.1, 2.2, CONTAMINATION, 1.1, 1.2, 2.1, 3.1, BLOOD AND VENOM, 1.2, 3.1, POLAR OPPOSITES, 1.1, 2.1, 3.1, MYSTERY IN THE MICRO-REALMS, 1.1, 1.3, 2.1, 2.2, 3.3, ULTRON'S ASSAULT, 2.1, 3.3"
                    },
                "champid":"abomination",
                "status":200,
                "detail":"Successful"
                }
                ```
        - Example of Unsuccessful response(404 Not Found)
            - ```json
                {"detail":"Error on Finding Champ/Element on AUNTM.ai"}
              ```
