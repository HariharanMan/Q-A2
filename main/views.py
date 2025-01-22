from django.shortcuts import render
from django.core.paginator import Paginator

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


def Questions(request):
    search_query = request.GET.get("q", "")
    filtered_questions = questions_data

    if search_query:
        filtered_questions = [q for q in filtered_questions if search_query.lower() in q["title"].lower()]

    paginator = Paginator(filtered_questions, 5)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    return render(request, "Questions.html", {"questions": page_obj,"search_query": search_query})


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

