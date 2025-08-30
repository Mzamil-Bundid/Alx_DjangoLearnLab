Tech Blog API - Backend Capstone Project
Welcome to the Tech Blog API, a backend system for a blogging platform focused on technology and programming tutorials. This project was created as part of my capstone assignment to demonstrate backend development skills using Django and Django REST Framework (DRF).

Project Title: Tech Blog API
Created by: Mzamil Bundid
Project Overview
The Tech Blog API allows users to create, manage, and share blog posts categorized by topics (e.g., Python, Web Development), save drafts, filter posts by category or author, and search by title or tags. A unique bookmark feature enables users to save and revisit favorite tutorials. The API includes user authentication (via JWT) to secure content creation and editing.
Why This Project?

Personal Relevance: Aligns with my passion for coding and reading tech blogs.
Originality: The bookmark feature adds a unique twist to the pre-made Blogging Platform API idea.
Feasibility: Leverages core CRUD operations, authentication, and filtering using Django and DRF within a 5-week timeline.
Problem Solved: Helps coders share and discover tutorials while addressing the frustration of losing track of useful articles.

Main Features

User Authentication: Register, log in, and log out with JWT; only authenticated users can create, update, or delete posts.
Post Management (CRUD): Create, read, update, and delete posts with title, content, category, and publication status (published or draft).
Category Management: Assign and filter posts by categories (e.g., "Python", "Web Development").
Filtering and Search: Filter posts by category, author, or search by title/tags.
Bookmark Feature: Save and view a list of bookmarked posts.
Basic Comment System: Add and view comments on posts.

Project Structure
The project follows modular Django app organization for clarity and maintainability:
texttech-blog-api/
├── core/              # Project-wide settings, custom error handling, logging
│   ├── settings.py
│   ├── urls.py
│   └── utils.py
├── users/             # User authentication and profiles
│   ├── models.py      # User (extends Django's AbstractUser)
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── posts/             # Blog posts, categories, bookmarks, and comments
│   ├── models.py      # Post, Category, Bookmark, Comment
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── manage.py
└── requirements.txt
Database Schema
The schema supports the features with normalized models and relationships:

User: Extends AbstractUser with an optional bio field.
Category: name (unique), created_at.
Post: title, content, author (ForeignKey to User), category (nullable), is_draft, created_at, updated_at.
Bookmark: user and post (unique together to prevent duplicates), created_at.
Comment: post, author, content, created_at.

API Endpoints
The API follows RESTful conventions with clear endpoints and appropriate HTTP status codes:































































































MethodEndpointDescriptionStatus CodesPOST/api/auth/register/Register a new user201, 400POST/api/auth/login/Log in and return JWT token200, 401GET/api/posts/List all published posts200, 400GET/api/posts/:id/Get a specific post200, 404POST/api/posts/Create a new post (authenticated)201, 400, 401PUT/api/posts/:id/Update a post (authenticated, author)200, 400, 401, 403DELETE/api/posts/:id/Delete a post (authenticated, author)204, 401, 403, 404GET/api/posts/?category={name}Filter posts by category200, 400GET/api/posts/?author={id}Filter posts by author200, 400GET/api/posts/?search={query}Search posts by title or tags200, 400POST/api/bookmarks/Bookmark a post (authenticated)201, 400, 401GET/api/bookmarks/List user’s bookmarked posts200, 401POST/api/comments/Add a comment to a post (authenticated)201, 400, 401GET/api/posts/:id/comments/List comments for a post200, 404
Note: Authentication via JWT is required for POST, PUT, DELETE endpoints.
Getting Started
Prerequisites

Python 3.8+
pip (Python package manager)
Virtual environment (e.g., virtualenv or venv)

Installation

Clone the Repository
bashgit clone https://github.com/Mzamil-Bundid/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab

Set Up a Virtual Environment
bashpython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Dependencies
Install the required packages listed in requirements.txt:
bashpip install -r requirements.txt
Note: Ensure requirements.txt includes django, djangorestframework, djangorestframework-simplejwt, etc.
Apply Migrations
bashpython manage.py migrate

Run the Development Server
bashpython manage.py runserver
Access the API at http://127.0.0.1:8000/.

Testing

Use Postman to test API endpoints (e.g., POST /api/auth/register/ with {"username": "user1", "email": "user@example.com", "password": "pass123"}).
Write unit tests using Django’s test framework (to be added in tests.py files).

Project Timeline

Week 1 (Jul 28 – Aug 3): Planning, setup, initial models, and migrations.
Week 2 (Aug 4 – Aug 10): Authentication and core CRUD.
Week 3 (Aug 11 – Aug 17): Filtering and bookmark feature.
Week 4 (Aug 18 – Aug 24): Comments and documentation.
Week 5 (Aug 25 – Sep 3): Polish, deployment, and QA review.
Deadline: September 3, 2025 (extended to Sep 17, 2025 if needed).

Tech Stack

Backend: Django, Django REST Framework
Database: SQLite (development), PostgreSQL (production)
Authentication: djangorestframework-simplejwt
Version Control: Git/GitHub
Deployment: Heroku

Additional Notes

ERD Tool: The Entity Relationship Diagram was created using dbdiagram.io.
Challenges: Initial setup and JWT configuration were addressed using Django/DRF documentation.
Next Steps: Complete CRUD, filtering, bookmarking, comments, testing, and deployment.
Support: Feedback from a mentor is optional but recommended.

License
This project is for educational purposes and does not have a formal license yet.
Contributions
Feel free to fork this repository, submit issues, or provide feedback!
