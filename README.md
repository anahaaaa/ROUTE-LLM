# Route-LLM

A self-hosted LLM gateway that routes requests across multiple AI providers
with automatic fallback, semantic caching, and cost tracking.

---

## Why this project?

Calling LLM APIs directly from your application creates three problems:

- **Reliability** — if your provider goes down, your app goes down
- **Cost** — duplicate and near-duplicate requests pay full price every time
- **Visibility** — no easy way to track spend, latency, or failures per request

Route-LLM sits between your app and the providers and handles all three.

---

## Tech Stack

| | |
|---|---|
| API | FastAPI |
| Database | PostgreSQL 17 + pgvector |
| Cache & Rate Limiting | Redis 7 |
| Migrations | Alembic |
| Testing | pytest |
| Infra | Docker + Docker Compose |
| CI | GitHub Actions |

---

## Project Structure

## Project Structure

    route-llm/
    ├── gateway/
    │ ├── api/ # routes
    │ ├── auth/ # JWT + API key
    │ ├── services/ # router, cache, circuit breaker, rate limiter
    │ ├── routing/ # cost, capability, latency, fallback strategies
    │ ├── providers/ # OpenAI, Anthropic, Ollama adapters
    │ ├── models/ # SQLAlchemy ORM
    │ ├── repositories/ # DB access layer
    │ └── core/ # config, logging, exceptions
    ├── tests/
    ├── alembic/
    ├── scripts/
    ├── docker-compose.yml
    ├── Dockerfile
    └── DESIGN.md

---

---

## Getting Started

```bash
git clone https://github.com/anahaaaa/route-llm.git
cd route-llm

cp .env.example .env
# add your API keys to .env

docker compose up
# API: http://localhost:8000
# Docs: http://localhost:8000/docs
```

---

## Architecture & Design Decisions

See [DESIGN.md](./DESIGN.md) — covers the full request flow, component
responsibilities, and the reasoning behind every major decision.

---

## Status

🚧 Active development — v1.0 in progress

- [x] Docker + CI setup
- [ ] Core config and logging
- [ ] Database models and migrations
- [ ] Provider abstraction
- [ ] Circuit breaker
- [ ] Rate limiter
- [ ] Semantic cache
- [ ] Router service
- [ ] API routes
- [ ] Test suite

---

## License

MIT

## Author

**Anagha R S** — M.Tech AI/CS @ CUSAT | Ex-Research Intern @ IIT Madras

[GitHub](https://github.com/anahaaaa)
[LinkedIn](https://linkedin.com/in/anagha-r-285872370)