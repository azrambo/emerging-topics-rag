import requests

def main():
    base_url = "http://localhost:8000"  # Adjust if needed

    # Upload sample texts
    texts = [
        "La capital de Francia es París.",
        "Miguel de Cervantes Saavedra escribió Don Quijote.",
        "El lenguaje de programación Python fue creado por Guido van Rossum."
    ]
    upload_payload = {"texts": texts}
    print("Uploading documents...\n")
    resp_upload = requests.post(f"{base_url}/upload", json=upload_payload)
    print("Status code /upload:", resp_upload.status_code)
    print("Response /upload:", resp_upload.json())

    # Example questions
    questions = [
        "¿Cuál es la capital de Francia?",
        "¿Quién creó el lenguaje de programación Python?",
        "¿Quién escribió Don Quijote?"
    ]

    for q in questions:
        print(f"\nQuestion: {q}")
        generate_payload = {"new_message": {"role": "user", "content": q}}
        resp_generate = requests.post(f"{base_url}/generate", json=generate_payload)
        print("Status code /generate:", resp_generate.status_code)
        if resp_generate.ok:
            data = resp_generate.json()
            print("Generated response:", data.get("generated_text"))
        else:
            print("Error:", resp_generate.text)

if __name__ == "__main__":
    main()