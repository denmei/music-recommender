import json

artists_in = open('artists.csv', 'r+').readlines()

model_fixes = []
pk_count = 1

for line in artists_in:
    artist = line.split(",", 1)[1].strip()
    pk = pk_count
    pk_count += 1
    fix_dict = dict()
    fix_dict['model'] = "recommender_app.artist"
    fix_dict['pk'] = pk
    fix_dict['fields'] = {}
    fix_dict['fields']['name'] = artist
    print(fix_dict)
    model_fixes += [fix_dict]

fixes = json.dumps(model_fixes)
with open("artists_fixture.json", 'w+') as artists_out:
    artists_out.write(fixes)
    artists_out.close()
