# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- Deactivate a workshop.
- Activate a workshop.
- Protected workshop management routes.
- Internationalization.
- Workshop statistics.

## [0.15.0] - 2024-03-07

### Added

- Workshop speciality image.
- Api Key authentication via `X-Api-Key` header.

### Changed

- Some endpoints return 410 Gone when the resource is deleted.
- Deprecated 'client' field and added 'user' on review model.

### Fixed

- X-Page-Size header always returning 25.

### Removed

- Deprecated fields from MinimalWorkshop ("owner", "vehicles", "location", "recent_rating", "brands_count", "specialities_count", "vehicles_count", "vehicles_url", "brands_url" and "specialities_url").
- Deprecated field from Workshop ("owner").

## [0.14.0] - 2024-03-01

### Added

- Support for `application/json` content type.
- Vehicle service indicator (designates if the vehicle is in a service).

### Changed

- `GET /workshops/recommended` recommendations.
- Deprecated 'message' field on workshop review serializer in favor of 'body'.
- Removed support for trailing slash endpoints.

### Fixed

- Workshop specialities filter returning duplicated workshops.
- Review, Question and Service number generation.
- `DELETE /workshops/{workshop_id}/reviews/{review_number}` returning 500 error.
- `DELETE /vehicles/{vehicle_id}` returning 500 error.
- `PUT /auth/password/reset/confirm` returning 500 error.

## [0.13.1] - 2024-02-23

### Fixed

- `POST /workshops/{workshop_id}/brands` endpoint.

### Changed

- Renamed Rating headers from `X-#-Star-Rating`to `X-Rating-#-Star`.
- Workshop description is required.

## [0.13.0] - 2024-02-22

### Added

- Workshop description and banner.

## [0.12.0] - 2024-02-17

### Added

- Delete vehicles endpoint (soft-delete).
- Delete workshop reviews endpoint (soft-delete).
- Delete workshop questions endpoint (soft-delete).
- Caching (Cache-Control, ETag and Last Modified headers).
- Throttling (Rate Limiting).

### Changed

- Only major version number is used as the API version. e.g. `X-AutoMatico-API-Version: 0` instead of `X-AutoMatico-API-Version: v0.12`.
- 'workshop' field on service serializer is now the workshop id.

### Fixed

- `DELETE /workshops/{workshop_id}/questions/{question_id}` endpoint.
- `POST /workshops/{workshop_id}/reviews` endpoint.
- `PATCH /workshops/{workshop_id}/reviews/{review_id}` endpoint.
- `DELETE /workshops/{workshop_id}/reviews/{review_id}` endpoint.
- `GET /workshops/{workshop_id}/reviews/{review_id}/response` endpoint.

## [0.11.1] - 2024-02-07

### Added

- Garages of the month (based on reviews).
- New garages (last 30 days).
- Garages for you (based on your vehicles and location).
- Question and review retrieve, update and delete endpoints.
- 'image_url' field to user list serializer.
- 'url' field to question serializer.
- 'is_favorite' field to workshop serializer.
- Workshop rating metadata (average and stars count).

### Fixed

- 'url' field on review serializer.
- Workshop distance filter. Was retrieving workshops with no location.

### Changed

- Deprecated 'score' field on review serializer. Use 'rating' instead.

## [0.11.0] - 2024-02-05

### Added

- Favorite workshops.
- Archive vehicles. This allows to keep the vehicle data but not show it on the list of vehicles.
- User phone number in the admin panel and signup endpoint.

### Changed

- Workshop reviews only accept 1 response. This response is made by the workshop owner. The response cannot be edited or deleted.

### Fixed

- Crash when trying to upload a review image.
- Error when trying to add a speciality to a workshop if name was exactly the same as one registered.

### Removed

- 'responsable' field from service history request.

## [0.10.1] - 2024-02-03

### Changed

- Vehicle plate validation regex.

### Fixed

- Crash when trying to update a user through the admin panel.

## [0.10.0] - 2024-02-03

### Added

- 'answer' field to question response.
- Workshop location (GeoJSON).
- Filter workshops by distance.
- 'vehicle' and 'workshop' fields to private service serializer.
- Vehicles are editable.
- 'archived' field to vehicle serializer.

### Changed

- Plate validation regex.

### Fixed

- Question responses endpoints.
- Missing 'current_state' field on service serializer.
- Crash when trying to add a speciality to a workshop.

## [0.9.3] - 2024-02-02

### Fixed

- DB error when trying to search for iexact service number.

## [0.9.2] - 2024-02-02

### Added

- VIN and Plate regex validation.

## [0.9.1] - 2024-02-02

### Fixed

- Vehicle serializer crashing because of non existing route.
- Only `GET` requests were checking if the resource (on path) exists.

## [0.9.0] - 2024-01-26

### Changed

- Everything.

### Removed

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
