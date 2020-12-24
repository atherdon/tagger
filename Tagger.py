"""Categorizes tags from file tags.csv into categories in new file sorted.csv"""

import csv
import keywordparser

#categories as variables and tags as list
b_cat = keywordparser.blockchain
p_cat = keywordparser.programming
s_cat = keywordparser.startups
#uncategorized csv file should be named tags.csv. It will create a file called formatted.csv
with open ("tags.csv") as form_csv:
    forma = csv.reader(form_csv)
    with open ("formatted.csv", "w", newline = None, encoding = "utf-8") as inputter_csv:
        writer = csv.writer(inputter_csv)
        for item in forma:
            x = []
            if "-" in item[0]:
                x.append(((item[0].replace("-", " "))))
                writer.writerow(x)
            elif "-" not in item[0]:
                x.append(item[0])
                writer.writerow(x)

#takes formatted.csv and categorizes it into a file named catted

with open ("formatted.csv", newline = "", encoding = "utf-8") as tags_file:
    reader = csv.reader(tags_file)
    with open ("catted.csv", "w") as writer_obj:
        catter = csv.writer(writer_obj)
        for tag in reader:
            for item in b_cat:
                if item in tag[0].lower():
                    tag.append("Blockchain")
                    catter.writerow(tag)
                    break
            for p_key in p_cat:
                if p_key in tag[0].lower():
                    tag.append("Programming")
                    catter.writerow(tag)
                    break
            for s_key in s_cat:
                if s_key in tag[0].lower():
                    tag.append("Startups")
                    catter.writerow(tag)
                    break
            if len(tag)<2:
                tag.append("Not Categorized")
                catter.writerow(tag)