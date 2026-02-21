# Itorbit Trading Hub

Welcome to the Itorbit Trading Hub! This README will provide you with complete setup instructions for running the trading platform, including backend Flask setup and frontend configuration.

## Prerequisites
Before you begin, ensure you have the following installed on your machine:
- Python 3.x
- Node.js
- npm (Node Package Manager)
- A PostgreSQL database (optional)

## Backend Setup (Flask)

### Step 1: Clone the Repository
Clone the Itorbit Trading Hub repository:
```bash
git clone https://github.com/alexmu613/itorbit-trading-hub.git
cd itorbit-trading-hub
```

### Step 2: Create a Virtual Environment
It's a good practice to use a virtual environment to manage your Python packages:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables
Create an `.env` file in the root directory of your project with the necessary environment variables. You can refer to the `.env.example` for guidance.

### Step 5: Run Database Migrations (if applicable)
If your project uses a database, run migrations to set up your database schema:
```bash
flask db upgrade
```

### Step 6: Run the Flask Server
Start the Flask development server:
```bash
flask run
```

The backend should now be running on [http://localhost:5000](http://localhost:5000).

## Frontend Configuration

### Step 1: Navigate to the Frontend Directory
If your frontend is in a separate directory, navigate to it:
```bash
cd frontend
```

### Step 2: Install Frontend Dependencies
Install the required Node packages:
```bash
npm install
```

### Step 3: Configure Environment Variables
Create a `.env` file for your frontend with the necessary API URLs and configurations.

### Step 4: Start the Frontend Server
Run the frontend development server:
```bash
npm start
```

The frontend will now be running on [http://localhost:3000](http://localhost:3000).

## Troubleshooting
- Ensure all dependencies are installed correctly.
- Check the console for any error messages during setup.
- If you face issues, refer to the documentation or open an issue on GitHub.

## Conclusion
You are now ready to use the Itorbit Trading Hub! For any further questions or contributions, feel free to reach out or submit a pull request.

Happy Trading!