from flask import Flask, request, jsonify
from flask_cors import CORS
from index import process_message, get_conversation, clear_conversation, list_conversations
import uuid

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "message": "Agent API is running"})

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({"error": "Missing 'message' in request body"}), 400
        
        user_message = data['message']
        conversation_id = data.get('conversation_id', str(uuid.uuid4()))

        result = process_message(user_message, conversation_id)

        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Server error: {str(e)}"
        }), 500

@app.route('/api/conversations/<conversation_id>', methods=['GET'])
def get_conversation_endpoint(conversation_id):
    """Get conversation history"""
    try:
        conversation = get_conversation(conversation_id)
        return jsonify({
            "success": True,
            "conversation": conversation,
            "conversation_id": conversation_id
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/conversations/<conversation_id>', methods=['DELETE'])
def clear_conversation_endpoint(conversation_id):
    """Clear conversation history"""
    try:
        clear_conversation(conversation_id)
        return jsonify({
            "success": True,
            "message": "Conversation cleared"
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/conversations', methods=['GET'])
def list_conversations_endpoint():
    """List all conversations"""
    try:
        conversations = list_conversations()
        return jsonify({
            "success": True,
            "conversations": conversations
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == '__main__':
    print("🚀 Starting Agent Chat API Server...")
    print("📍 API Base URL: http://localhost:5000/api")
    print("🏥 Health Check: http://localhost:5000/api/health")
    print("💬 Chat Endpoint: POST http://localhost:5000/api/chat")
    
    app.run(debug=True, host='0.0.0.0', port=5000) 