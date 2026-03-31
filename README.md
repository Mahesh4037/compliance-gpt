# ComplianceGPT MVP

This repository now contains a complete MVP scaffold under `compliancegpt/`:

- `compliancegpt/backend`: FastAPI + Supabase + Gemini grounding + scrapers + scheduler + alerts
- `compliancegpt/frontend`: Next.js 14 App Router dashboard and auth flows

## 1. Create Supabase Project and Run Schema

1. Sign in to Supabase and create a new free-tier project.
2. Open SQL Editor.
3. Copy SQL from `compliancegpt/backend/database/schema.sql` and execute it.
4. In Project Settings -> API, copy:
   - Project URL as `SUPABASE_URL`
   - Service role key as `SUPABASE_SERVICE_KEY`

## 2. Get Gemini API Key (Free Tier)

1. Open Google AI Studio and create an API key.
2. Ensure your key can access Gemini 2.5 Flash.
3. Grounding with Google Search is enabled in code via:
   - `tools=[types.Tool(google_search=types.GoogleSearch())]`
4. Add key to backend env as `GEMINI_API_KEY`.

## 3. Set Up WhatsApp Business Cloud API

1. Go to Meta Developer Portal and create an app.
2. Add WhatsApp product.
3. Copy temporary or permanent access token -> `WHATSAPP_TOKEN`.
4. Copy phone number ID -> `WHATSAPP_PHONE_NUMBER_ID`.
5. Add recipient numbers in test mode as needed.

## 4. Set Up Resend API Key

1. Create free Resend account.
2. Generate API key.
3. Add as `RESEND_API_KEY`.
4. Configure sending domain for production deliverability.

## 5. Backend Local Setup

1. `cd compliancegpt/backend`
2. `python -m venv .venv`
3. Activate virtual environment.
4. `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and fill values.
6. Run: `uvicorn main:app --reload`

## 6. Frontend Local Setup

1. `cd compliancegpt/frontend`
2. `npm install`
3. Copy `.env.local.example` to `.env.local`
4. Set `NEXT_PUBLIC_API_URL` to backend URL, for local use `http://localhost:8000`
5. Run: `npm run dev`

## 7. Deploy Backend to Railway (Free Tier)

1. Create Railway project from GitHub repo.
2. Set root directory to `compliancegpt/backend`.
3. Add all backend environment variables from `.env.example`.
4. Railway detects Dockerfile or run command.
5. Confirm `/health` endpoint returns `{ "status": "ok" }`.

## 8. Deploy Frontend to Vercel (Free Tier)

1. Import repository to Vercel.
2. Set project root to `compliancegpt/frontend`.
3. Add env var `NEXT_PUBLIC_API_URL` with Railway backend URL.
4. Deploy and verify:
   - Landing page
   - Register/Login
   - Dashboard endpoints

## Environment Files

- Backend example: `compliancegpt/backend/.env.example`
- Frontend example: `compliancegpt/frontend/.env.local.example`

## API Summary

- Auth: `/api/auth/register`, `/api/auth/login`
- Regulations: `/api/regulations`, `/api/regulations/{id}`, `/api/regulations/relevant`
- Dashboard: `/api/dashboard/summary`, `/api/dashboard/calendar`, `/api/dashboard/ca-overview`
- Businesses: `/api/businesses/me`, `/api/businesses/clients`
- Alerts: `/api/alerts`, `/api/alerts/send-test`
