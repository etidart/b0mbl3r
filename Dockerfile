FROM python

# Set app workdir
WORKDIR /usr/src/app

# Expose port
EXPOSE 80

# Copy dependencies list
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app sources
COPY . .

# Run app
CMD ["python", "main.py"]
