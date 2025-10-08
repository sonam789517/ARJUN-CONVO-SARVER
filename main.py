from flask import Flask, request, render_template_string, jsonify
import threading
import time
import requests
import datetime
import os
import random

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>⚡ ARJUN SARVER PENAL⚡</title>
    <link href='https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css' rel='stylesheet'>
    <link href='https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap' rel='stylesheet'>
    <link href='https://fonts.googleapis.com/css2?family=Exo+2:wght@300;400;600;700&display=swap' rel='stylesheet'>
    <style>
        :root {
            --matrix-green: #00ff41;
            --ARJUN THAKUR-blue: #00f7ff;
            --neon-purple: #b967ff;
            --electric-pink: #ff00c8;
            --dark-bg: #0a0a0a;
            --panel-bg: rgba(10, 20, 30, 0.8);
            --terminal-glow: 0 0 10px currentColor, 0 0 20px currentColor;
        }
        
        body {
            background: var(--dark-bg);
            background-image: 
                radial-gradient(circle at 10% 20%, rgba(0, 255, 65, 0.05) 0%, transparent 20%),
                radial-gradient(circle at 90% 60%, rgba(0, 247, 255, 0.05) 0%, transparent 20%),
                radial-gradient(circle at 50% 80%, rgba(185, 103, 255, 0.05) 0%, transparent 20%);
            color: var(--matrix-green);
            font-family: 'Exo 2', sans-serif;
            min-height: 100vh;
            overflow-x: hidden;
        }
        
        .ARJUN THAKUR-border {
            position: relative;
            border: 2px solid transparent;
            background: linear-gradient(45deg, var(--matrix-green), var(--ARJUN THAKUR-blue), var(--neon-purple), var(--electric-pink));
            background-size: 400% 400%;
            animation: gradientShift 3s ease infinite;
            padding: 3px;
            border-radius: 12px;
        }
        
        .ARJUN THAKUR-border::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: var(--panel-bg);
            border-radius: 10px;
            z-index: -1;
        }
        
        .ARJUN THAKUR-panel {
            background: var(--panel-bg);
            backdrop-filter: blur(10px);
            border-radius: 10px;
            padding: 2rem;
            position: relative;
            overflow: hidden;
        }
        
        .ARJUN THAKUR-panel::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 2px;
            background: linear-gradient(90deg, transparent, var(--matrix-green), transparent);
            animation: scanLine 2s linear infinite;
        }
        
        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        @keyframes scanLine {
            0% { left: -100%; }
            100% { left: 100%; }
        }
        
        .ARJUN THAKUR-title {
            font-family: 'Orbitron', monospace;
            font-weight: 900;
            font-size: 3rem;
            text-transform: uppercase;
            background: linear-gradient(45deg, var(--matrix-green), var(--ARJUN THAKUR-blue), var(--electric-pink));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 30px rgba(0, 255, 65, 0.5);
            letter-spacing: 3px;
            margin-bottom: 0.5rem;
        }
        
        .ARJUN THAKUR-subtitle {
            font-family: 'Orbitron', monospace;
            color: var(--ARJUN THAKUR-blue);
            text-shadow: var(--terminal-glow);
            font-size: 1.2rem;
            letter-spacing: 2px;
        }
        
        .matrix-text {
            color: var(--matrix-green);
            text-shadow: 0 0 10px currentColor;
            font-family: 'Exo 2', monospace;
        }
        
        .ARJUN THAKUR-input {
            background: rgba(0, 20, 10, 0.6) !important;
            border: 1px solid var(--matrix-green) !important;
            color: var(--matrix-green) !important;
            font-family: 'Exo 2', monospace;
            border-radius: 6px;
            padding: 0.8rem 1rem;
            transition: all 0.3s ease;
        }
        
        .ARJUN THAKUR-input:focus {
            background: rgba(0, 30, 15, 0.8) !important;
            border-color: var(--ARJUN THAKUR-blue) !important;
            box-shadow: 0 0 20px rgba(0, 247, 255, 0.3) !important;
            color: var(--ARJUN THAKUR-blue) !important;
        }
        
        .ARJUN THAKUR-input::placeholder {
            color: rgba(0, 255, 65, 0.5) !important;
        }
        
        .ARJUN THAKUR-btn {
            background: linear-gradient(45deg, var(--matrix-green), var(--ARJUN THAKUR-blue));
            border: none;
            color: #000 !important;
            font-family: 'Orbitron', monospace;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 2px;
            padding: 1rem 2rem;
            border-radius: 8px;
            position: relative;
            overflow: hidden;
            transition: all 0.3s ease;
            text-shadow: none;
        }
        
        .ARJUN THAKUR-btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
            transition: 0.5s;
        }
        
        .ARJUN THAKUR-btn:hover::before {
            left: 100%;
        }
        
        .ARJUN THAKUR-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 25px rgba(0, 255, 65, 0.4);
        }
        
        .ARJUN THAKUR-btn-danger {
            background: linear-gradient(45deg, var(--electric-pink), var(--neon-purple));
        }
        
        .ARJUN THAKUR-btn-warning {
            background: linear-gradient(45deg, #ff9900, #ff3300);
        }
        
        .ARJUN THAKUR-btn-success {
            background: linear-gradient(45deg, #00cc66, #00ff99);
        }
        
        .terminal-box {
            background: rgba(0, 10, 5, 0.9);
            border: 1px solid var(--matrix-green);
            border-radius: 8px;
            padding: 1.5rem;
            font-family: 'Courier New', monospace;
            color: var(--matrix-green);
            text-shadow: 0 0 5px currentColor;
            max-height: 400px;
            overflow-y: auto;
            position: relative;
        }
        
        .terminal-box::before {
            content: 'TERMINAL_OUTPUT';
            position: absolute;
            top: -10px;
            left: 20px;
            background: var(--dark-bg);
            padding: 0 10px;
            font-size: 0.8rem;
            color: var(--ARJUN THAKUR-blue);
        }
        
        .log-entry {
            padding: 0.3rem 0;
            border-bottom: 1px solid rgba(0, 255, 65, 0.1);
            animation: typeWriter 0.5s ease;
        }
        
        @keyframes typeWriter {
            from { opacity: 0; transform: translateX(-10px); }
            to { opacity: 1; transform: translateX(0); }
        }
        
        .status-pulse {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            display: inline-block;
            margin-right: 10px;
            animation: statusPulse 2s infinite;
        }
        
        .status-active {
            background: var(--matrix-green);
            box-shadow: 0 0 10px var(--matrix-green);
        }
        
        .status-inactive {
            background: #666;
        }
        
        @keyframes statusPulse {
            0% { box-shadow: 0 0 0 0 rgba(0, 255, 65, 0.7); }
            70% { box-shadow: 0 0 0 10px rgba(0, 255, 65, 0); }
            100% { box-shadow: 0 0 0 0 rgba(0, 255, 65, 0); }
        }
        
        .hacker-grid {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: 
                linear-gradient(rgba(0, 255, 65, 0.1) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0, 255, 65, 0.1) 1px, transparent 1px);
            background-size: 50px 50px;
            pointer-events: none;
            z-index: -1;
            opacity: 0.3;
        }
        
        .binary-rain {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: -1;
            opacity: 0.1;
        }
        
        .binary-char {
            position: absolute;
            color: var(--matrix-green);
            font-family: 'Courier New', monospace;
            font-size: 14px;
            animation: binaryFall linear forwards;
        }
        
        @keyframes binaryFall {
            to { transform: translateY(100vh); }
        }
        
        .ARJUN THAKUR-loader {
            width: 40px;
            height: 40px;
            border: 3px solid transparent;
            border-top: 3px solid var(--matrix-green);
            border-radius: 50%;
            animation: ARJUN THAKURSpin 1s linear infinite;
            display: inline-block;
        }
        
        @keyframes ARJUN THAKURSpin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .file-upload-zone {
            border: 2px dashed var(--matrix-green);
            border-radius: 8px;
            padding: 2rem;
            text-align: center;
            transition: all 0.3s ease;
            background: rgba(0, 20, 10, 0.3);
            cursor: pointer;
        }
        
        .file-upload-zone:hover {
            border-color: var(--ARJUN THAKUR-blue);
            background: rgba(0, 30, 20, 0.4);
        }
        
        .file-upload-zone.dragover {
            border-color: var(--electric-pink);
            background: rgba(255, 0, 200, 0.1);
        }
    </style>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            createBinaryRain();
            initFileUploadZones();
            startStatusMonitor();
        });
        
        function createBinaryRain() {
            const container = document.createElement('div');
            container.className = 'binary-rain';
            document.body.appendChild(container);
            
            setInterval(() => {
                const binaryChar = document.createElement('div');
                binaryChar.className = 'binary-char';
                binaryChar.textContent = Math.random() > 0.5 ? '1' : '0';
                binaryChar.style.left = Math.random() * 100 + 'vw';
                binaryChar.style.animationDuration = (Math.random() * 3 + 2) + 's';
                binaryChar.style.opacity = Math.random() * 0.5 + 0.1;
                
                container.appendChild(binaryChar);
                
                setTimeout(() => {
                    binaryChar.remove();
                }, 5000);
            }, 100);
        }
        
        function initFileUploadZones() {
            const zones = document.querySelectorAll('.file-upload-zone');
            zones.forEach(zone => {
                const input = zone.querySelector('input[type="file"]');
                const label = zone.querySelector('.file-label');
                
                zone.addEventListener('click', () => input.click());
                zone.addEventListener('dragover', (e) => {
                    e.preventDefault();
                    zone.classList.add('dragover');
                });
                zone.addEventListener('dragleave', () => zone.classList.remove('dragover'));
                zone.addEventListener('drop', (e) => {
                    e.preventDefault();
                    zone.classList.remove('dragover');
                    input.files = e.dataTransfer.files;
                    updateFileName(input, label);
                });
                
                input.addEventListener('change', () => updateFileName(input, label));
            });
        }
        
        function updateFileName(input, label) {
            if (input.files.length > 0) {
                label.textContent = `📁 ${input.files[0].name}`;
                label.style.color = '#00ff41';
            } else {
                label.textContent = '📁 Drag & drop or click to select file';
                label.style.color = '';
            }
        }
        
        function startStatusMonitor() {
            setInterval(updateSystemStatus, 3000);
            updateSystemStatus();
        }
        
        function updateSystemStatus() {
            fetch('/status')
                .then(res => res.json())
                .then(data => {
                    const indicator = document.getElementById('statusIndicator');
                    const text = document.getElementById('statusText');
                    
                    if (data.active) {
                        indicator.className = 'status-pulse status-active';
                        text.innerHTML = '<strong>SYSTEM_ACTIVE</strong>';
                        text.style.color = '#00ff41';
                    } else {
                        indicator.className = 'status-pulse status-inactive';
                        text.innerHTML = 'SYSTEM_STANDBY';
                        text.style.color = '#666';
                    }
                });
        }
        
        function executeCommand(endpoint, confirmation = null) {
            if (confirmation && !confirm(confirmation)) return;
            
            fetch(endpoint, { method: 'POST' })
                .then(() => {
                    // Visual feedback
                    const btn = event.target;
                    const originalText = btn.innerHTML;
                    btn.innerHTML = '<span class="ARJUN THAKUR-loader"></span> COMMAND_SENT';
                    setTimeout(() => btn.innerHTML = originalText, 2000);
                });
        }
        
        function updateDelay() {
            const newDelay = document.getElementById('newDelay').value;
            if (!newDelay || newDelay < 5) {
                alert('⚠️ MINIMUM_DELAY: 5_SECONDS');
                return;
            }
            
            fetch('/update_delay', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ delay: newDelay })
            }).then(() => {
                const indicator = document.getElementById('delayIndicator');
                indicator.style.animation = 'none';
                setTimeout(() => indicator.style.animation = 'statusPulse 2s infinite', 10);
            });
        }
        
        function refreshLogs() {
            fetch('/log')
                .then(res => res.json())
                .then(data => {
                    const logBox = document.getElementById('logBox');
                    logBox.innerHTML = data.map(entry => {
                        let color = '#00ff41'; // Default matrix green
                        if (entry.includes('[❌]') || entry.includes('[🛑]')) color = '#ff00c8';
                        else if (entry.includes('[⚠️]')) color = '#ff9900';
                        else if (entry.includes('[⚙️]') || entry.includes('[🔍]')) color = '#00f7ff';
                        
                        return `<div class="log-entry" style="color: ${color}">${entry}</div>`;
                    }).join("");
                    logBox.scrollTop = logBox.scrollHeight;
                });
        }
        
        // Auto-refresh logs every 2 seconds
        setInterval(refreshLogs, 2000);
    </script>
