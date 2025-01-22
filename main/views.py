from django.shortcuts import render

def home(request):
    questions = [
        {
            "title": "How to learn Python?",
            "details": "What are the best resources and methods for learning Python?",
            "author": "Hari",
            "answers": 5,
            "comments": 10,
        },
        {
            "title": "What is Django?",
            "details": "Can someone explain what Django is and its main use cases?",
            "author": "Mem2",
            "answers": 8,
            "comments": 15,
        },
        {
            "title": "Difference between list and tuple?",
            "details": "What are the key differences between Python lists and tuples?",
            "author": "Mem3",
            "answers": 12,
            "comments": 20,
        },
        {
            "title": "What is React?",
            "details": "How does React work, and why is it so popular?",
            "author": "Mem4",
            "answers": 6,
            "comments": 12,
        },
        {
            "title": "How to manage state in React?",
            "details": "What are the best practices for managing state in large React applications?",
            "author": "Hari",
            "answers": 10,
            "comments": 18,
        },
    ]

    return render(request, "home.html", {"questions": questions})
