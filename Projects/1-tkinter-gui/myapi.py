import requests
# Setting your API key

class API:

    def __init__(self):
        pass

    def sentiment_analysis(self,text):
        

        # Call Dandelion API to get sentiment analysis
        url = "https://api.dandelion.eu/datatxt/sent/v1/"
        params = {
            'lang': 'en',
            'text': text,
            'token': '38e2e49988e24393a759010c502b7aeb'
        }

        # Make the GET request to Dandelion API
        response = requests.get(url, params=params)
        sentiment_data = response.json()  # Convert the response to JSON

        # Check if sentiment analysis is present in the response
        if 'sentiment' in sentiment_data:
            sentiment = sentiment_data['sentiment']['type']  # The sentiment type (positive, neutral, or negative)
            score = sentiment_data['sentiment']['score']  # The sentiment score
        else:
            sentiment = "Error"
            score = "N/A"
        return sentiment, score


    def ner(self,text):
        # ner_result = None  # To store the NER result
        # if request.method == "POST":
        #     user_text = request.form["user_text"]
        
        # Build the URL for Dandelion API
        api_url = f"https://api.dandelion.eu/datatxt/nex/v1/?text={text}&include=types,abstract,categories&token={'38e2e49988e24393a759010c502b7aeb'}"
        
        # Send a GET request to Dandelion API
        response = requests.get(api_url)
        print(response)
        
        if response.status_code == 200:
            ner_result = response.json()
            print(ner_result)
            print("done")  # Parse the response JSON
        else:
            ner_result = {"error": "API request failed, please try again later."}
            print("undone")
            # Extract entities with types
        # return ner_result
        entities = []
        spots = []
        for annotation in ner_result['annotations']:
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
            spots.append(spot)
        return spots
    
        

    def perform_text_similarity(self,text1,text2):


        # Call Dandelion API to get text similarity
        url = "https://api.dandelion.eu/datatxt/sim/v1/"
        params = {
            'text1': text1,
            'text2': text2,
            'token': '38e2e49988e24393a759010c502b7aeb'
        }

        # Make the GET request to Dandelion API
        response = requests.get(url, params=params)
        similarity_data = response.json()  # Convert the response to JSON

        # Extract similarity score from the response
        if 'similarity' in similarity_data:
            similarity_score = similarity_data['similarity']
        else:
            similarity_score = "Error"
        return similarity_score