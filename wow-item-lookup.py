import sys
import requests

search_param=sys.argv[1]
if search_param == "--help":
    print("USAGE:\n\t   item_fetcher.py <item>") 
else:
    print(search_param)
    item_id_r = requests.get(f"https://api.nexushub.co/wow-classic/v1/search?query={search_param}")
    item_id=item_id_r.json()[0]["itemId"]
    crafting_r=requests.get(f"https://api.nexushub.co/wow-classic/v1/crafting/{item_id}")
    item=crafting_r.json()
    print(item["name"])
    reagents=[[reagent["name"], reagent["amount"]] for reagent in item["createdBy"][0]["reagents"]]
    reagent_str=""
    for index, reagent in enumerate(reagents):
        reagent_str += f"\n\t {index + 1}: {reagent[0]}, Amount: {reagent[1]}"
    output=f"""
Item: {item["name"]}
Category: {item["createdBy"][0]["category"]}
Reagents: {reagent_str}"""
    print(output)