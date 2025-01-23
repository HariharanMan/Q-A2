from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
import pymongo
import json



questions_data = [
    {"domain": "Python", "title": "What is Python?", "author": "Hari", "answers": "Python is a versatile, high-level programming language.", "comments": 10},
    {"domain": "Python", "title": "How to manage memory in Python?", "author": "Mem2", "answers": "Python uses garbage collection and reference counting.", "comments": 8},
    {"domain": "Python", "title": "What are the key features of Python?", "author": "User1", "answers": "Key features include readability, versatility, large community, and extensive libraries.", "comments": 12},
    {"domain": "Python", "title": "What are the data types in Python?", "author": "User2", "answers": "Data types include integers, floats, strings, lists, tuples, dictionaries, and booleans.", "comments": 9},
    {"domain": "Python", "title": "Explain object-oriented programming in Python.", "author": "User3", "answers": "Python supports OOP concepts like classes, objects, inheritance, polymorphism, and encapsulation.", "comments": 15},

    {"domain": "Python", "title": "What are modules and packages in Python?", "author": "User4", "answers": "Modules are single files containing Python code, while packages are a collection of related modules.", "comments": 7},
    {"domain": "Python", "title": "How to handle exceptions in Python?", "author": "User5", "answers": "Use try-except blocks to catch and handle exceptions.", "comments": 11},
    {"domain": "Python", "title": "What is the purpose of the 'self' keyword in Python?", "author": "User6", "answers": "It refers to the instance of the class.", "comments": 8},
    {"domain": "Python", "title": "What are decorators in Python?", "author": "User7", "answers": "Decorators are functions that modify the behavior of other functions.", "comments": 10},
    {"domain": "Python", "title": "How to write a simple Python program to print 'Hello, World!'?", "author": "User8", "answers": "print('Hello, World!')", "comments": 13},

    {"domain": "Django", "title": "What is Django?", "author": "Mem3", "answers": "Django is a high-level Python web framework.", "comments": 12},
    {"domain": "Django", "title": "What are Django models?", "author": "Mem4", "answers": "Models define the structure of data in Django.", "comments": 6},
    {"domain": "Django", "title": "Explain the MVC architecture in Django.", "author": "User9", "answers": "Django follows the MVT (Model-View-Template) pattern.", "comments": 9},
    {"domain": "Django", "title": "How to create a new Django project?", "author": "User10", "answers": "Use the command 'django-admin startproject myproject'", "comments": 10},
    {"domain": "Django", "title": "What are Django views?", "author": "User11", "answers": "Views are Python functions that handle requests and return responses.", "comments": 8},

    {"domain": "Django", "title": "What is the role of the URLconf in Django?", "author": "User12", "answers": "It maps URLs to specific views.", "comments": 7},
    {"domain": "Django", "title": "How to handle forms in Django?", "author": "User13", "answers": "Use Django's built-in form classes.", "comments": 11},
    {"domain": "Django", "title": "What are Django templates?", "author": "User14", "answers": "Templates are used to generate HTML dynamically.", "comments": 12},
    {"domain": "Django", "title": "How to implement user authentication in Django?", "author": "User15", "answers": "Use the Django authentication system.", "comments": 15},
    {"domain": "Django", "title": "What are Django middleware?", "author": "User16", "answers": "Middleware modifies incoming and outgoing HTTP requests/responses.", "comments": 9},

    {"domain": "React", "title": "What is React?", "author": "Hari", "answers": "React is a JavaScript library for building user interfaces.", "comments": 15},
    {"domain": "React", "title": "What are components in React?", "author": "User17", "answers": "Components are reusable building blocks of a React UI.", "comments": 12},
    {"domain": "React", "title": "Explain JSX in React.", "author": "User18", "answers": "JSX allows writing HTML-like syntax within JavaScript.", "comments": 10},
    {"domain": "React", "title": "What is state in React?", "author": "User19", "answers": "State is an internal data store that can change over time.", "comments": 14},
    {"domain": "React", "title": "What are props in React?", "author": "User20", "answers": "Props are read-only properties that pass data from parent to child components.", "comments": 11},
    
    {"domain": "React", "title": "How to handle events in React?", "author": "User21", "answers": "Use event handlers like onClick, onChange, etc.", "comments": 9},
    {"domain": "React", "title": "What is the purpose of the key prop in React?", "author": "User22", "answers": "Keys help React efficiently update lists.", "comments": 8},
    {"domain": "React", "title": "Explain the concept of 'lifting state' in React.", "author": "User23", "answers": "Sharing state between multiple child components.", "comments": 13},
    {"domain": "React", "title": "What are React hooks?", "author": "User24", "answers": "Functions that let you 'hook into' React state and lifecycle features from function components.", "comments": 16},
    {"domain": "React", "title": "How to perform asynchronous operations in React?", "author": "User25", "answers": "Use useEffect hook with async/await or promises.", "comments": 15},
]


