import time

import google.generativeai as genai
import os

api = os.getenv("API_GEMINI")

genai.configure(api_key=api)
model = genai.GenerativeModel("gemini-1.5-flash")

desconhecidos = list()
conhecidos = list()

with open("cpus_filtro3.csv", "r") as arquivo:
    for x in arquivo:
        if x.split(",")[4] == "Unknown":
            desconhecidos.append(x)
        else:
            conhecidos.append(x)

    with open("socket_conhecido.csv", "w") as arquivo_conhecidos:
        arquivo_conhecidos.writelines(conhecidos)

    with open("socket_atualizado.csv", "w") as arquivo_desconhecidos:
        for x in desconhecidos:
            partes = x.split(",")
            prompt = f"qual é o socket do processador {partes[0]}? Responda apenas o nome e mais nada"
            response = model.generate_content(prompt)
            partes[4] = response.text[0:-1]
            partes = ",".join(partes)
            arquivo_desconhecidos.write(partes)
            time.sleep(4)
