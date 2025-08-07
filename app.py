from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
      <head><title>Flask CI/CD App</title></head>
      <body style="font-family: Arial; text-align: center; padding-top: 50px;">
        <h1 style="color: green;">✅ Flask CI/CD Deployment Successful!</h1>
        <p>Welcome to your DevOps project deployed using Docker, GitHub Actions & GCP VM.</p>
        <p><b>Status:</b> Running Perfectly on Port 8080</p>
      </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
