# 🤖 AI Research Assistant Chat Interface

A modern, interactive chat interface for your LangChain-powered AI research assistant using React frontend and Flask backend.

![AI Chat Interface](https://img.shields.io/badge/AI-Chat%20Interface-blue) ![React](https://img.shields.io/badge/React-18.2.0-61dafb) ![Flask](https://img.shields.io/badge/Flask-Latest-green) ![LangChain](https://img.shields.io/badge/LangChain-Latest-yellow)

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Environment Variables](#environment-variables)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

## 🎯 Overview

This project provides a clean, modern web interface to interact with your AI research assistant powered by:
- **Backend**: Flask API with LangChain and Anthropic Claude
- **Frontend**: React.js with modern UI components
- **AI Model**: Claude-3.5-Sonnet for intelligent responses

## ✨ Features

- 💬 **Real-time Chat Interface** - Clean, responsive chat UI
- 🧠 **AI-Powered Responses** - Powered by Anthropic Claude
- 💾 **Conversation History** - Persistent chat sessions
- 🎨 **Modern UI/UX** - Professional design with animations
- 📱 **Mobile Responsive** - Works on all device sizes
- ⚡ **Fast Performance** - Optimized for speed
- 🔄 **Error Handling** - Graceful error management
- 🎯 **Typing Indicators** - Real-time feedback

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+** - [Download Python](https://python.org/downloads/)
- **Node.js 16+** - [Download Node.js](https://nodejs.org/)
- **npm or yarn** - Comes with Node.js
- **Git** - [Download Git](https://git-scm.com/)

## 📁 Project Structure

```
IA/
├── agent-01/                 # Backend directory
│   ├── Models/
│   │   └── message.py        # Pydantic message model
│   ├── index.py              # Main agent logic
│   ├── app.py                # Flask API server
│   ├── requirements.txt      # Python dependencies
│   └── .env                  # Environment variables
├── frontend/                 # React frontend
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── ...
└── README.md                # This file
```

This comprehensive README provides:

1. **Clear overview** and features
2. **Step-by-step setup** instructions  
3. **Multiple running options** (manual vs scripts)
4. **Troubleshooting guide** for common issues
5. **API documentation** 
6. **Environment setup** details
7. **Professional formatting** with emojis and badges

The README will help anyone (including beginners) successfully set up and run your AI chat interface! 🚀

## 🚀 Setup Instructions

### Step 1: Clone the Repository
```bash
git clone <your-repository-url>
cd IA
```

### Step 2: Set Up Environment Variables

1. **Create `.env` file in the `agent-01` directory:**
```bash
cd agent-01
touch .env
```

2. **Add your Anthropic API key to `.env`:**
```env
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

> 💡 **Get your API key from:** [Anthropic Console](https://console.anthropic.com/)

### Step 3: Backend Setup

1. **Navigate to the backend directory:**
```bash
cd agent-01
```

2. **Create a virtual environment (recommended):**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

### Step 4: Frontend Setup

1. **Navigate to the frontend directory:**
```bash
cd ../front
```

2. **Create React app (if not already created):**
```bash
npx create-react-app . --template minimal
```

3. **Install additional dependencies:**
```bash
npm install axios lucide-react
```

## 🌐 Access Your Application

Once both services are running:

- **Frontend (Chat Interface):** http://localhost:3000
- **Backend API:** http://localhost:5000/api
- **Health Check:** http://localhost:5000/api/health

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/health` | Health check |
| `POST` | `/api/chat` | Send message to AI |
| `GET` | `/api/conversations/<id>` | Get conversation history |
| `DELETE` | `/api/conversations/<id>` | Clear conversation |
| `GET` | `/api/conversations` | List all conversations |

### Example API Usage:

```bash
# Health check
curl http://localhost:5000/api/health

# Send a message
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello!", "conversation_id": "test123"}'
```

## 🔧 Environment Variables

Create `.env` file in `agent-01/` directory:

```env
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

## 🐛 Troubleshooting

### Common Issues:

#### 1. **"Module not found" errors**
```bash
# Backend
cd agent-01
pip install -r requirements.txt

# Frontend
cd frontend
npm install
```

#### 2. **CORS errors**
- Ensure Flask-CORS is installed
- Check that the frontend is making requests to `http://localhost:5000/api`

#### 3. **API key errors**
- Verify your `.env` file contains the correct Anthropic API key
- Check that the `.env` file is in the `agent-01` directory

#### 4. **Port conflicts**
```bash
# Check if ports are in use
netstat -ano | findstr :3000  # Windows
lsof -i :3000                 # macOS/Linux

# Kill processes if needed
taskkill /PID <PID> /F        # Windows
kill -9 <PID>                 # macOS/Linux
```

#### 5. **Virtual environment issues**
```bash
# Recreate virtual environment
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Debug Mode:

Enable debug logging by setting:
```python
# In app.py
app.run(debug=True, host='0.0.0.0', port=5000)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LangChain](https://langchain.com/) for the AI framework
- [Anthropic](https://anthropic.com/) for Claude AI model
- [React](https://reactjs.org/) for the frontend framework
- [Flask](https://flask.palletsprojects.com/) for the backend API

---

**🎉 Enjoy chatting with your AI Research Assistant!**


For support or questions, please open an issue in the repository.
