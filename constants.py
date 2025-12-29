import os
from dotenv import load_dotenv

# Load .env file if it exists (for local testing)
load_dotenv()

# Credentials from environment variables (for GitHub Actions)
USERNAME = os.environ.get('NAUKRI_USERNAME', 'your_naukri_username')
PASSWORD = os.environ.get('NAUKRI_PASSWORD', 'your_naukri_password')
MOBILE = os.environ.get('NAUKRI_MOBILE', 'your_naukri_phone')

# Resume paths
ORIGINAL_RESUME_PATH = "resume/Resume.pdf"
MODIFIED_RESUME_PATH = "resume/Resume_modified.pdf"

# URLs
NAUKRI_LOGIN_URL = "https://www.naukri.com/nlogin/login"
NAUKRI_PROFILE_URL = "https://www.naukri.com/mnjuser/profile"