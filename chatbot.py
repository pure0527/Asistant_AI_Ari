from openai import OpenAI

def preguntar_ia(pregunta, api_key):
       
    client = OpenAI(base_url="https://openrouter.ai/api/v1",
                    api_key=api_key)
    
    try:
        respuesta = client.chat.completions.create(
            model="qwen/qwen-vl-plus:free",
            messages=[
                {"role": "user",
                "content": [{
                    "type": "text",
                    "text": pregunta}]
                }]
        )
        print(f"\n\nRespuesta de IA: {respuesta.choices[0].message.content}")
    except Exception as e:
        print(f"Error en la consulta: {e}")

    # try:
    #     respuesta = client.chat.completions.create(
    #         model="deepseek/deepseek-r1-distill-llama-8b",
    #         messages=[
    #             {"role": "user",
    #             "content": pregunta}]
    #     )
    #     print(f"\n\nRespuesta de IA: {respuesta.choices[0].message.content}")
    # except Exception as e:
    #     print(f"Error en la consulta: {e}")