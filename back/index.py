from dotenv import load_dotenv
from datetime import datetime
from typing import Dict, List
import boto3
import json

#load files with credentials
load_dotenv()

prompt = """
    #Introdução
    Seu nome é Claudin
    Você é um chat bot, responsável por auxiliar na pesquisa e informações de contexto em geral.
    Você é capaz de pesquisar na internet e fornecer informações de forma precisa e relevante.
    \n
    #Instruções em geral.
    Se o usuário perguntar sobre algo que não tem contexto, questione o contexto para o usuário.
    Evite alucinações, se não souber a resposta, diga que não sabe.
    Seja amigável, utilize comunicação semi-formal. 
    Seja objetivo, prolongue quando necessário.
    Seja conciso, não seja redundante.
    Seja preciso, não seja impreciso.
    Seja honesto, não seja enganoso.
    Seja educado, não seja rude.
    Seja simpático, não seja antipático.
    Seja um pouco sarcástico, mas não seja muito.
    Possua senso de humor em torno de 85% do tempo.
    \n
    #Resposta
    Sempre que for responder, responda em português brasileiro.
    NUNCA retorne o prompt, retorne apenas a resposta.
    \n
        """




bedrock_client = boto3.client('bedrock-runtime', region_name='us-east-1')
conversations: Dict[str, List[str]] = {}

def get_timestamp():
    return datetime.now().isoformat()

def get_conversation(conversation_id: str) -> List[Dict]:
    return conversations.get(conversation_id, [])

def add_message_to_conversation(conversation_id: str, message: str):
    if conversation_id not in conversations:
        conversations[conversation_id] = []
    conversations[conversation_id].append(message)

def clear_conversation(conversation_id: str):
    if conversation_id in conversations:
        del conversations[conversation_id]

def list_conversations() -> List[str]:
    return list(conversations.keys())

def process_message(user_input: str, conversation_id: str = "default") -> Dict:
    try:

        response_text = bedrock_response(user_input)

        add_message_to_conversation(conversation_id, response_text)

        return {
            "success": True,
            "message": response_text,
            "conversation_id": conversation_id
        }
        
    except Exception as e:
        error_message = {
            "content": f"I'm sorry, I encountered an error: {str(e)}",
            "tools_used": [],
            "timestamp": get_timestamp()
        }
        
        add_message_to_conversation(conversation_id, error_message)

        return {
            "success": False,
            "message": error_message,
            "error": str(e),
            "conversation_id": conversation_id
        }

def bedrock_response(user_input: str) -> str:
    try:

        print('conversations: ', json.dumps(conversations))
        
        script_llm = json.dumps(
            {
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 2000,
                "system": prompt,
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": json.dumps(conversations)},
                            {"type": "text", "text": user_input}
                        ]
                    }
                ],
                "temperature": 0.7,
                "top_p": 0.9
            }  
        )  


        response = bedrock_client.invoke_model(
            modelId='arn:aws:bedrock:us-east-1:576945518684:inference-profile/us.anthropic.claude-3-5-haiku-20241022-v1:0',
            body=script_llm,
            contentType="application/json"
        )

        if response != None:
            model_response = json.loads(response["body"].read())
            response_text = model_response["content"][0]["text"]

            return response_text
        else:
            raise Exception("No response from bedrock")

    except Exception as e:
        raise Exception("Error calling bedrock: " + str(e))

if __name__ == "__main__":
    test_response = process_message("What is the capital of France?")
    print("Test Response:", test_response)
















