from app import create_app

app = create_app()

#URL http://127.0.0.1:5000 o http://192.168.0.111:5000
# Permite iniciar la app con: python run.py
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)