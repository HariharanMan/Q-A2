from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import JsonResponse

# Predefined questions and answers
questions_data = [
    {"title": "How to learn Python?", "details": "What are the best resources?", "author": "Hari", "answers": 5, "comments": 10},
    {"title": "What is Django?", "details": "Can someone explain Django?", "author": "Mem2", "answers": 8, "comments": 15},
    {"title": "Difference between list and tuple?", "details": "Key differences in Python.", "author": "Mem3", "answers": 12, "comments": 20},
    {"title": "What is React?", "details": "How does React work?", "author": "Mem4", "answers": 6, "comments": 12},
    {"title": "How to manage state in React?", "details": "State management best practices.", "author": "Hari", "answers": 10, "comments": 18},
    {"title": "What is Flask?", "details": "How Flask differs from Django?", "author": "Mem5", "answers": 3, "comments": 5},
    {"title": "What is REST API?", "details": "Explain REST API with examples.", "author": "Mem6", "answers": 7, "comments": 8},
    {"title": "Best practices for JavaScript?", "details": "Modern JavaScript practices.", "author": "Mem7", "answers": 9, "comments": 15},
    {"title": "What is TypeScript?", "details": "How does TypeScript enhance JS?", "author": "Mem8", "answers": 4, "comments": 6},
    {"title": "How to learn CSS?", "details": "Resources for mastering CSS.", "author": "Hari", "answers": 11, "comments": 22},
]

def home(request):
    # Get search query
    search_query = request.GET.get("q", "")
    filtered_questions = [q for q in questions_data if search_query.lower() in q["title"].lower()] if search_query else questions_data

    # Paginate questions (5 per page)
    paginator = Paginator(filtered_questions, 5)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    return render(request, "home.html", {"questions": page_obj, "search_query": search_query})
