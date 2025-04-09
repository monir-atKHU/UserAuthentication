from fastapi import FastAPI
from api import router  # Make sure you're importing the router here, not 'api'

server = FastAPI(debug=True)

server.include_router(router)

# Optional: test root endpoint
@server.get("/")
def read_root():
    return {"message": "FastAPI is working"}

# Debug print
print("✅ Registered routes in server:")
for route in server.routes:
    print(f"  {route.path} → {route.name}")
