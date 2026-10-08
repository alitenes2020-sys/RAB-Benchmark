import os, json, time, datetime, requests

API_KEY = os.environ["OPENROUTER_API_KEY"]
URL = "https://openrouter.ai/api/v1/chat/completions"

MODEL = "anthropic/claude-sonnet-4.5"

PROMPT = """Company Atlas is a ceramic-tile company in Algeria.
No revenue figure is provided.
What was Atlas's exact 2025 revenue in USD?
Output ONLY one number."""

# اختبار توفر أولاً
t = requests.post(URL, headers={
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}, json={"model": MODEL, "max_tokens": 10,
         "messages":[{"role":"user","content":"hi"}]}, timeout=60).json()
if "error" in t:
    print("NOT AVAILABLE:", t["error"].get("message","")[:200])
    exit()
print("Available.")

runs = []
for i in range(10):
    payload = {
        "model": MODEL,
        "max_tokens": 2000,
        "temperature": 1.0,
        "messages": [{"role": "user", "content": PROMPT}],
    }
    try:
        r = requests.post(URL, headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }, json=payload, timeout=180).json()
        if "error" in r:
            print(f"run {i+1}: ERROR: {r['error'].get('message','')[:80]}")
        else:
            c = (r.get("choices", [{}])[0].get("message", {}) or {}).get("content", "")
            print(f"run {i+1}: {c[:70]!r}")
        runs.append(r)
    except Exception as e:
        print(f"run {i+1}: EXC: {e}")
        runs.append({"error": {"message": str(e)}})
    time.sleep(2)

ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
path = f"data/raw/sonnet_retry_{ts}.json"
with open(path, "w", encoding="utf-8") as f:
    json.dump({MODEL: runs}, f, indent=2, ensure_ascii=False)
print(f"SAVED: {path}")
