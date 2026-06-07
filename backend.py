from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

# Hedef sunucu
TARGET = "http://104.249.8.46"
SECRET_KEY = "X9kLmN3pQrT7vY2wZ5"

def check_key():
    key = request.args.get('key')
    if not key or key != SECRET_KEY:
        return False
    return True

@app.route('/api/101m', methods=['GET'])
def api_101m():
    if not check_key():
        return jsonify({"error": "Geçersiz anahtar"}), 403
    try:
        params = {k: v for k, v in request.args.items() if k != 'key'}
        r = requests.get(f"{TARGET}/101m.php", params=params, timeout=10)
        return r.text, r.status_code, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/tapu', methods=['GET'])
def api_tapu():
    if not check_key():
        return jsonify({"error": "Geçersiz anahtar"}), 403
    try:
        params = {k: v for k, v in request.args.items() if k != 'key'}
        r = requests.get(f"{TARGET}/tapu.php", params=params, timeout=10)
        return r.text, r.status_code, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/tapu/<il>', methods=['GET'])
def api_tapu_il(il):
    if not check_key():
        return jsonify({"error": "Geçersiz anahtar"}), 403
    try:
        params = {k: v for k, v in request.args.items() if k != 'key'}
        r = requests.get(f"{TARGET}/tapu.php/{il}", params=params, timeout=10)
        return r.text, r.status_code, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/okul', methods=['GET'])
def api_okul():
    if not check_key():
        return jsonify({"error": "Geçersiz anahtar"}), 403
    try:
        params = {k: v for k, v in request.args.items() if k != 'key'}
        r = requests.get(f"{TARGET}/okul.php", params=params, timeout=10)
        return r.text, r.status_code, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/iys', methods=['GET'])
def api_iys():
    if not check_key():
        return jsonify({"error": "Geçersiz anahtar"}), 403
    try:
        params = {k: v for k, v in request.args.items() if k != 'key'}
        r = requests.get(f"{TARGET}/api.php/search", params=params, timeout=10)
        return r.text, r.status_code, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/vergi/ad', methods=['GET'])
def api_vergi_ad():
    if not check_key():
        return jsonify({"error": "Geçersiz anahtar"}), 403
    try:
        params = {k: v for k, v in request.args.items() if k != 'key'}
        r = requests.get(f"{TARGET}/api.php/vergi-adi", params=params, timeout=10)
        return r.text, r.status_code, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/vergi/tc', methods=['GET'])
def api_vergi_tc():
    if not check_key():
        return jsonify({"error": "Geçersiz anahtar"}), 403
    try:
        params = {k: v for k, v in request.args.items() if k != 'key'}
        r = requests.get(f"{TARGET}/api.php/vergi-tc", params=params, timeout=10)
        return r.text, r.status_code, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/ogretmen', methods=['GET'])
def api_ogretmen():
    if not check_key():
        return jsonify({"error": "Geçersiz anahtar"}), 403
    try:
        params = {k: v for k, v in request.args.items() if k != 'key'}
        r = requests.get(f"{TARGET}/api.php/isler-ogretmen", params=params, timeout=10)
        return r.text, r.status_code, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/serino', methods=['GET'])
def api_serino():
    if not check_key():
        return jsonify({"error": "Geçersiz anahtar"}), 403
    try:
        params = {k: v for k, v in request.args.items() if k != 'key'}
        r = requests.get(f"{TARGET}/api.php/vergi", params=params, timeout=10)
        return r.text, r.status_code, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/bursasicil', methods=['GET'])
def api_bursasicil():
    if not check_key():
        return jsonify({"error": "Geçersiz anahtar"}), 403
    try:
        params = {k: v for k, v in request.args.items() if k != 'key'}
        r = requests.get(f"{TARGET}/api.php/bursasicil", params=params, timeout=10)
        return r.text, r.status_code, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/papara', methods=['GET'])
def api_papara():
    if not check_key():
        return jsonify({"error": "Geçersiz anahtar"}), 403
    try:
        params = {k: v for k, v in request.args.items() if k != 'key'}
        r = requests.get(f"{TARGET}/api.php/papara", params=params, timeout=10)
        return r.text, r.status_code, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/eczane', methods=['GET'])
def api_eczane():
    if not check_key():
        return jsonify({"error": "Geçersiz anahtar"}), 403
    try:
        params = {k: v for k, v in request.args.items() if k != 'key'}
        r = requests.get(f"{TARGET}/api.php/eczane", params=params, timeout=10)
        return r.text, r.status_code, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/universite/arama', methods=['GET'])
def api_universite_arama():
    if not check_key():
        return jsonify({"error": "Geçersiz anahtar"}), 403
    try:
        params = {k: v for k, v in request.args.items() if k != 'key'}
        r = requests.get(f"{TARGET}/api.php/universite/arama", params=params, timeout=10)
        return r.text, r.status_code, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/universite/ad', methods=['GET'])
def api_universite_ad():
    if not check_key():
        return jsonify({"error": "Geçersiz anahtar"}), 403
    try:
        params = {k: v for k, v in request.args.items() if k != 'key'}
        r = requests.get(f"{TARGET}/api.php/universite/ad", params=params, timeout=10)
        return r.text, r.status_code, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/universite/soyad', methods=['GET'])
def api_universite_soyad():
    if not check_key():
        return jsonify({"error": "Geçersiz anahtar"}), 403
    try:
        params = {k: v for k, v in request.args.items() if k != 'key'}
        r = requests.get(f"{TARGET}/api.php/universite/soyad", params=params, timeout=10)
        return r.text, r.status_code, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/universite/universite', methods=['GET'])
def api_universite_universite():
    if not check_key():
        return jsonify({"error": "Geçersiz anahtar"}), 403
    try:
        params = {k: v for k, v in request.args.items() if k != 'key'}
        r = requests.get(f"{TARGET}/api.php/universite/universite", params=params, timeout=10)
        return r.text, r.status_code, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/universite/bolum', methods=['GET'])
def api_universite_bolum():
    if not check_key():
        return jsonify({"error": "Geçersiz anahtar"}), 403
    try:
        params = {k: v for k, v in request.args.items() if k != 'key'}
        r = requests.get(f"{TARGET}/api.php/universite/bolum", params=params, timeout=10)
        return r.text, r.status_code, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/universite/kisi', methods=['GET'])
def api_universite_kisi():
    if not check_key():
        return jsonify({"error": "Geçersiz anahtar"}), 403
    try:
        params = {k: v for k, v in request.args.items() if k != 'key'}
        r = requests.get(f"{TARGET}/api.php/universite/kisi", params=params, timeout=10)
        return r.text, r.status_code, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/plaka', methods=['GET'])
def api_plaka():
    if not check_key():
        return jsonify({"error": "Geçersiz anahtar"}), 403
    try:
        params = {k: v for k, v in request.args.items() if k != 'key'}
        r = requests.get(f"{TARGET}/api.php/plaka", params=params, timeout=10)
        return r.text, r.status_code, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return jsonify({"status": "active", "message": "API çalışıyor", "key": "X9kLmN3pQrT7vY2wZ5"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
