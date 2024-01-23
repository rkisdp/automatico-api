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

## [0.8.1] - 2024-01-22

### Added

- "url" field to `/vehicles/*` endpoints.
- "url" field to `/services/*` endpoints.
- "url" field to `/users/*` endpoints.
- "url" field to `/workshops/*` endpoints.

### Fixed

- `/vehicles/*`, `/user/*`, `/users/*` and `/workshops/*`  now return "photo" value with it's absolute URL.

### Changed

- Workshops related fields "resource" field renamed to "name".
- Workshops related fields "link" field renamed to "url".
- Renamed workshops/id/vehicles/ vehicle_id field to id.

## [0.8.0] - 2024-01-21

### Added

- Changelog
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