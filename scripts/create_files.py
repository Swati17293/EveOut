import csv
import json
from yattag import Doc, indent

def create_xml(source_lst):

    doc, tag, text = Doc().tagtext()

    csvfile = open('data/raw/dataset.csv', 'r')
    lines = csv.reader(csvfile)

    #skip header
    next(lines)

    fieldnames = ['uri','title','event_date','sentiment','categories','loc_country','loc_continent','article_count','total_article_count','summary']

    for src in source_lst:
        fieldnames.append(src.split('.')[0])

    with tag('events'):

        for line in lines:
            with tag('results'):

                idx = 0
                for field in fieldnames:
                    with tag(field):
                        text(line[idx])
                    idx += 1

    result = indent(
        doc.getvalue(),
        indentation = ' '*4,
        newline = '\r\n'
    )

    xml_file = open("data/raw/dataset.xml", "w")
    xml_file.write(result)

    xml_file.close()
    csvfile.close()

def create_json(source_lst):

    csvfile = open('data/raw/dataset.csv', 'r')

    lines = csv.reader(csvfile)

    #skip header
    next(lines)

    fieldnames = ['uri','title','event_date','sentiment','categories','loc_country','loc_continent','article_count','total_article_count','summary']

    for src in source_lst:
        fieldnames.append(src.split('.')[0])

    data = {'events':{'results':[]}}

    for line in lines:

        dic = {}
        idx = 0

        for field in fieldnames:
            dic[field] = line[idx]
            idx += 1

        data['events']['results'].append(dic)

    with open('data/raw/dataset.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)

    csvfile.close()