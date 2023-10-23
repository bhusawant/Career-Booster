import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv, find_dotenv
from langchain.llms import Cohere
load_dotenv(find_dotenv())

app = Flask(__name__)

app.config['MONGO_URI'] = os.environ['MONGO_URI']
app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET']

CORS(app)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)
db = PyMongo(app).db





llm = Cohere(cohere_api_key="Pt5Aqeee3CA0uMkXnYNG16Q8yfwQ3rIZpV86MwB0", temperature=0.5)

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    
    print(data)
    question = data.get('question', '')
    response = llm.predict(question)
    return jsonify({"answer": response})


@app.route('/jobss',methods=["POST","GET"])
def job():
    name=db.users.find_one({"email":"sid@gmail.com"})
    return jsonify({"email": name["email"], "isDoctor":name["isDoctor"]}) 

@app.route("/page",methods=["POST","GET"])
@jwt_required()
def pages():
     ans=request.get_json()
     print(ans)
     db.ans.insert_one(ans)
     return jsonify("hello")


@app.route('/login', methods=['POST', 'GET'])
def login():
    response = request.get_json()
    print(response)
    # if response['userType'] == 'USER':
    user = db.users.find_one({'email': response['email']})
    if user:
        if bcrypt.check_password_hash(user['password'], response['password']):
            access_token = create_access_token(identity=user['email'])
            return jsonify({'login': True, 'token': access_token})
        return jsonify({'login': False, 'error': 'Incorrect Password'})
    return jsonify({'login': False, 'error': 'EmailId not registered'})
    # elif response['userType'] == 'ORG':
    #     org = db.organisations.find_one({'email': response['email']})
    #     if org:
    #         if bcrypt.check_password_hash(org['password'], response['password']):
    #             access_token = create_access_token(identity=org['email'])
    #             return jsonify({'login': True, 'token': access_token})
    #         return jsonify({'login': False, 'error': 'Incorrect Password'})
    #     return jsonify({'login': False, 'error': 'EmailId not registered'})


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    response = request.get_json()
    # if response['userType'] == 'USER':
    isUser = db.users.find_one({'email': response['email']})
    if isUser is None:
        hashed_pass = bcrypt.generate_password_hash(response['password']).decode('utf-8')
        db.users.insert_one({
            'name': response['name'],
            'email': response['email'],
            'password': hashed_pass,
        })
        access_token = create_access_token(identity=response['email'])
        return jsonify({'signup': True, 'token': access_token})
    return jsonify({'signup': False, 'error': 'EmailId already registered'})

# @app.route('/diff', methods=['POST'])
# def dif():
#     response = request.get_json()
#     print(response)
#     db.ans.insert_one({
#             response
#         })
#     return jsonify({"msg":'hello'})


