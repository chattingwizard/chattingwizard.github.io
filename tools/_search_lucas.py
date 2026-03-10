"""Search Airtable for any model linked to client Lucas."""
import sys, os
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from airtable_cli import get_headers, API_BASE
import requests

headers = get_headers()

# Get all records and check client name
r = requests.get(API_BASE, headers=headers, params={'pageSize': 100})
r.raise_for_status()
records = r.json().get('records', [])

print(f"Total records: {len(records)}\n")

# Search for Lucas in client name or recent records
for rec in records:
    f = rec.get('fields', {})
    name = f.get('Model Name', '???')
    client = f.get('Client Name', '')
    created = f.get('Created', '')
    status = f.get('Status', '')
    
    if 'lucas' in str(client).lower() or 'lucas' in str(name).lower():
        print(f"=== MATCH: {name} ===")
        print(f"  Client: {client}")
        print(f"  Status: {status}")
        print(f"  Created: {created}")
        print()

# Also show most recently created records
print("=== RECENT RECORDS (last 5) ===")
sorted_recs = sorted(records, key=lambda r: r.get('fields', {}).get('Created', ''), reverse=True)
for rec in sorted_recs[:5]:
    f = rec.get('fields', {})
    print(f"  {f.get('Model Name', '???')} | Client: {f.get('Client Name', '?')} | Created: {f.get('Created', '?')[:10]} | Status: {f.get('Status', '?')}")