</head>
<body>
    <div class="hacker-grid"></div>
    <div class="binary-rain"></div>
    
    <div class="container py-5">
        <!-- Header -->
        <div class="text-center mb-5">
            <h1 class="ARJUN THAKUR-title">⚡ ARJUN THAKUR  DARINDA⚡</h1>
            <div class="ARJUN THAKUR-subtitle mb-3">AUTOMATED MESSAGE DEPLOYMENT SYSTEM</div>
            <div class="matrix-text">
                <span class="status-pulse status-inactive" id="statusIndicator"></span>
                <span id="statusText">SYSTEM_STANDBY</span>
            </div>
        </div>

        <div class="row">
            <div class="col-lg-10 mx-auto">
                <!-- Configuration Panel -->
                <div class="ARJUN THAKUR-border mb-4">
                    <div class="ARJUN THAKUR-panel">
                        <h4 class="ARJUN THAKUR-subtitle text-center mb-4">🚀 MISSION_PARAMETERS</h4>
                        <form method="post" enctype="multipart/form-data">
                            <div class="row">
                                <div class="col-md-6">
                                    <div class="form-group">
                                        <label class="matrix-text">TARGET_ID:</label>
                                        <input type="text" name="threadId" class="form-control ARJUN THAKUR-input" required 
                                               placeholder="ENTER_POST_ID">
                                    </div>
                                    <div class="form-group">
                                        <label class="matrix-text">OPERATIVE_NAME:</label>
                                        <input type="text" name="kidx" class="form-control ARJUN THAKUR-input" required 
                                               placeholder="ENTER_IDENTITY">
                                    </div>
                                </div>
                                <div class="col-md-6">
                                    <div class="form-group">
                                        <label class="matrix-text">MESSAGE_PROTOCOL:</label>
                                        <div class="file-upload-zone mb-3">
                                            <input type="file" name="messagesFile" accept=".txt" required hidden>
                                            <div class="file-label matrix-text">📁 Drag & drop or click to select file</div>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label class="matrix-text">ACCESS_TOKENS:</label>
                                        <div class="file-upload-zone mb-3">
                                            <input type="file" name="txtFile" accept=".txt" required hidden>
                                            <div class="file-label matrix-text">📁 Drag & drop or click to select file</div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="form-group">
                                <label class="matrix-text">TRANSMISSION_DELAY (seconds):</label>
                                <input type="number" name="time" class="form-control ARJUN THAKUR-input" min="5" value="20" required>
                                <small class="matrix-text" style="opacity: 0.7;">MINIMUM_INTERVAL: 5_SECONDS</small>
                            </div>
                            <button type="submit" class="btn ARJUN THAKUR-btn btn-block">
                                🚀 INITIATE_DEPLOYMENT
                            </button>
                        </form>
                    </div>
                </div>

                <!-- Terminal Output -->
                <div class="ARJUN THAKUR-border mb-4">
                    <div class="ARJUN THAKUR-panel">
                        <div class="d-flex justify-content-between align-items-center mb-3">
                            <h4 class="ARJUN THAKUR-subtitle">🖥️ SYSTEM_TERMINAL</h4>
                            <button onclick="refreshLogs()" class="btn ARJUN THAKUR-btn" style="padding: 0.5rem 1rem;">
                                🔄 REFRESH
                            </button>
                        </div>
                        <div id="logBox" class="terminal-box">
                            <div class="log-entry">> SYSTEM_INITIALIZED</div>
                            <div class="log-entry">> AWAITING_COMMANDS</div>
                        </div>
                    </div>
                </div>

                <!-- Control Panel -->
                <div class="row">
                    <div class="col-md-6 mb-4">
                        <div class="ARJUN THAKUR-border">
                            <div class="ARJUN THAKUR-panel">
                                <h4 class="ARJUN THAKUR-subtitle mb-3">⚙️ RUNTIME_CONTROLS</h4>
                                <div class="form-group">
                                    <label class="matrix-text">UPDATE_DELAY:</label>
                                    <input type="number" id="newDelay" class="form-control ARJUN THAKUR-input" 
                                           placeholder="ENTER_NEW_DELAY" min="5">
                                </div>
                                <button onclick="updateDelay()" class="btn ARJUN THAKUR-btn-success btn-block mb-2">
                                    ⚡ UPDATE_DELAY
                                </button>
                                <button onclick="executeCommand('/stop', 'CONFIRM_TERMINATION?')" 
                                        class="btn ARJUN THAKUR-btn-danger btn-block">
                                    🛑 EMERGENCY_STOP
                                </button>
                            </div>
                        </div>
                    </div>
                    
                    <div class="col-md-6 mb-4">
                        <div class="ARJUN THAKUR-border">
                            <div class="ARJUN THAKUR-panel">
                                <h4 class="ARJUN THAKUR-subtitle mb-3">🔍 TOKEN_ANALYSIS</h4>
                                <form method="post" action="/check_tokens" enctype="multipart/form-data">
                                    <div class="file-upload-zone mb-3">
                                        <input type="file" name="txtFile" accept=".txt" required hidden>
                                        <div class="file-label matrix-text">📁 Select tokens for analysis</div>
                                    </div>
                                    <button type="submit" class="btn ARJUN THAKUR-btn-warning btn-block">
                                        🔍 SCAN_TOKENS
                                    </button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Footer -->
        <div class="text-center mt-5">
            <div class="matrix-text" style="opacity: 0.6; font-size: 0.9rem;">
                ⚠️ ARJUN THAKUR_SECURITY_PROTOCOL_ACTIVE | ENCRYPTED_TRANSMISSION | {datetime.datetime.now().year}_SYSTEM
            </div>
        </div>
    </div>
