# Use an official Python runtime as a parent image
FROM python:3.8.10

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the project files into the working directory
COPY pyproject.toml poetry.lock* ./

# Install poetry
RUN pip install --no-cache-dir poetry

# Configure poetry: Do not create a virtual environment inside the container
# as the container itself provides isolation
RUN poetry config virtualenvs.create false

# Install only dependencies specified in pyproject.toml using poetry
# This is efficient because it helps to cache the dependencies layer
RUN poetry install --no-dev --no-interaction --no-ansi

# Copy the rest of your application's code
COPY . /app

# Command to run the application
# You can change `app.main:app` to your FastAPI app's module and variable name
CMD ["uvicorn", "application.main:app", "--reload","--host", "0.0.0.0", "--port", "80","--log-level", "debug","--use-colors"]
