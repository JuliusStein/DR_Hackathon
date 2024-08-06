import json
import csv

file_path = 'rawJSONL/reviews/Electronics.jsonl'
#reading all jsonl files
jsonl_data = open(file_path, 'r')
json_lines = tuple(json_line for json_line in jsonl_data.readlines() if json_line.strip())
jsons_objs = tuple(json.loads(json_line) for json_line in json_lines)
#creating csv files  
with open('CSVs/Electronics.csv', 'a' , newline='') as f:
    writer = csv.writer(f)
    #headers should be the Key values from json files that make Coulmn header
    writer.writerow(["main_category", "title", "average_rating", "rating_number", "features", "description", "price", "images", "videos", "store", "categories", "details", "parent_asin", "bought_together"])
    writer.writerows((value for key, value in (json_obj.items())) for json_obj in jsons_objs)

