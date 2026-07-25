# Digital Vocabulary API

Digital Vocabulary is a Django REST API project that allows users to create their own vocabulary lists, manage words, follow other users, and practice word meanings through quiz-style questions.

## Features

- User registration and authentication with JWT
- Custom user and profile management
- Follow / unfollow other profiles
- Create, read, update, and delete vocabulary sets
- Add and manage words inside vocabularies
- Copy vocabularies between profiles
- Generate quiz questions from stored words
- API documentation with Swagger 

## Tech Stack

- Python
- Django
- Django REST Framework
- Simple JWT
- DRF Spectacular
- PostgreSQL
- Gunicorn

## Project Structure

- profiles: user profiles, authentication-related endpoints, and follow system
- vocabularies: vocabulary and word management
- exercises: quiz question generation
- digitalvocabulary: Django project settings and URL routing

## Requirements

Install the dependencies with:

```bash
pip install -r requirements.txt
```

## Local Development Setup

1. Clone the repository
2. Navigate to the project folder
3. Create and activate a virtual environment

On Windows:

```bash
python -m venv myenv
myenv\Scripts\activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Create a `.env` file with the required environment variables:

```env
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:password@localhost:5432/digitalvocabulary
```

6. Run database migrations

```bash
cd digitalvocabulary
python manage.py migrate
```

7. Start the development server

```bash
python manage.py runserver
```

## API Endpoints

### Authentication

- POST `/api/profiles/register/`
- POST `/api/profiles/token/`
- POST `/api/profiles/token/refresh/`

### Profiles

- GET `/api/profiles/search/`
- POST `/api/profiles/follow/<username>/`
- POST `/api/profiles/unfollow/<username>/`
- GET `/api/profiles/followed-list/`

### Vocabularies

- GET/POST `/api/vocabularies/`
- GET/PUT/DELETE `/api/vocabularies/<id>/`
- GET/POST `/api/vocabularies/<vocabulary_id>/words/`
- GET/PUT/DELETE `/api/vocabularies/<vocabulary_id>/words/<word_id>/`
- POST `/api/vocabularies/<vocabulary_id>/copy/`

### Exercises

- GET `/api/exercises/question/`

## API Documentation

The project includes OpenAPI schema documentation.

> You can test the live API directly here: https://my-digital-vocabulary-a0fc9931d037.herokuapp.com/api/schema/swagger-ui/

- Swagger UI: `/api/schema/swagger-ui/`
- Raw schema: `/api/schema/`

## Deployment

This project is configured for deployment with Heroku using the included Procfile.

## Notes

The project currently uses a custom user model and is designed as a backend API service. If you want, it can later be expanded with a frontend client or additional learning features.