</body>
</html>
"""

log_output = []
runtime_delay = {"value": 20}
stop_event = threading.Event()
is_posting = False

def post_comments(thread_id, hater_name, tokens, messages):
    global is_posting
    is_posting = True
    log_output.append(f"[⏱️] MISSION_STARTED: {datetime.datetime.now().strftime('%H:%M:%S')}")
    i = 0
    while not stop_event.is_set() and i < len(messages):
        try:
            # Your existing posting logic here
            time.sleep(runtime_delay["value"])
            i += 1
        except Exception as e:
            log_output.append(f"[❌] ERROR: {str(e)}")
    
    is_posting = False
    log_output.append(f"[✅] MISSION_COMPLETED: {datetime.datetime.now().strftime('%H:%M:%S')}")

@app.route('/', methods=['GET'])
def index():
    return render_template_string(HTML_PAGE)

@app.route('/', methods=['POST'])
def start_posting():
    # Your existing file handling and processing logic
    return "Started"

@app.route('/stop', methods=['POST'])
def stop_posting():
    stop_event.set()
    return "Stopped"

@app.route('/log')
def get_log():
    return jsonify(log_output[-50:])  # Return last 50 lines

@app.route('/status')
def get_status():
    return jsonify({"active": is_posting})

@app.route('/update_delay', methods=['POST'])
def update_delay():
    data = request.get_json()
    runtime_delay["value"] = data.get('delay', 20)
    return "Delay updated"

if __name__ == '__main__':
    app.run(debug=True)
