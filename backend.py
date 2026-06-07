from flask import Flask, request, jsonify, Response
import requests
import json
from functools import wraps

app = Flask(__name__)

# HEDEF SUNUCU (GİZLİ)
TARGET = "http://104.249.8.46"

# GİZLİ ANAHTAR - Bunu URL'de ?key= veya &key= ile gönderecekler
SECRET_KEY = "X9kLmN3pQrT7vY2wZ5"

def check_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # URL'de ?key= veya &key= kontrol et
        key = request.args.get('key')
        if not key or key != SECRET_KEY:
            return jsonify({"error": "Geçersiz veya eksik anahtar", "status": 403}), 403
        # Anahtarı temizle ki hedef sunucuya gitmesin
        request_args = {k: v for k, v in request.args.items() if k != 'key'}
        request.args = request_args
        return f(*args, **kwargs)
    return decorated

def proxy_request(endpoint, params=None):
    """Hedef sunucuya istek yap"""
    try:
        url = f"{TARGET}/{endpoint}"
        response = requests.get(url, params=params, timeout=15)
        try:
            return jsonify(response.json())
        except:
            return jsonify({"data": response.text, "status": response.status_code})
    except Exception as e:
        return jsonify({"error": str(e), "status": 500}), 500

# ============================================
# 1. 101M.PHP - KİŞİ BİLGİLERİ (20 endpoint)
# ============================================
@app.route('/api/101m', methods=['GET'])
@check_key
def api_101m():
    params = request.args.to_dict()
    return proxy_request("101m.php", params)

# ============================================
# 2. TAPU.PHP - ANA TAPU (14 endpoint)
# ============================================
@app.route('/api/tapu', methods=['GET'])
@check_key
def api_tapu():
    params = request.args.to_dict()
    return proxy_request("tapu.php", params)

# ============================================
# 3. TAPU İL BAZLI (81 il x 4 = 324 endpoint)
# ============================================
@app.route('/api/tapu/<il>', methods=['GET'])
@check_key
def api_tapu_il(il):
    params = request.args.to_dict()
    return proxy_request(f"tapu.php/{il}", params)

# ============================================
# 4. OKUL.PHP (15 endpoint)
# ============================================
@app.route('/api/okul', methods=['GET'])
@check_key
def api_okul():
    params = request.args.to_dict()
    return proxy_request("okul.php", params)

# ============================================
# 5. API.PHP - TÜM ALT API'LER (38 endpoint)
# ============================================

# ----- IYS (4) -----
@app.route('/api/iys', methods=['GET'])
@check_key
def api_iys():
    params = request.args.to_dict()
    return proxy_request("api.php/search", params)

# ----- Vergi (2) -----
@app.route('/api/vergi/ad', methods=['GET'])
@check_key
def api_vergi_ad():
    params = request.args.to_dict()
    return proxy_request("api.php/vergi-adi", params)

@app.route('/api/vergi/tc', methods=['GET'])
@check_key
def api_vergi_tc():
    params = request.args.to_dict()
    return proxy_request("api.php/vergi-tc", params)

# ----- Öğretmen (4) -----
@app.route('/api/ogretmen', methods=['GET'])
@check_key
def api_ogretmen():
    params = request.args.to_dict()
    return proxy_request("api.php/isler-ogretmen", params)

# ----- Serino/Vergi No (4) -----
@app.route('/api/serino', methods=['GET'])
@check_key
def api_serino():
    params = request.args.to_dict()
    return proxy_request("api.php/vergi", params)

# ----- Bursa Sicil (4) -----
@app.route('/api/bursasicil', methods=['GET'])
@check_key
def api_bursasicil():
    params = request.args.to_dict()
    return proxy_request("api.php/bursasicil", params)

# ----- Papara (4) -----
@app.route('/api/papara', methods=['GET'])
@check_key
def api_papara():
    params = request.args.to_dict()
    return proxy_request("api.php/papara", params)

# ----- Eczane (3) -----
@app.route('/api/eczane', methods=['GET'])
@check_key
def api_eczane():
    params = request.args.to_dict()
    return proxy_request("api.php/eczane", params)

# ----- Üniversite (6) -----
@app.route('/api/universite/arama', methods=['GET'])
@check_key
def api_universite_arama():
    params = request.args.to_dict()
    return proxy_request("api.php/universite/arama", params)

@app.route('/api/universite/ad', methods=['GET'])
@check_key
def api_universite_ad():
    params = request.args.to_dict()
    return proxy_request("api.php/universite/ad", params)

@app.route('/api/universite/soyad', methods=['GET'])
@check_key
def api_universite_soyad():
    params = request.args.to_dict()
    return proxy_request("api.php/universite/soyad", params)

@app.route('/api/universite/universite', methods=['GET'])
@check_key
def api_universite_adi():
    params = request.args.to_dict()
    return proxy_request("api.php/universite/universite", params)

@app.route('/api/universite/bolum', methods=['GET'])
@check_key
def api_universite_bolum():
    params = request.args.to_dict()
    return proxy_request("api.php/universite/bolum", params)

@app.route('/api/universite/kisi', methods=['GET'])
@check_key
def api_universite_kisi():
    params = request.args.to_dict()
    return proxy_request("api.php/universite/kisi", params)

# ----- Plaka (2) -----
@app.route('/api/plaka', methods=['GET'])
@check_key
def api_plaka():
    params = request.args.to_dict()
    return proxy_request("api.php/plaka", params)

# ============================================
# TOPLU SORGU - Tüm verileri tek endpoint'te al
# ============================================
@app.route('/api/tum', methods=['GET'])
@check_key
def api_tum():
    params = request.args.to_dict()
    tc = params.get('tc')
    ad = params.get('ad')
    soyad = params.get('soyad')
    
    result = {}
    
    if tc:
        result['kisi'] = requests.get(f"{TARGET}/101m.php", params={'tc': tc}).json() if tc else None
        result['tapu'] = requests.get(f"{TARGET}/tapu.php", params={'tc': tc}).json() if tc else None
        result['okul'] = requests.get(f"{TARGET}/okul.php", params={'tc': tc}).json() if tc else None
        result['vergi'] = requests.get(f"{TARGET}/api.php/vergi-tc", params={'tc': tc}).json() if tc else None
    if ad and soyad:
        result['vergi_adi'] = requests.get(f"{TARGET}/api.php/vergi-adi", params={'adi': ad, 'soyadi': soyad}).json()
    
    return jsonify(result)

# Ana sayfa
@app.route('/')
def home():
    return jsonify({
        "api": "Gizli API Gateway",
        "status": "active",
        "kullanim": "Tüm endpointlerde ?key=X9kLmN3pQrT7vY2wZ5 parametresi gereklidir",
        "ornek": "/api/101m?key=X9kLmN3pQrT7vY2wZ5&tc=13334777982"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
