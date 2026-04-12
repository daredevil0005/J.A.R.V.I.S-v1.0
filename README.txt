J.A.R.V.I.S v1.0

1. Requirements

Make sure you have installed:
Windows OS
Python 3.11 or higher
Node.js 20+
npm (comes with Node.js)
Git (optional)

2.Open Project Folder
Open PowerShell / Terminal inside:
e:\Github\J.A.R.V.I.S-v1.0

3. Setup Python Backend
Step 1: Create Virtual Environment:
py -m venv .venv

Step 2: Activate Virtual Environment:
.\.venv\Scripts\Activate.ps1

Step 4: Install Python Dependencies
python -m pip install -r requirements.txt

4. Run Python Agent
python agent.py console (For Testing)

5. Setup Frontend
Open new terminal and move to frontend folder:
cd agent-ui

Install frontend dependencies using npm:
npm install

6. Run Frontend
Start frontend server:
npm run dev

7. Open in Browser
http://localhost:3000

9. Important Notes
Run backend and frontend in separate terminals
Terminal 1 = Python backend
Terminal 2 = Frontend with npm
Configure LiveKit/external services if needed