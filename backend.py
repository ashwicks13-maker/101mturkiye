from flask import Flask, request, jsonify, Response
import requests
import json

app = Flask(__name__)

# Hedef sunucu
TARGET = "http://104.249.8.46"

def proxy_request(endpoint, params=None):
    """Hedef sunucuya istek yap"""
    try:
        url = f"{TARGET}/{endpoint}"
        r = requests.get(url, params=params, timeout=15)
        
        # JSON ise JSON döndür, değilse text döndür
        try:
            return jsonify(r.json())
        except:
            return Response(r.text, mimetype='application/json')
    except Exception as e:
        return jsonify({"error": str(e), "status": 500}), 500

# ========== 1. KİŞİ BİLGİLERİ ==========
@app.route('/api/101m', methods=['GET'])
def api_101m():
    params = request.args.to_dict()
    return proxy_request("101m.php", params)

# ========== 2. TAPU ==========
@app.route('/api/tapu', methods=['GET'])
def api_tapu():
    params = request.args.to_dict()
    return proxy_request("tapu.php", params)

@app.route('/api/tapu/<il>', methods=['GET'])
def api_tapu_il(il):
    params = request.args.to_dict()
    return proxy_request(f"tapu.php/{il}", params)

# ========== 3. OKUL ==========
@app.route('/api/okul', methods=['GET'])
def api_okul():
    params = request.args.to_dict()
    return proxy_request("okul.php", params)

# ========== 4. SORGU PANELİ - GSM/TC ==========
@app.route('/api/sorgu/tc', methods=['GET'])
def api_sorgu_tc():
    tc = request.args.get('tc')
    if not tc:
        return jsonify({"error": "tc parametresi gerekli"}), 400
    return proxy_request("sorgu_paneli/apiocgsmtc.php", {'tc': tc})

@app.route('/api/sorgu/gsm', methods=['GET'])
def api_sorgu_gsm():
    gsm = request.args.get('gsm')
    if not gsm:
        return jsonify({"error": "gsm parametresi gerekli"}), 400
    return proxy_request("sorgu_paneli/apiocgsmtc.php", {'gsm': gsm})

# ========== 5. IYS ==========
@app.route('/api/iys', methods=['GET'])
def api_iys():
    params = request.args.to_dict()
    return proxy_request("api.php/search", params)

# ========== 6. VERGİ ==========
@app.route('/api/vergi/ad', methods=['GET'])
def api_vergi_ad():
    params = request.args.to_dict()
    return proxy_request("api.php/vergi-adi", params)

@app.route('/api/vergi/tc', methods=['GET'])
def api_vergi_tc():
    params = request.args.to_dict()
    return proxy_request("api.php/vergi-tc", params)

# ========== 7. ÖĞRETMEN ==========
@app.route('/api/ogretmen', methods=['GET'])
def api_ogretmen():
    params = request.args.to_dict()
    return proxy_request("api.php/isler-ogretmen", params)

# ========== 8. SERİNO ==========
@app.route('/api/serino', methods=['GET'])
def api_serino():
    params = request.args.to_dict()
    return proxy_request("api.php/vergi", params)

# ========== 9. BURSA SİCİL ==========
@app.route('/api/bursasicil', methods=['GET'])
def api_bursasicil():
    params = request.args.to_dict()
    return proxy_request("api.php/bursasicil", params)

# ========== 10. PAPARA ==========
@app.route('/api/papara', methods=['GET'])
def api_papara():
    params = request.args.to_dict()
    return proxy_request("api.php/papara", params)

# ========== 11. ECZANE ==========
@app.route('/api/eczane', methods=['GET'])
def api_eczane():
    params = request.args.to_dict()
    return proxy_request("api.php/eczane", params)

# ========== 12. ÜNİVERSİTE ==========
@app.route('/api/universite/arama', methods=['GET'])
def api_universite_arama():
    params = request.args.to_dict()
    return proxy_request("api.php/universite/arama", params)

@app.route('/api/universite/ad', methods=['GET'])
def api_universite_ad():
    params = request.args.to_dict()
    return proxy_request("api.php/universite/ad", params)

@app.route('/api/universite/soyad', methods=['GET'])
def api_universite_soyad():
    params = request.args.to_dict()
    return proxy_request("api.php/universite/soyad", params)

@app.route('/api/universite/universite', methods=['GET'])
def api_universite_uni():
    params = request.args.to_dict()
    return proxy_request("api.php/universite/universite", params)

@app.route('/api/universite/bolum', methods=['GET'])
def api_universite_bolum():
    params = request.args.to_dict()
    return proxy_request("api.php/universite/bolum", params)

@app.route('/api/universite/kisi', methods=['GET'])
def api_universite_kisi():
    params = request.args.to_dict()
    return proxy_request("api.php/universite/kisi", params)

# ========== 13. PLAKA ==========
@app.route('/api/plaka', methods=['GET'])
def api_plaka():
    params = request.args.to_dict()
    return proxy_request("api.php/plaka", params)

# ========== ANA SAYFA ==========
@app.route('/')
def home():
    return jsonify({
        "api": "API Gateway",
        "status": "active",
        "endpoints": [
            "/api/101m",
            "/api/tapu", 
            "/api/tapu/<il>",
            "/api/okul",
            "/api/sorgu/tc?tc=TC",
            "/api/sorgu/gsm?gsm=GSM",
            "/api/iys",
            "/api/vergi/ad",
            "/api/vergi/tc",
            "/api/ogretmen",
            "/api/serino",
            "/api/bursasicil",
            "/api/papara",
            "/api/eczane",
            "/api/universite/*",
            "/api/plaka"
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
