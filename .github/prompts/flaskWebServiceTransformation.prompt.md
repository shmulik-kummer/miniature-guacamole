---
description: Transform a basic Python script with calculate_area function into a Flask web service with REST API endpoint for area calculations
---

# Plan: Flask Web Service Transformation (Area Calculator)

Transform the basic Python script into a robust Flask web service with a REST API endpoint for area calculations, including proper dependency management, strict input validation, and clear JSON response handling.

## Project Overview

**Current State:**
- Basic Python script (`app.py`) with `calculate_area(length, width)` function
- Empty `requirements.txt` file
- No web service functionality

**Target State:**
- Flask web service with REST API
- GET `/area` endpoint accepting `length` and `width` query parameters
- Strict input validation for numeric and positive values
- JSON response format for both success and errors
- Proper dependency management

## Implementation Steps

### 1. Update Dependencies
- Add the `Flask` library to the `requirements.txt` file.

### 2. Transform app.py Structure
- Import necessary components: `Flask`, `request`, and `jsonify`.
- Initialize the Flask application instance.
- **Keep** the existing `calculate_area(length, width)` function definition as the core logic.

### 3. Implement /area Endpoint and Validation
- Create the GET route at `/area`.
- **Extract** `length` and `width` from query parameters (`request.args`).
- **Convert** the parameters to a numeric type (float/integer) for calculation.
- **Perform Strict Input Validation (Critical):**
    - **Check 1 (Missing):** If either `length` or `width` is missing, return a `400 Bad Request` error.
    - **Check 2 (Invalid Type/Value):** If parameters are non-numeric or are negative/zero, return a `400 Bad Request` error.
- Call the existing `calculate_area` function with the validated numeric parameters.

### 4. Return API Response
- If the calculation is successful, return the result using `jsonify` in the specified **Success Response** format (Step 5).
- If validation fails, return the error message in the specified **Error Response** format (Step 5) with the appropriate `400 Bad Request` status.

### 5. Configure Flask App Runner
- Replace the simple print statement with the standard `if __name__ == '__main__':` block.
- Execute the Flask application using `app.run()`.
- **Configuration:** Set `host='0.0.0.0'` and `debug=True` for development purposes.

## Technical Requirements

### API Specification
GET /area?length={number}&width={number}

Success Response (HTTP 200 OK): { "length": number, "width": number, "area": number }

Error Response (HTTP 400 Bad Request): { "error": "Specific error message related to the failed validation." }


### Dependencies
- Flask (web framework)

### File Changes
- `requirements.txt`: Add Flask dependency.
- `app.py`: Complete transformation from script to web service, including imports, app instance, endpoint, validation, and runner.

## Success Criteria
- Flask web service starts successfully on `http://0.0.0.0:5000`.
- GET `/area?length=5&width=10` responds with `HTTP 200 OK` and the correct JSON area.
- GET `/area` without parameters responds with `HTTP 400 Bad Request` and a specific error message.
- GET `/area?length=-5&width=10` responds with `HTTP 400 Bad Request` and a specific error message.
- The code maintains the existing `calculate_area` function logic.