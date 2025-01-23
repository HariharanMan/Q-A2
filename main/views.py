from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
import pymongo
import json




MONGO_URI = "mongodb+srv://1QoSRtE75wSEibZJ:1QoSRtE75wSEibZJ@cluster0.mregq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client = pymongo.MongoClient(MONGO_URI)
    db = client['Q&A_Platform'] 
    UsersSignup = db['UserData'] 
    questions = db['questions']

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
            data = json.loads(request.body)
            email = data.get("email")
            password = data.get("password")

            if not email or not password:
                return JsonResponse({"error": "Email and password are required."}, status=400)

            user = UsersSignup.find_one({"email": email})

            if not user:
                return JsonResponse({"error": "User not found or email is incorrect."}, status=404)

            if user.get("password") != password:
                return JsonResponse({"error": "Invalid password."}, status=401)

            role = user.get("role")

            if role not in ['admin', 'user']:
                return JsonResponse({"error": "Unknown role. Please contact support."}, status=403)

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

    filtered_questions = questions
    if domain_filter:
        filtered_questions = [q for q in filtered_questions if q["domain"] == domain_filter]
    if search_query:
        filtered_questions = [q for q in filtered_questions if search_query.lower() in q["title"].lower()]

    paginator = Paginator(filtered_questions, 5)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    domains = sorted(set(q["domain"] for q in questions))

    return render(request, "home.html", {"questions": page_obj, "domains": domains, "domain_filter": domain_filter, "search_query": search_query})


@csrf_exempt
def tags(request):
    domain_filter = request.GET.get("domain", "")
    search_query = request.GET.get("q", "")

    filtered_questions = questions
    if domain_filter:
        filtered_questions = [q for q in filtered_questions if q["domain"] == domain_filter]
    if search_query:
        filtered_questions = [q for q in filtered_questions if search_query.lower() in q["title"].lower()]

    paginator = Paginator(filtered_questions, 5)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    domains = sorted(set(q["domain"] for q in questions))

    return render(request, "tags.html", {"questions": page_obj, "domains": domains, "domain_filter": domain_filter, "search_query": search_query})

@csrf_exempt
def questions(request):
    search_query = request.GET.get("q", "")
    filtered_questions = questions

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

    filtered_questions = questions
    if domain_filter:
        filtered_questions = [q for q in filtered_questions if q["domain"] == domain_filter]
    if search_query:
        filtered_questions = [q for q in filtered_questions if search_query.lower() in q["title"].lower()]

    paginator = Paginator(filtered_questions, 5)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    domains = sorted(set(q["domain"] for q in questions))

    return render(request, "adminhome.html", {"questions": page_obj, "domains": domains, "domain_filter": domain_filter, "search_query": search_query})

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            required_fields = ["domain", "name", "question", "answer"]
            for field in required_fields:
                if not data.get(field):
                    return JsonResponse({"error": f"{field} is required."}, status=400)
                
            data = {
                "domain": data.get("domain"),
                "name": data.get("name"),
                "question": data.get("question"),
                "answer": data.get("answer"),
            }

            Q_A.insert_one(data)

            return JsonResponse({"message": "Uploaded successfully!"}, status=201)

        except Exception as e:
            return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=500)

    return render(request, "Upload.html")