def provideJobRecommendation(userKnowledge):
    skills = {
        "marketing strategy": {
            "ans1": 1,
            "ans2": 2,
            "ans3": 3,
            "ans4": 2,
            "ans5": 3,
            "ans6": 3,
            "ans7": 3,
            "ans8": 3,
            "ans9": 1,
            "ans10": 1
        },
        "market research": {
            "ans1": 3,
            "ans2": 1,
            "ans3": 2,
            "ans4": 2,
            "ans5": 1,
            "ans6": 4,
            "ans7": 2,
            "ans8": 1,
            "ans9": 2,
            "ans10": 1
        },
        "digital marketing": {
            "ans1": 2,
            "ans2": 3,
            "ans3": 3,
            "ans4": 2,
            "ans5": 4,
            "ans6": 2,
            "ans7": 3,
            "ans8": 2,
            "ans9": 3,
            "ans10": 1 
        },
        "financial analysis": {
            "ans1": 3,
            "ans2": 2,
            "ans3": 1,
            "ans4": 2,
            "ans5": 2,
            "ans6": 4,
            "ans7": 2,
            "ans8": 1,
            "ans9": 2,
            "ans10": 1
        },
        "audit": {
            "ans1": 3,
            "ans2": 1,
            "ans3": 3,
            "ans4": 2,
            "ans5": 3,
            "ans6": 3,
            "ans7": 2,
            "ans8": 1,
            "ans9": 3,
            "ans10": 1
        },
        "accounting software": {
            "ans1": 2,
            "ans2": 2,
            "ans3": 1,
            "ans4": 2,
            "ans5": 3,
            "ans6": 3,
            "ans7": 3,
            "ans8": 3,
            "ans9": 3,
            "ans10": 2
        },
        "financial modeling": {
            "ans1": 3,
            "ans2": 2,
            "ans3": 2,
            "ans4": 1,
            "ans5": 2,
            "ans6": 3,
            "ans7": 1,
            "ans8": 1,
            "ans9": 2,
            "ans10": 1
        },
        "data analysis": {
            "ans1": 4,
            "ans2": 2,
            "ans3": 1,
            "ans4": 2,
            "ans5": 2,
            "ans6": 4,
            "ans7": 1,
            "ans8": 1,
            "ans9": 1,
            "ans10": 1  
        },
        "investment analysis": {
            "ans1": 3,
            "ans2": 2,
            "ans3": 1,
            "ans4": 2,
            "ans5": 2,
            "ans6": 4,
            "ans7": 2,
            "ans8": 2,
            "ans9": 2,
            "ans10": 1
        },
        "creativity": {
            "ans1": 2,
            "ans2": 2,
            "ans3": 4,
            "ans4": 2,
            "ans5": 3,
            "ans6": 3,
            "ans7": 1,
            "ans8": 3,
            "ans9": 3,
            "ans10": 2
        },
        "visual design": {
            "ans1": 1,
            "ans2": 3,
            "ans3": 4,
            "ans4": 2,
            "ans5": 3,
            "ans6": 2,
            "ans7": 1,
            "ans8": 2,
            "ans9": 3,
            "ans10": 2
        },
        "adobe creative suite": {
            "ans1": 1,
            "ans2": 3,
            "ans3": 4,
            "ans4": 2,
            "ans5": 2,
            "ans6": 2,
            "ans7": 2,
            "ans8": 2,
            "ans9": 3,
            "ans10": 1
        },
        "recruitment": {
            "ans1": 1,
            "ans2": 3,
            "ans3": 3,
            "ans4": 4,
            "ans5": 4,
            "ans6": 3,
            "ans7": 3,
            "ans8": 1,
            "ans9": 1,
            "ans10": 1
        },
        "employee relations": {
            "ans1": 1,
            "ans2": 4,
            "ans3": 3,
            "ans4": 4,
            "ans5": 3,
            "ans6": 2,
            "ans7": 3,
            "ans8": 1,
            "ans9": 1,
            "ans10": 1
        },
        "organizational development": {
            "ans1": 5,
            "ans2": 4,
            "ans3": 4,
            "ans4": 5,
            "ans5": 4,
            "ans6": 3,
            "ans7": 3,
            "ans8": 4,
            "ans9": 4,
            "ans10": 2
        },
        "supply chain ans7": {
            "ans1": 1,
            "ans2": 3,
            "ans3": 1,
            "ans4": 3,
            "ans5": 3,
            "ans6": 1,
            "ans7": 4,
            "ans8": 1,
            "ans9": 1,
            "ans10": 2
        },
        "procurement": {
            "ans1": 1,
            "ans2": 3,
            "ans3": 2,
            "ans4": 3,
            "ans5": 4,
            "ans6": 3,
            "ans7": 3,
            "ans8": 1,
            "ans9": 1,
            "ans10": 1
        },
        "logistics": {
            "ans1": 1,
            "ans2": 3,
            "ans3": 1,
            "ans4": 2,
            "ans5": 4,
            "ans6": 3,
            "ans7": 3,
            "ans8": 1,
            "ans9": 1,
            "ans10": 2
        },
        "teaching": {
            "ans1": 3,
            "ans2": 3,
            "ans3": 3,
            "ans4": 3,
            "ans5": 3,
            "ans6": 3,
            "ans7": 3,
            "ans8": 1,
            "ans9": 3,
            "ans10": 2
        },
        "ans5": {
            "ans1": 1,
            "ans2": 3,
            "ans3": 2,
            "ans4": 2,
            "ans5": 4,
            "ans6": 2,
            "ans7": 2,
            "ans8": 1,
            "ans9": 2,
            "ans10": 1
        },
        "lesson planning": {
            "ans1": 1,
            "ans2": 3,
            "ans3": 3,
            "ans4": 3,
            "ans5": 3,
            "ans6": 1,
            "ans7": 3,
            "ans8": 1,
            "ans9": 2,
            "ans10": 1   
        },
        "journalism": {
            "ans1": 1,
            "ans2": 3,
            "ans3": 3,
            "ans4": 4,
            "ans5": 4,
            "ans6": 2,
            "ans7": 2,
            "ans8": 2,
            "ans9": 3,
            "ans10": 1
        },
        "interviewing": {
            "ans1": 1,
            "ans2": 3,
            "ans3": 2,
            "ans4": 3,
            "ans5": 4,
            "ans6": 3,
            "ans7": 3,
            "ans8": 1,
            "ans9": 1,
            "ans10": 1
        },
        "news ans9": {
            "ans1": 1,
            "ans2": 2,
            "ans3": 3,
            "ans4": 3,
            "ans5": 2,
            "ans6": 2,
            "ans7": 2,
            "ans8": 1,
            "ans9": 4,
            "ans10": 1
        },
        "programming":{
            "ans1":3,
            "ans2": 3,
            "ans3": 2,
            "ans4": 2,
            "ans5": 2,
            "ans6": 4,
            "ans7": 1,
            "ans8": 1,
            "ans9": 2,
            "ans10": 1
        },
        "problem-solving":{
            "ans1":3,
            "ans2": 1,
            "ans3": 1,
            "ans4": 3,
            "ans5": 2,
            "ans6": 4,
            "ans7": 1,
            "ans8": 1,
            "ans9": 2,
            "ans10": 1
        },
        "software development":{
            "ans1":3,
            "ans2": 3,
            "ans3": 3,
            "ans4": 3,
            "ans5": 2,
            "ans6": 3,
            "ans7": 2,
            "ans8": 1,
            "ans9": 1,
            "ans10": 1
        },
        "data analysis":{
            "ans1": 4,
            "ans2": 2,
            "ans3": 2,
            "ans4": 2,
            "ans5": 2,
            "ans6": 3,
            "ans7": 1,
            "ans8": 1,
            "ans9": 1,
            "ans10": 1
        },
        "data visualization":{
            "ans1": 3,
            "ans2": 3,
            "ans3": 3,
            "ans4": 2,
            "ans5": 2,
            "ans6": 3,
            "ans7": 2,
            "ans8": 2,
            "ans9": 2,
            "ans10": 1
        },
        "SQL":{
            "ans1": 3,
            "ans2": 2,
            "ans3": 1,
            "ans4": 2,
            "ans5": 2,
            "ans6": 3,
            "ans7": 1,
            "ans8": 1,
            "ans9": 1,
            "ans10": 1
        }
    }

    jobs = [
        
        {
            "name":"Marketing Manager",
            "skills":["marketing strategy", "market research", "digital marketing"]
        },
        {
            "name": "Accountant",
            "skills": ["financial analysis", "audit", "accounting software"]
        },
        {
            "name": "Financial Analyst",
            "skills": ["financial modeling", "data analysis", "investment analysis"]
        },
        {
            "name": "Graphic Designer",
            "skills": ["creativity", "visual design", "adobe creative suite"]
        },
        {
            "name": "Human Resources Manager",
            "skills": ["recruitment", "employee relations", "organizational development"]
        },
        {
            "name": "Supply Chain Manager",
            "skills": ["supply chain ans7", "procurement", "logistics"]
        },
        {
            "name": "Teacher",
            "skills": ["teaching", "ans5", "lesson planning"]
        },
        {
            "name": "Journalist",
            "skills": ["journalism", "interviewing", "news ans9"]
        },
        {
            "name": "Software Developer",
            "skills": ["programming", "problem-solving", "software development"]
        },
        {
            "name": "Data Analyst",
            "skills": ["data analysis", "data visualization", "SQL"]
        }
        
    ]

    user_skill = []

    for skill in skills.keys():
        count = 0
        for skill_needs in skills[skill].keys():
            if skills[skill][skill_needs] <= int(userKnowledge[skill_needs]):
                count += 1
        if count == 10:
            user_skill.append(skill)

    suggest = []

    user_skill.sort()
    print(user_skill)
    for job in jobs:
        name = job["name"]
        job_skills = job["skills"]
        job_skills.sort()
        
        count = 0
        for skill in job_skills:
            if skill in user_skill:
                count += 1
        if count == len(job_skills):
            suggest.append(name)
    
    return suggest

