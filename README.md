# 🚀 Enterprise-Grade FastAPI Social Backend

A production-ready social media engine built for performance, security, and scalability.

## 🏗️ Technical Architecture
- **Backend:** FastAPI (Python 3.11) with Asynchronous support.
- **Database:** PostgreSQL managed via SQLAlchemy ORM.
- **Migrations:** Alembic for version-controlled schema evolution.
- **Security:** JWT (JSON Web Tokens) & OAuth2 Password Grant flow.
- **Testing:** Pytest for Unit and Integration testing.
- **Infrastructure:** Dockerized multi-container orchestration.

## 🌟 Key Features
- **Complex Querying:** Optimized SQL Joins for retrieving posts with aggregated vote counts.
- **Object-Level Permissions:** Strict authorization logic ensuring users only modify their own content.
- **Automated CI/CD:** Integrated GitHub Actions for automated testing and deployment readiness.
- **Type-Safe Config:** Pydantic-based environment variable validation.

## 🚦 Getting Started
1. Clone the repo.
2. Create a `.env` file based on the provided configuration.
3. Run `docker-compose up --build`.
