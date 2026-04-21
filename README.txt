# 🤖 J.A.R.V.I.S v1.0

### (Just A Rather Very Intelligent System)

J.A.R.V.I.S is a **real-time AI voice assistant** that combines **Conversational AI + System Automation** using Python and LiveKit.
It allows users to interact using voice commands and perform tasks like searching, opening applications, controlling system settings, and storing memory.

---

## 🚀 Features

* 🎤 Real-time voice interaction
* 🧠 AI-powered responses (Google Realtime Model)
* ⚙️ System automation (open apps, control WiFi, brightness, etc.)
* 🌐 Google search (opens browser + voice summary)
* 🖼️ Image search support
* 🧾 Memory storage & recall
* 🔊 Voice response output
* 🌍 LiveKit-based frontend UI

---

## 🏗️ System Architecture

```
User → LiveKit UI → Assistant Core → AI Model → Tool Modules → Operating System
```

---

## 🛠️ Technologies Used

* Python
* LiveKit (Realtime Communication)
* Google Realtime AI
* Node.js (Frontend)
* WebRTC
* JavaScript (UI)

---

## 📋 Prerequisites

Make sure you have installed:

* 🪟 Windows OS
* 🐍 Python 3.11 or higher
* 🟢 Node.js 20+
* 📦 npm (comes with Node.js)
* 🔧 Git (optional)

---

## 📂 Project Setup

### 1️⃣ Clone or Open Project

```bash
cd e:\Github\J.A.R.V.I.S-v1.0
```

---

## ⚙️ Backend Setup (Python)

### Step 1: Create Virtual Environment

```bash
py -m venv .venv
```

### Step 2: Activate Virtual Environment

```bash
.\.venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

## 🔐 Environment Variables Setup

Create a `.env` file in root folder and add:

```
GOOGLE_API_KEY=your_api_key
GOOGLE_SEARCH_API_KEY=your_search_key
SEARCH_ENGINE_ID=your_engine_id
LIVEKIT_URL=your_livekit_url
LIVEKIT_API_KEY=your_livekit_key
LIVEKIT_API_SECRET=your_livekit_secret
```

👉 This keeps sensitive data secure.

---

## ▶️ Run Backend (Jarvis Agent)

```bash
python agent.py console
```

✔ Starts AI assistant
✔ Handles voice + commands
✔ Connects to LiveKit

---

## 🌐 Frontend Setup (LiveKit UI)

Open new terminal:

### Step 1: Navigate to UI folder

```bash
cd agent-ui
```

### Step 2: Install dependencies

```bash
npm install
```

---

## ▶️ Run Frontend

```bash
npm run dev
```

---

## 🌍 Open Application

Open in browser:

```
http://localhost:3000
```

---

## ⚠️ Important Notes

* Run backend and frontend in **separate terminals**

  👉 Terminal 1 → Python Backend
  👉 Terminal 2 → Frontend

* Ensure `.env` file is properly configured

* Internet connection is required

* Microphone permission must be enabled

---

## 🧠 How It Works

1. User gives voice command
2. LiveKit captures and sends audio
3. Assistant processes input using AI
4. If query → AI responds
5. If command → Tool executes action
6. OS performs action
7. Jarvis gives voice response

---

## ⚙️ Feature Workflow Example

### Example: “Open Chrome”

* Input → Voice command
* Processing → Assistant detects intent
* Execution → Calls tool function
* Output → Chrome opens + voice confirmation

---

## 🧾 Memory System

Jarvis can remember user information.

### Example:

* “Remember my name is Pratik”
* “What is my name?”

✔ Stored in memory module
✔ Retrieved when needed

---

## 🔍 Google Search Feature

* Searches using API
* Opens browser automatically
* Gives voice summary

---

## 🖼️ Image Search

* Opens Google Images
* Displays visual results

---

## 🧩 Project Structure

```
J.A.R.V.I.S/
│
├── agent.py           # Main assistant logic
├── features/          # Tool modules (functions)
├── memory/            # Memory storage system
├── agent-ui/          # Frontend (LiveKit UI)
├── requirements.txt   # Python dependencies
└── .env               # Environment variables
```

---

## 🔐 Security

* API keys stored in `.env`
* Only predefined commands allowed
* No direct OS access without tools

---

## 🧪 Testing

Tested for:

* Voice input/output
* AI response generation
* System commands
* Memory storage
* Performance

---

## 🚀 Future Scope

* Mobile application
* Cloud deployment
* Multi-user support
* Smart home integration
* Advanced NLP improvements

---

## 👨‍💻 Author

**Pratik S. Dabhane**

---

## 🎯 Conclusion

J.A.R.V.I.S successfully integrates **AI + Automation + Real-time communication** to create an intelligent voice assistant system. It demonstrates practical implementation of modern AI technologies in real-world applications.

---

## ⭐ Final Note

> This project showcases how AI can be used to create interactive and intelligent systems that enhance user experience through voice-based automation.
