import json
import os

# Get the directory path of the current script
current_dir1 = os.path.dirname(__file__)

# Construct the path to the careers.json file
careers_json_path1 = os.path.join(current_dir1, '..', 'data', 'careers.json')

# Load the career dataset from JSON
with open(careers_json_path1, 'r') as file:
    careers_data = json.load(file)
    
    
    
# Get the directory path of the current script
current_dir2 = os.path.dirname(__file__)

# Construct the path to the careers.json file
careers_json_path2 = os.path.join(current_dir2, '..', 'data', 'user_response.json')

# Load the career dataset from JSON
with open(careers_json_path2, 'r') as file:
    user_response = json.load(file)
    
    
    
    
# Get the directory path of the current script
current_dir3 = os.path.dirname(__file__)

# Construct the path to the careers.json file
careers_json_path3 = os.path.join(current_dir3, '..', 'data', 'test_q.json')

# Load the career dataset from JSON
with open(careers_json_path3, 'r') as file:
    test_q = json.load(file)

# # Load the user responses
# user_response = json.load(open("user_response.json"))

# # Load the assessment questions
# test_q = json.load(open("test_q.json"))

# Define the ideal career name function
def ideal_career_name(user_response, careers_data):
    # Calculate the user's career score
    career_score = 0
    for question in test_q:
        if user_response[question['id']] in question['options']:
            career_score += question['weight']
    # Sort the careers by their scores
    careers = [(career, careers_data[career]) for career in careers_data]
    careers.sort(key=lambda x: x[1]['score'] * (x[1]['weight'] if 'weight' in x[1] else 1), reverse=True)
    # Return the ideal career name

    return careers[0][0]
print(ideal_career_name)
