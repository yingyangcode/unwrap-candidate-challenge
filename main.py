from fastapi import FastAPI
from api.books.router import router as books_router
from api.customers.router import router as customers_router
from api.checkouts.router import router as checkouts_router
from api.system.router import router as system_router
from api.error_handlers import library_exception_handler
from app.exceptions import LibraryException

app = FastAPI(title="Library Management System", version="1.0.0")

# Add global exception handler
app.add_exception_handler(LibraryException, library_exception_handler)

API_PREFIX = "/api"
app.include_router(books_router, prefix=API_PREFIX, tags=["books"])
app.include_router(customers_router, prefix=API_PREFIX, tags=["customers"])
app.include_router(checkouts_router, prefix=API_PREFIX, tags=["checkouts"])
app.include_router(system_router, prefix=API_PREFIX, tags=["system"])

@app.get("/")
def health_check():
    return {"message": "Library Management System API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)