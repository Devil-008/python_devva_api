import os
from dotenv import load_dotenv
from app import create_app

# Load environment variables from .env file if present
load_dotenv()

env_name = os.environ.get("FLASK_ENV", "development")
app = create_app(env_name)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7000))
    app.run(host="0.0.0.0", port=port, debug=(env_name == "development"))
