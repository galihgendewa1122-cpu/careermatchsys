import subprocess
import json

payload = {
    'years_code': 1.0,
    'education_level': 1,
    'all_skills': 'typescript javascript react angular htmlcss',
    'tools': 'visual studio code git ',
    'databases': 'postgresql oracle'
}

payload_str = json.dumps(payload)
result = subprocess.run(
    ['python', 'ai_service.py', payload_str],
    capture_output=True, text=True
)

data = json.loads(result.stdout)
print("Top Recommendations:")
for rec in data.get('top_recommendations', []):
    print(f"  {rec['career']}: {rec['score']}%")
print(f"Roadmap: {data.get('ai_roadmap', '-')}")