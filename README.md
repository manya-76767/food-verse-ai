# Food Verse AI — Multimodal Food Intelligence Agent

A responsive college-project demo for food image recognition, visual freshness
checks, restaurant hygiene observations, ingredient-based recipes, and
personalized meal suggestions.

## Features

- **Food recognition:** upload an image and receive likely visible food matches.
- **Freshness detection:** describe visible signs that may relate to freshness.
  Image analysis cannot guarantee food safety.
- **Restaurant hygiene monitoring:** review visible potential hygiene concerns in
  a still image. Video analysis is not implemented yet.
- **Smart cooking assistant:** turn available ingredients into a measured recipe
  with servings, timing, and cooking steps.
- **Nutrition planner:** generate meal suggestions from dietary preferences,
  allergies, meal goals, and meals per day. All nutrition values are estimates,
  not medical advice.
- **Health check:** `GET /api/food-verse/healthz` reports API and AI configuration
  status without exposing secrets.

AI results are never mocked. If the AI provider is not configured, the API
returns a setup message and the interface shows it instead of inventing a
prediction.

## Technology

- Frontend: React, TypeScript/JSX, Vite, CSS, and responsive layouts.
- Backend: Python Flask.
- AI provider: OpenAI-compatible Chat Completions API, called only from Flask.
- API contract/client: OpenAPI with generated React Query hooks.

## Requirements

- Node.js and pnpm for the workspace frontend.
- Python 3.10 or newer for the Flask API.
- An OpenAI API key for live AI analysis and generation.

## Configure the AI provider

Copy `.env.example` to `.env` and set the key in the backend environment:

```env
OPENAI_API_KEY=your-key
OPENAI_MODEL=gpt-5.4-mini
OPENAI_BASE_URL=https://api.openai.com/v1
```

Keep `.env` out of Git. On Replit, add `OPENAI_API_KEY` through Secrets; do not
put it in frontend variables or source code. `OPENAI_MODEL` and `OPENAI_BASE_URL`
are optional server-side settings for a compatible provider/model. Without a
key, the health endpoint reports `aiConfigured: false` and AI requests return
HTTP 503 with setup guidance.

## Run in Replit

Open the Food Verse AI preview. The project has separate managed services for
the React app and Flask API, routed through the preview. Add `OPENAI_API_KEY` to
Replit Secrets to enable live AI calls. The API service can be checked at
`/api/food-verse/healthz`.

## Run locally from the repository root

Install the JavaScript workspace dependencies and Python backend dependencies:

```bash
pnpm install
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r artifacts/food-verse-ai/backend/requirements.txt
cp .env.example .env
```

Set `OPENAI_API_KEY` in `.env` if you want live AI results. Start Flask in one
terminal:

```bash
set -a && source .env && set +a
PORT=5000 .venv/bin/python artifacts/food-verse-ai/backend/app.py
```

Start the React app in a second terminal:

```bash
VITE_API_BASE_URL=http://localhost:5000 PORT=5173 BASE_PATH=/ pnpm --filter @workspace/food-verse-ai run dev
```

The Replit preview routes `/api/food-verse` to Flask automatically. For a
standalone frontend deployment, configure its API base URL/routing so requests
to `/api/food-verse/*` reach the Flask service.

## API

| Method | Path | Purpose |
| --- | --- | --- |
| `GET` | `/api/food-verse/healthz` | API and provider configuration status |
| `POST` | `/api/food-verse/image-analysis` | Food recognition, freshness, or hygiene image analysis |
| `POST` | `/api/food-verse/recipes` | Ingredient-based recipe generation |
| `POST` | `/api/food-verse/nutrition` | Personalized meal recommendations |

Image requests accept a PNG, JPG, or WebP data URL. Images are limited to 8 MB
and are sent to the configured AI provider for processing; the app does not
persist uploaded images.

## Validate

```bash
pnpm --filter @workspace/food-verse-ai run typecheck
pnpm --filter @workspace/food-verse-ai run build
python -m compileall artifacts/food-verse-ai/backend
```

The app also exposes the health check above for a quick backend status check.

## Publish the source to GitHub

1. Create an empty repository on GitHub.
2. In Replit, open the Git pane and connect the project to that repository.
3. Review the changed files, then commit and push the source.
4. Confirm `.env` is not included; the repository includes only `.env.example`.
5. Add `OPENAI_API_KEY` to the deployment's secret/environment settings rather
   than committing it.

Alternatively, from a configured Git checkout, use:

```bash
git add .
git commit -m "Build Food Verse AI"
git branch -M main
git remote add origin https://github.com/YOUR-ACCOUNT/YOUR-REPOSITORY.git
git push -u origin main
```

## Deploy

The Replit app is set up with a static React frontend and a Flask API service.
Use Replit's **Publish** action to publish both services with their configured
routes. Before publishing, add `OPENAI_API_KEY` to Replit Secrets for the
deployment environment. The Flask service listens on its configured port and
serves `/api/food-verse/*` through Gunicorn; preserve that route when deploying
the frontend and backend separately on another host.

## Safety and limitations

- Image analysis is not a food-safety determination, medical advice, or a
  restaurant inspection.
- Nutrition estimates vary by ingredients, brands, and portions.
- Video analysis, user accounts, persistent history, and offline AI are not
  implemented in this project version.
