# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- Fix `DELETE /vehicles/{id}/` with related services returns 500.
- Add workshop to favorite.
- Fix responsable not added when accepting a service.
- Change Q/A and reviews endpoints.
- Add service request (model, endpoints). This allows to have a chat on a request, not just two messages and more details about the request itself.
- Change "response" to "message" (QuestionResponse model).
- Deactivate a workshop.
- Activate a workshop.
- Removed "Paginated*" object schemas.
- Authorization with 3rd party (Google and Facebook).
- Enable `POST /image` to upload an image and return it's ID.
- Protect workshop management routes. This routes should need a workshop_id claim.

## [0.9.1] - 2024-02-02

## Fixed

- Vehicle serializer crashing because of non existing route.
- Only `GET` requests were checking if the resource (on path) exists.

## [0.9.0] - 2024-01-26

## Changed

- Everything.

## Removed

- A lot.

## [0.8.1] - 2024-01-22

### Added

- "url" field to `/vehicles/*` endpoints.
- "url" field to `/services/*` endpoints.
- "url" field to `/users/*` endpoints.
- "url" field to `/workshops/*` endpoints.
- Decapricating `/workshops/questions/?.*` and `/workshops/reviews/?.*` endpoints.

### Fixed

- `/vehicles/*`, `/user/*`, `/users/*` and `/workshops/*`  now return "photo" value with it's absolute URL.

### Changed

- Workshops related fields "resource" field renamed to "name".
- Workshops related fields "link" field renamed to "url".
- Renamed workshops/id/vehicles/ vehicle_id field to id.
- Endpoints trailing slash is now optional.
- Improved workshops documentation.

## [0.8.0] - 2024-01-21

### Added

- Changelog.
- Workshop's service rating.
- Workshop's service comments.
- Workshop's service images.
- Service filtering by current state.
- Deactivate user.
- Workshops Q/A endpoints.
- API versioning.
- Custom media type (application/vnd.automatico+json).
- Some response headers on schema.

### Changed

- Related fields "resource" field renamed to "name".
- Related fields "link" field renamed to "url".
- Images URLs now include absolute address.
- User vehicle's "brand" now returns as an object.
- Workshop service's "requested_by" and "vehicle" now return as objects.
- Workshop "brands", "employees" and "vechicles" now return as objects.

### Removed

- "is_active", "is_staff" and "date_joined" fields from `GET /user/`.
