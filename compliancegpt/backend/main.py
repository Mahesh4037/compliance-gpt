from dotenv import load_dotenv
load_dotenv()

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import admin, alerts, auth, businesses, chat, compliance_profile, dashboard, deadlines, regulations, tasks
from scheduler.jobs import start_scheduler


@asynccontextmanager
async def lifespan(app: FastAPI):
    start_scheduler()
    yield


app = FastAPI(title="ComplianceGPT API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth")
app.include_router(regulations.router, prefix="/api/regulations")
app.include_router(businesses.router, prefix="/api/businesses")
app.include_router(alerts.router, prefix="/api/alerts")
app.include_router(dashboard.router, prefix="/api/dashboard")
app.include_router(admin.router, prefix="/api/admin")
app.include_router(chat.router, prefix="/api/chat")
app.include_router(deadlines.router, prefix="/api/deadlines")
app.include_router(tasks.router, prefix="/api/tasks")
app.include_router(compliance_profile.router, prefix="/api/compliance-profile")


@app.get("/health")
def health():
    return {"status": "ok"}
