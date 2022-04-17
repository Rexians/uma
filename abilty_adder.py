"""
Temporary File, Will be deleted once all the abilties gets added.
"""
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os


def get_abilities(champname: str, tier: int, rank: int) -> str:
    """
    Returns abilities of a champ
    """
    url = f"https://auntm.ai/champions/{champname}/tier/{tier}"
    opts = webdriver.ChromeOptions()
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-gpu")

    browser = webdriver.Chrome(options=opts)
    browser.get(url)

    browser.maximize_window()
    browser.implicitly_wait(10)

    browser.find_element(By.ID, "rankDropdown").click()
    browser.find_element(By.XPATH, f"//*[contains(text(), 'RANK {rank}')]").click()

    html = browser.find_element(By.TAG_NAME, "html")
    for num in range(0, 21):
        html.send_keys(Keys.ARROW_DOWN)

    abilities_flex = browser.find_element(
        By.CSS_SELECTOR, "div.sc-idOhPF:nth-child(4) > div:nth-child(1)"
    )
    abilities = abilities_flex.find_elements(By.CLASS_NAME, "Collapsible")
    abilities_list = []
    for ability in abilities:
        try:
            ability.click()
            time.sleep(3)
            ability_info = ability.text
            abilities_list.append(ability_info)
        except:
            pass
            # print(f"Couldn't click on", ability.text)
    time.sleep(10)
    browser.close()
    abilities = ""
    for ability_name in abilities_list:
        if "." not in ability_name:
            abilities_list.pop(abilities_list.index(ability_name))
        abilities += f"{ability_name}"
    return abilities


def get_ranks_list(tier: int) -> list:
    """
    Returns rank list for a tier
    """
    if tier == 6:
        return [1, 2, 3, 4]
    elif tier == 5 or tier == 4:
        return [1, 2, 3, 4, 5]
    elif tier == 3:
        return [1, 2, 3, 4]
    elif tier == 2:
        return [1, 2, 3]


def main():
    errors = []

    champ_names = sorted(os.listdir("./uma/files/champ_stats"))
    for champ in champ_names:
        champname = champ.replace(".json", "")
        for tier in range(2, 7):
            for rank in get_ranks_list(tier):
                try:
                    abilities = get_abilities(champname, tier, rank)
                    with open(f"./uma/files/champ_stats/{champ}", "r") as f:
                        json_data = json.load(f)
                        json_data["data"][f"{tier}+{rank}"]["abilities"] = abilities
                        with open(f"./uma/files/champ_stats/{champ}", "w") as f:
                            json.dump(json_data, f, indent=4)
                            print("Done for", champname)
                except:
                    errors.append(f"{tier}* R{rank} {champname}")

    print("At end, all the errors were:")
    for error in errors:
        print(error)


if __name__ == "__main__":
    main()
