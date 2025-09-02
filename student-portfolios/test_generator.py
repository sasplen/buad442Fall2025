#!/usr/bin/env python3
"""
Test script for the portfolio README generator.
Run this to verify the generator works correctly.
"""

import subprocess
import sys
from pathlib import Path

def test_generator():
    """Test the portfolio README generator."""
    print("🧪 Testing Portfolio README Generator...")
    
    # Check if the generator script exists
    generator_path = Path("generate_portfolio_readme.py")
    if not generator_path.exists():
        print("❌ Error: generate_portfolio_readme.py not found!")
        return False
    
    try:
        # Run the generator
        result = subprocess.run([sys.executable, "generate_portfolio_readme.py"], 
                              capture_output=True, text=True, cwd=".")
        
        if result.returncode == 0:
            print("✅ Generator script ran successfully!")
            print("📝 Output:", result.stdout.strip())
            
            # Check if README.md was created
            readme_path = Path("README.md")
            if readme_path.exists():
                print("✅ README.md was created successfully!")
                
                # Read and display first few lines
                with open(readme_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    lines = content.split('\n')[:10]
                    print("📖 First 10 lines of generated README:")
                    for i, line in enumerate(lines, 1):
                        print(f"   {i:2d}: {line}")
                
                return True
            else:
                print("❌ README.md was not created!")
                return False
        else:
            print("❌ Generator script failed!")
            print("Error:", result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Error running generator: {e}")
        return False

if __name__ == "__main__":
    success = test_generator()
    if success:
        print("\n🎉 All tests passed! The generator is working correctly.")
    else:
        print("\n💥 Tests failed! Please check the errors above.")
        sys.exit(1)