# @app.route('/diff', methods=['POST'])
# # @jwt_required()
# def dif():
#     response = request.get_json()
#     print(response)
    
#     true_responses = [key for key, value in response.items() if value]
    
#     if true_responses:
#         print("True responses:", true_responses)

#     db.ans.insert_one({"ans1": response['ans1'],"ans2": response['ans2'],"ans3": response['ans3'],"ans4": response['ans4'],"ans5": response['ans5'],"ans6": response['ans6'],"ans7": response['ans7'],"ans8": response['ans8'],"ans9": response['ans9'],"ans10": response['ans10'],})

#     result=db.ans.insert_one({"ans1": response['ans1'],"ans2": response['ans2'],"ans3": response['ans3'],"ans4": response['ans4'],"ans5": response['ans5'],"ans6": response['ans6'],"ans7": response['ans7'],"ans8": response['ans8'],"ans9": response['ans9'],"ans10": response['ans10'],})

#     provideJobRecommendation(result)
#     # print(result)

#     # "email":jwt_required()})
#     return jsonify({"key": 'hello'})





@app.route('/diff', methods=['POST'])
# @jwt_required()
def dif():
    response = request.get_json()
    print(response)
    
    true_responses = [key for key, value in response.items() if value]
    
    if true_responses:
        print("True responses:", true_responses)

    db.ans.insert_one({
        "ans1": response['ans1'],
        "ans2": response['ans2'],
        "ans3": response['ans3'],
        "ans4": response['ans4'],
        "ans5": response['ans5'],
        "ans6": response['ans6'],
        "ans7": response['ans7'],
        "ans8": response['ans8'],
        "ans9": response['ans9'],
        "ans10": response['ans10'],
    })

    d = {"ans1": response['ans1'],
        "ans2": response['ans2'],
        "ans3": response['ans3'],
        "ans4": response['ans4'],
        "ans5": response['ans5'],
        "ans6": response['ans6'],
        "ans7": response['ans7'],
        "ans8": response['ans8'],
        "ans9": response['ans9'],
        "ans10": response['ans10'],}
    
    print("RESULT")
    # print(result)
    # print(result.inserted_id)
    # result = str(result.inserted_id)
    # print(result)

    # job_recommendations = provideJobRecommendation(result)
    # print("Job Recommendations:", job_recommendations)
    l = provideJobRecommendation(d)
    for item in l:
        print(item)

    # for key in suggest.keys():
    #     print(f"{key} -> {suggest[key]}")

    return jsonify({'arr': l})



    
    # elif response['userType'] == 'ORG':
    #     isOrg = db.organisations.find_one({'email': response['email']})
    #     if isOrg is None:
    #         hashed_pass = bcrypt.generate_password_hash(response['password']).decode('utf-8')
    #         db.organisations.insert_one({
    #             'name': response['name'],
    #             'email': response['email'],
    #             'gstin': response['gstin'],
    #             'password': hashed_pass,
    #             'nfts': []
    #         })
    #         access_token = create_access_token(identity=response['email'])
    #         return jsonify({'signup': True, 'token': access_token})
    #     return jsonify({'signup': False, 'error': 'EmailId already registered'})



@app.route('/buyNFT', methods=['POST', 'GET'])
def buyNFT():
    response = request.get_json()
    db.users.find_one_and_update({'email': response['email']},
    {'$push': {'nfts':{
        'image': response['image'],
        'title': response['title'],
        'price': response['price'],
        'description': response['description']
    }}})
    return jsonify({'nft': True})


@app.route('/addNFT', methods=['POST', 'GET'])
def addNFT():
    response = request.get_json()
    db.organisations.find_one_and_update({'email': response['email']},
    {'$push': {'nfts': {
        'image': response['image'],
        'title': response['title'],
        'price': response['price'],
        'description': response['description']
    }}})
    return jsonify({'nft': True})


@app.route('/getNFTs', methods=['POST', 'GET'])
@jwt_required()
def getNFTs():
    user = get_jwt_identity()
    print(user)
    nfts = db.users.find_one({'email': user}, {'nfts': 1})
    return jsonify(nfts['nfts'])



# @app.route("/getChat", methods=['POST', 'GET'])
# def chatAPI():
#     response = request.get_json()
#     response = getChat(response['prompt'])
#     return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)