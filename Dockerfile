# 1. Start from a base image (a lightweight Linux with Python pre-installed)
FROM python:3.9-slim

# 2. Create a working directory inside the container
WORKDIR /app

# 3. Copy the requirements file into the container
COPY requirements.txt .

# 4. Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your code (main.py, model.pkl) into the container
COPY . .

# 6. Command to run the app when the container starts
# Note: We use host "0.0.0.0" so the container listens to the outside world
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]