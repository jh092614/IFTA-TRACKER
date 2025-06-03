from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'IFTA MILE TRACKER - Web App'

# ✅ Required for Render: bind to 0.0.0.0 and use PORT env variable
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
