from fastapi import FastAPI
from app.database import engine, Base
from app.routes import create_student, get_student, update_student, delete_student, ai_query

# Create SQLite database tables automatically on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="EWB Student Management & AI API",
    description="Production-grade FastAPI backend with SQLite persistence and optional Ollama AI integration.",
    version="1.0.0"
)

# Include Modular Routers
app.include_router(create_student.router)
app.include_router(get_student.router)
app.include_router(update_student.router)
app.include_router(delete_student.router)
app.include_router(ai_query.router)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the EWB Student Management API!",
        "documentation": "Visit /docs for interactive Swagger UI."
    }