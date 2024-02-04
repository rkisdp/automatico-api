# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- Fix `DELETE /vehicles/{id}/` with related services returns 500.
- Add workshop to favorite.
- Fix responsable not added when accepting a service.
- Add service request (model, endpoints). This allows to have a chat on a request, not just two messages and more details about the request itself.
- Deactivate a workshop.
- Activate a workshop.
- Removed "Paginated*" object schemas.
- Authorization with 3rd party (Google and Facebook).
- Enable `POST /image` to upload an image and return it's ID.
- Protect workshop management routes. This routes should need a workshop_id claim.
- Translate all error messages.
- Archive vehicles.

## [0.10.0] - 2024-02-03

## Added

- 'answer' field to question response.
- Workshop location (GeoJSON).
- Filter workshops by distance.
- 'vehicle' and 'workshop' fields to private service serializer.
- Vehicles are editable.
- 'archived' field to vehicle serializer.

## Changed

- Plate validation regex.

## Fixed

- Question responses endpoints.
- Missing 'current_state' field on service serializer.
- Crash when trying to add a speciality to a workshop.

## [0.9.3] - 2024-02-02

## Fixed

- DB error when trying to search for iexact service number.

## [0.9.2] - 2024-02-02

## Added

- VIN and Plate regex validation.

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
