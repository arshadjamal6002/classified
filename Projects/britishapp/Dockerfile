FROM python:3.11.5

# Set working directory
WORKDIR /app

# Copy the application code
COPY flask_app/ /app/

# Copy the model file
COPY tfidf.pkl /app/tfidf.pkl
COPY model.pkl /app/model.pkl

# Install system dependencies
RUN apt-get update && apt-get install -y gcc

# Install Python dependencies
COPY flask_app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install NLTK data
RUN python -m nltk.downloader stopwords wordnet punkt averaged_perceptron_tagger maxent_ne_chunker words

# Expose the application port
EXPOSE 5000

# Start the Flask application
CMD ["python", "app.py"]
