## Record CRUD API (Atom API - First Commit)

### Goal

Build a minimal, production-structured CRUD API using FastAPI that supports a single `Record` model with basic create and read operations. The system should establish clean architecture foundations (controller → service → repository), in-memory storage, and simple validation, preparing the codebase for future persistence and feature expansion.

### Changes Needed

- Add FastAPI application bootstrap (`app/main.py`)
- Add project folder structure:
  - `app/controllers/`
  - `app/services/`
  - `app/repositories/`
  - `app/models/`
  - `app/schemas/`
  - `app/core/` (config, settings)
- Add environment configuration using `.env` + Pydantic settings
- Define `Record` data model:
  - id (string/UUID)
  - model (string)
  - title (string)
  - json (dict | optional)
  - markdown (string | optional)
  - created (datetime)
  - updated (datetime)
- Implement in-memory storage (dictionary or list in repository layer)
- Add repository layer:
  - `create_record`
  - `get_record_by_id`
  - `list_records`
- Add service layer:
  - validation rules (required: model, title)
  - timestamp handling (created/updated)
  - business logic delegation to repository
- Add controller layer (FastAPI routers):
  - `POST /model`
  - `GET /model/{id}`
  - `GET /model`
- Add Pydantic schemas:
  - `RecordCreate`
  - `RecordResponse`
- Add basic error handling:
  - 404 for missing record
  - 400 for invalid input
- Add FastAPI app entrypoint with router registration
- Add minimal README:
  - setup instructions
  - env variables
  - how to run server
  - sample curl requests

### Acceptance Criteria

- [ ] FastAPI server starts successfully with `uvicorn`
- [ ] Project follows layered architecture (controller → service → repository)
- [ ] Record model is defined with required fields and timestamps
- [ ] POST `/model` creates a record and returns it with generated id
- [ ] GET `/model/{id}` returns a single record or 404 if not found
- [ ] GET `/model` returns list of all stored records
- [ ] Data is stored in-memory via repository abstraction
- [ ] Required field validation (model, title) is enforced
- [ ] Basic error handling returns correct HTTP status codes (400, 404)
- [ ] Environment configuration is loaded via `.env`
- [ ] README includes clear setup and usage instructions