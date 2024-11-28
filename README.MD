# FAKEBBS

[中文文档](README_CN.md)

This project is a web application built with FastAPI, featuring a user interface powered by Amis and containerized using Docker.

## Features

- FastAPI backend with automatic API documentation
- Amis-powered frontend for rapid UI development
- Docker containerization for easy deployment
- GitHub Actions for CI/CD
- Nacos service registration for microservices architecture
- Dynamic function rendering system
- Built-in tools collection for common operations
- Multi-language support

## Project Structure

The main components of the project are:

- `main.py`: The entry point of the FastAPI application
- `webUI/`: Contains the frontend-related files
- `api/`: Contains API route definitions and view tools
- `config/`: Configuration files, including Swagger and Nacos setup
- `Dockerfile`: Defines the Docker image for the application
- `.github/workflows/deploy.yml`: GitHub Actions workflow for deployment

## Setup and Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   uvicorn main:app --reload
   ```


## Dynamic Function Rendering System

One of the key features of this application is its ability to automatically generate UI pages from Python function declarations. This system allows developers to quickly create interactive web interfaces without writing frontend code.

### How it works

1. The system automatically detects Python functions in view files
2. Function parameters are converted into form inputs
3. A complete AMIS-powered UI is generated with appropriate form controls
4. The function's return value is displayed in the output field

### Example Usage

Create a view file with a simple function:
```python
python
view_sort = 10
view_desc = "Addition Function"
def f(first_number, second_number):
return int(first_number) + int(second_number)
```

The system will automatically generate:
- A form with input fields for each parameter
- A submit button
- An output field for the result
- Proper API endpoints for function execution

The dynamic function rendering system is one of the most powerful features of this application, as it dramatically reduces the amount of boilerplate code needed to create new interactive web pages. It follows a "convention over configuration" approach, where developers only need to define their business logic as Python functions, and the framework handles all the UI generation and API routing automatically.

### Key Features

- Automatic parameter type detection
- Support for multiple input parameters
- Real-time function execution
- Clean and consistent UI generation
- Integration with AMIS form system

## Docker Deployment

To build and run the Docker container:

1. Build the Docker image:
   ```bash
   docker build -t your-fastapi-app .
   ```
2. Run the container:
   ```bash
   docker run -d -p 8000:80 your-fastapi-app
   ```

## Auto-reload Development Mode

The project includes a reload script for development:
```bash
./reload.sh
```
This script automatically monitors for changes and restarts the application when updates are detected.

---

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

Copyright (C) 2023 [ZAKL]

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```
