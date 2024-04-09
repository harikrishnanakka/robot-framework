from django.shortcuts import render
from django.http import JsonResponse
import subprocess
import json
from django.views.decorators.csrf import csrf_exempt

def generate_test_suite(tests):
    # Generate Robot Framework test suite dynamically
    suite = "*** Test Cases ***\n"
    for test in tests:
        title = test.get('title', 'Untitled Test')
        steps = test.get('steps', [])
        suite += f"{title}\n"
        for step in steps:
            suite += f"    {step}\n"
        suite += "\n"
    return suite

@csrf_exempt
def execute_tests(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            tests = data.get('tests', [])
            
            # Generate Robot Framework test suite dynamically
            test_suite = generate_test_suite(tests)
            
            # Write test suite to a temporary file
            with open('temp_test_suite.robot', 'w') as f:
                f.write(test_suite)
            
            # Execute the test suite using subprocess
            result = subprocess.run(['robot', 'temp_test_suite.robot'], capture_output=True)
            
            # Read the output and return as JSON response
            output = result.stdout.decode('utf-8')
            return JsonResponse({'output': output})
            
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON payload'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
