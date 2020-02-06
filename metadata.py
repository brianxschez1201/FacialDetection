import json

# Read JSON from training metadata file.
with open('training_metadata.json') as json_file :
    data = json.load(json_file)

def get_label_from_video_name(video_name) :

    label = data.get(video_name)

    return label
