# Portfolio API Documentation

This API allows for the management of portfolios for people worldwide. 

## Endpoints

### `GET /api/v1/portfolios/`

Retrieves a list of all portfolios.

#### Parameters
None

#### Response

- Status: `200 OK`
- Body: JSON array of portfolios

---

### `POST /api/v1/portfolios/`

Creates a new portfolio.

#### Parameters

- `name` (string, required): The name of the portfolio.
- `link` (string, required): The link to the portfolio.
- `socials` (array of objects, optional): An array of Socials objects associated with the portfolio. Each object should be formatted as: `{ "name": <string>, "link": <string> }`.
- `tags` (array of objects, optional): An array of Tags objects associated with the portfolio. Each object should be formatted as: `{ "name": <string> }`.
- `is_approved` (boolean, optional): Whether the portfolio is approved or not. Defaults to `true`.
- `country` (object, required): The country object where the portfolio is located. The object should be formatted as: `{ "name": <string> }`.

#### Response

- Status: `201 CREATED` if successful, `400 BAD REQUEST` if any errors.
- Body: `{"status": "success", "key": "<modification_key>"}`

---


### `PUT /api/v1/portfolios/<portfolio_id>/`

Updates a specific portfolio. Requires a modification key.

#### Parameters

- `modification_key` (string, required): The modification key for the portfolio.
- Other fields are the same as in the `POST /api/v1/portfolios/` request but are optional.

#### Response

- Status: `200 OK` if successful, `400 BAD REQUEST` if the modification key is wrong.
- Body: `{"status": "success"}`

---

### `PATCH /api/v1/portfolios/<portfolio_id>/`

Partially updates a specific portfolio. Requires a modification key.

#### Parameters

- `modification_key` (string, required): The modification key for the portfolio.
- Other fields are the same as in the `POST /api/v1/portfolios/` request but are optional.

#### Response

- Status: `200 OK` if successful, `400 BAD REQUEST` if the modification key is wrong.
- Body: `{"status": "success"}`

---

### `DELETE /api/v1/portfolios/<portfolio_id>/`

Deletes a specific portfolio.

#### Parameters
None

#### Response

- Status: `204 NO CONTENT`

---

## Models

### `Portfolio`

- `id` (integer, read-only): The ID of the portfolio.
- `name` (string): The name of the portfolio.
- `link` (string): The link to the portfolio.
- `socials` (array of Socials): The associated social media accounts.
- `tags` (array of Tags): The associated tags.
- `created_at` (datetime, read-only): When the portfolio was created.
- `is_approved` (boolean): Whether the portfolio is approved or not.
- `country` (Country): The country where the portfolio is located.
- `modification_key` (string, read-only): The key for modifying the portfolio.

### `Socials`

- `id` (integer, read-only): The ID of the social media account.
- `name` (string): The name of the social media platform.
- `link` (string): The link to the social media account.

### `Tags`

- `id` (integer, read-only): The ID of the tag.
- `name` (string): The name of the tag.

### `Country`

- `id` (integer, read-only): The ID of the country.
- `name` (string): The name of the country.

---
