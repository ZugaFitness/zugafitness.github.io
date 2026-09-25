import sys
import glob
import json
import urllib.request
import urllib.error

def main():
    if len(sys.argv) < 2:
        print("Usage: python indexnow_ping.py <url1> [<url2> ...]")
        sys.exit(1)

    urls = sys.argv[1:]

    # Find the key file at the repo root
    key_files = glob.glob("*.txt")
    key = None
    for f in key_files:
        if len(f) == 36 and f.endswith(".txt"): # 32 hex chars + .txt
            try:
                with open(f, 'r') as kf:
                    content = kf.read().strip()
                    if len(content) == 32 and content == f[:-4]:
                        key = content
                        break
            except Exception:
                pass

    if not key:
        print("Error: Could not find IndexNow key file (32-hex characters .txt) at repo root.")
        sys.exit(1)

    host = "zugafitness.in"
    key_location = f"https://{host}/{key}.txt"

    data = {
        "host": host,
        "key": key,
        "keyLocation": key_location,
        "urlList": urls
    }

    json_data = json.dumps(data).encode('utf-8')
    req = urllib.request.Request(
        "https://api.indexnow.org/indexnow",
        data=json_data,
        headers={'Content-Type': 'application/json; charset=utf-8'},
        method='POST'
    )

    try:
        with urllib.request.urlopen(req) as response:
            status = response.getcode()
            print(f"IndexNow Ping Result: HTTP {status} (SUCCESS)")
            for url in urls:
                print(f"  - {url} -> OK")
    except urllib.error.HTTPError as e:
        print(f"IndexNow Ping Failed: HTTP {e.code}")
        print(e.read().decode('utf-8'))
        sys.exit(1)
    except Exception as e:
        print(f"IndexNow Ping Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
