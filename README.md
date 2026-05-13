# Offline KYC Verification Service

## Overview
Offline KYC Verification Service is a backend microservice API designed to validate a user's Aadhaar ID by decoding and verifying the QR code present on it. This service is a part of a larger project called [TMS_SERVER](https://github.com/NallyTHEdude/TMS_SERVER).

This project is built with a focus on simplicity, scalability, and ease of use, making it suitable for developers of all experience levels.

---

## Features
- **QR Code Decoding**: Extracts and validates data from Aadhaar QR codes.
- **API-Driven**: Provides RESTful endpoints for seamless integration.
- **Error Handling**: Comprehensive error responses for invalid or malformed requests.
- **Modular Design**: Easy to extend and maintain.

---

## Prerequisites
To run this project, ensure you have the following installed:

- **Python 3.11+**
- **uv** (Python package manager)
- **Virtual Environment** (Recommended for dependency isolation)

---

## Installation
Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/offline-kyc-service.git
   cd offline-kyc-service
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   uv sync
   ```

4. **Run the Application**:
   ```bash
   python main.py
   ```

---

## Usage
The service exposes the following API endpoints:

### Health Check
- **Endpoint**: `/health`
- **Method**: GET
- **Description**: Verifies if the service is running.
- **Response**:
  ```json
  {
    "success": true,
    "status_code"=200,
    "message"="Service is healthy"
  }
  ```

### Upload Aadhaar File
- **Endpoint**: `/upload`
- **Method**: POST
- **Description**: Accepts an Aadhaar png or jpg files for offline verification.
- **Request Body**:
  ```json
  {
    "file": "<base64-encoded-file>"
  }
  ```
- **Response**:
  ```json
  {
    "success": "True",
    "status_code": "success",
    "data": {
      "name_match": bool,
      "dob_match": bool,
      "gender_match": bool
    }
  }
  ```

---

## Folder Structure
```
offline-kyc-service/
├── main.py                # Entry point of the application
├── pyproject.toml         # Project configuration
├── README.md              # Project documentation
├── _temp/                 # Temporary files
├── logs/                  # Log files
├── src/                   # Source code
│   ├── app.py             # Application setup
│   ├── config/            # Configuration files
│   │   ├── env.py         # Environment variables
│   │   ├── logger.py      # Logging setup
│   │   ├── paths.py       # Path configurations
│   ├── core/              # Core business logic
│   │   ├── upload_file_service.py
│   ├── routes/            # API routes
│   │   ├── healthCheck.py # Health check endpoint
│   │   ├── upload_file.py # File upload endpoint
│   ├── schemas/           # Data schemas
│       ├── AdhaarData.py  # Aadhaar data schema
│       ├── ApiError.py    # API error schema
│       ├── ApiResponse.py # API response schema
```

---

## Contributing
Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push the branch.
4. Open a pull request.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments
- [TMS_SERVER](https://github.com/NallyTHEdude/TMS_SERVER) for being the parent project.
- The open-source community for providing the tools and libraries used in this project.

---

Thank you for using Offline KYC Verification Service! If you have any questions or issues, feel free to open an issue in the repository.