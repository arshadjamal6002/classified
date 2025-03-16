import paralleldots, requests
paralleldots.set_api_key('IH4OCcC3pwUFU6jRcoyzug4ShpopFEtpLFigQEZImmk')

# def ner(text):
#     print('*'*10)
#     ner = paralleldots.ner(text)
#     print(ner)
#     print('*'*10)
#     return ner



def ner(text):
        # ner_result = None  # To store the NER result
        # if request.method == "POST":
        #     user_text = request.form["user_text"]
        
    # Build the URL for Dandelion API
    api_url = f"https://api.dandelion.eu/datatxt/nex/v1/?text={text}&include=types,abstract,categories&token={'38e2e49988e24393a759010c502b7aeb'}"
    
    # Send a GET request to Dandelion API
    response = requests.get(api_url)
    
    if response.status_code == 200:
        ner_result = response.json()  # Parse the response JSON
    else:
        ner_result = {"error": "API request failed, please try again later."}

    return ner_result

def extract_entities_and_types(response):
    # Extract entities with types
    entities = []
    for annotation in response['annotations']:
        spot = annotation['spot']
        # Try to determine the entity type from the types field
        types = annotation.get('types', [])
        if types:
            # If types contain a link, extract the last part of the URL for a human-readable type (e.g., Person, Place)
            entity_type = types[0].split('/')[-1].capitalize()
        else:
            # If no types, categorize it manually
            entity_type = 'Unknown'

        entities.append(f"{spot} - {entity_type}")
    return entities

# Output the formatted entities

# # Extract entities and their types
# entities = extract_entities_and_types()

# # Print the extracted entities and their types
# for entity in entities:
#     print(f"Entity: {entity['entity']}, Type: {entity['type']}")

    