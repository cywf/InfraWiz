#!/usr/bin/env python3
"""
Simple test to verify InfraWiz core functionality.
This test doesn't require an OpenAI API key.
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_import():
    """Test that the module can be imported"""
    try:
        import infra_wiz
        print("✓ Module import successful")
        return True
    except ImportError as e:
        print(f"✗ Module import failed: {e}")
        return False

def test_functions_exist():
    """Test that required functions exist"""
    import infra_wiz
    
    required_functions = ['get_user_input', 'ask_openai', 'execute_bash_command', 'main']
    success = True
    
    for func_name in required_functions:
        if hasattr(infra_wiz, func_name):
            print(f"✓ Function '{func_name}' exists")
        else:
            print(f"✗ Function '{func_name}' missing")
            success = False
    
    return success

def test_dependencies():
    """Test that required dependencies are available"""
    # Map package names to their import names
    required_modules = {
        'openai': 'openai',
        'python-dotenv': 'dotenv'
    }
    success = True
    
    for package_name, import_name in required_modules.items():
        try:
            __import__(import_name)
            print(f"✓ Dependency '{package_name}' available")
        except ImportError:
            print(f"✗ Dependency '{package_name}' missing")
            success = False
    
    return success

def test_no_api_key_handling():
    """Test that the script handles missing API key gracefully"""
    import infra_wiz
    import subprocess
    
    # Ensure no API key is set
    env = os.environ.copy()
    env.pop('OPENAI_API_KEY', None)
    
    try:
        result = subprocess.run(
            [sys.executable, 'infra_wiz.py'],
            input=b'test\n',
            capture_output=True,
            timeout=5,
            env=env
        )
        
        output = result.stderr.decode() + result.stdout.decode()
        
        if 'OPENAI_API_KEY' in output and 'not set' in output:
            print("✓ Missing API key handled correctly")
            return True
        else:
            print("✗ Missing API key not handled correctly")
            return False
    except Exception as e:
        print(f"✗ Error testing API key handling: {e}")
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("InfraWiz Functionality Tests")
    print("=" * 60)
    print()
    
    tests = [
        ("Import Test", test_import),
        ("Function Existence Test", test_functions_exist),
        ("Dependencies Test", test_dependencies),
        ("API Key Handling Test", test_no_api_key_handling),
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        print("-" * 40)
        results.append(test_func())
    
    print("\n" + "=" * 60)
    passed = sum(results)
    total = len(results)
    print(f"Results: {passed}/{total} tests passed")
    print("=" * 60)
    
    return 0 if all(results) else 1

if __name__ == "__main__":
    sys.exit(main())
