# Digital Vocabulary API

Digital Vocabulary is a Django REST API project that allows users to create their own vocabulary lists, manage words, follow other users, and practice word meanings through quiz-style questions.

## Live Demo

The API is deployed on Render and uses a PostgreSQL database hosted on Neon.

- Swagger UI → https://digital-vocabulary.onrender.com/api/schema/swagger-ui/
- Admin panel → https://digital-vocabulary.onrender.com/admin/

> The service runs on Render's free plan. After a period of inactivity the first request may take 30 to 50 seconds while the server wakes up.

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
- PostgreSQL (Neon)
- Gunicorn
- WhiteNoise
- Render

## Project Structure

- profiles: user profiles, authentication-related endpoints, and follow system
- vocabularies: vocabulary and word management
- exercises: quiz question generation
- digitalvocabulary: Django project settings and URL routing

## Requirements

Install the dependencies with the following command.

```bash
pip install -r requirements.txt
```

## Local Development Setup

1. Clone the repository
2. Navigate to the project folder
3. Create and activate a virtual environment

On Windows

```bash
python -m venv myenv
myenv\Scripts\activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Create a `.env` file with the required environment variables

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

## Deployment

The project runs on Render as a web service and connects to a PostgreSQL database on Neon.

- Build command → `./build.sh`
- Start command → `cd digitalvocabulary && gunicorn digitalvocabulary.wsgi`
- Environment variables → `SECRET_KEY` and `DATABASE_URL`

`build.sh` installs the dependencies, collects the static files and applies the database migrations on every deploy. Every push to the `master` branch starts a new deploy automatically.

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

- Swagger UI → `/api/schema/swagger-ui/`
- Raw schema → `/api/schema/`


## Notes

The project currently uses a custom user model and is designed as a backend API service. If you want, it can later be expanded with a frontend client or additional learning features.