MONGO_URI = "mongodb+srv://1QoSRtE75wSEibZJ:1QoSRtE75wSEibZJ@cluster0.mregq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client = pymongo.MongoClient(MONGO_URI)
    db = client['Q&A_Platform'] 
    UsersSignup = db['UserData'] 
    Q_A = db['Q&A']
except Exception as e:
    raise ConnectionError(f"Failed to connect to MongoDB: {e}")

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            required_fields = ["Name", "email", "password", "confirmPassword"]
            for field in required_fields:
                if not data.get(field):
                    return JsonResponse({"error": f"{field} is required."}, status=400)
            if data.get("password") != data.get("confirmPassword"):
                return JsonResponse({"error": "Passwords do not match."}, status=400)

            role = 'admin' if data.get("email") == "admin@example.com" else 'user'

            user_data = {
                "name": data.get("Name"),
                "email": data.get("email"),
                "password": data.get("password"),
                "role": role,
            }

            UsersSignup.insert_one(user_data)

            return JsonResponse({"message": "User signed up successfully!"}, status=201)

        except Exception as e:
            return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=500)

    return render(request, "signup.html")


@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            email = data.get("email")
            password = data.get("password")

            # Check if email and password are provided
            if not email or not password:
                return JsonResponse({"error": "Email and password are required."}, status=400)

            # Fetch the user from the database
            user = UsersSignup.find_one({"email": email})

            # If the user is not found
            if not user:
                return JsonResponse({"error": "User not found or email is incorrect."}, status=404)

            # If the password does not match
            if user.get("password") != password:
                return JsonResponse({"error": "Invalid password."}, status=401)

            # Fetch the user's role from the database
            role = user.get("role")

            # Check if the role exists and is valid
            if role not in ['admin', 'user']:
                return JsonResponse({"error": "Unknown role. Please contact support."}, status=403)

            # Construct the response data
            response_data = {
                "message": "Login successful!",
                "user": {
                    "id": str(user.get("_id")),
                    "email": user.get("email"),
                    "role": role,
                    "name": user.get("name"),
                },
            }

            return JsonResponse(response_data, status=200)

        except Exception as e:
            return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=500)

    return render(request, "login.html")


@csrf_exempt
def home(request):
    domain_filter = request.GET.get("domain", "")
    search_query = request.GET.get("q", "")

    filtered_questions = questions_data
    if domain_filter:
        filtered_questions = [q for q in filtered_questions if q["domain"] == domain_filter]
    if search_query:
        filtered_questions = [q for q in filtered_questions if search_query.lower() in q["title"].lower()]

    paginator = Paginator(filtered_questions, 5)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    domains = sorted(set(q["domain"] for q in questions_data))

    return render(request, "home.html", {"questions": page_obj, "domains": domains, "domain_filter": domain_filter, "search_query": search_query})


@csrf_exempt
def tags(request):
    domain_filter = request.GET.get("domain", "")
    search_query = request.GET.get("q", "")

    filtered_questions = questions_data
    if domain_filter:
        filtered_questions = [q for q in filtered_questions if q["domain"] == domain_filter]
    if search_query:
        filtered_questions = [q for q in filtered_questions if search_query.lower() in q["title"].lower()]

    paginator = Paginator(filtered_questions, 5)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    domains = sorted(set(q["domain"] for q in questions_data))

    return render(request, "tags.html", {"questions": page_obj, "domains": domains, "domain_filter": domain_filter, "search_query": search_query})

@csrf_exempt
def questions(request):
    search_query = request.GET.get("q", "")
    filtered_questions = questions_data

    if search_query:
        filtered_questions = [q for q in filtered_questions if search_query.lower() in q["title"].lower()]

    paginator = Paginator(filtered_questions, 5)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    return render(request, "questions.html", {"questions": page_obj,"search_query": search_query})


@csrf_exempt
def adminhome(request):
    domain_filter = request.GET.get("domain", "")
    search_query = request.GET.get("q", "")

    filtered_questions = questions_data
    if domain_filter:
        filtered_questions = [q for q in filtered_questions if q["domain"] == domain_filter]
    if search_query:
        filtered_questions = [q for q in filtered_questions if search_query.lower() in q["title"].lower()]

    paginator = Paginator(filtered_questions, 5)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    domains = sorted(set(q["domain"] for q in questions_data))

    return render(request, "adminhome.html", {"questions": page_obj, "domains": domains, "domain_filter": domain_filter, "search_query": search_query})

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            required_fields = ["Name", "email", "password", "confirmPassword"]
            for field in required_fields:
                if not data.get(field):
                    return JsonResponse({"error": f"{field} is required."}, status=400)
            if data.get("password") != data.get("confirmPassword"):
                return JsonResponse({"error": "Passwords do not match."}, status=400)

            role = 'admin' if data.get("email") == "admin@example.com" else 'user'

            user_data = {
                "name": data.get("Name"),
                "email": data.get("email"),
                "password": data.get("password"),
                "role": role,
            }

            UsersSignup.insert_one(user_data)

            return JsonResponse({"message": "Uploaded successfully!"}, status=201)

        except Exception as e:
            return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=500)

    return render(request, "Upload.html")



