import requests
import json

BASE_URL = "http://localhost:5000"

def test_valid_area_calculation():
    """Test valid area calculation with positive integers"""
    response = requests.get(f"{BASE_URL}/area", params={"length": 5, "width": 10})
    assert response.status_code == 200
    data = response.json()
    assert data["length"] == 5.0
    assert data["width"] == 10.0
    assert data["area"] == 50.0
    print("✓ Test passed: Valid area calculation")

def test_decimal_values():
    """Test area calculation with decimal values"""
    response = requests.get(f"{BASE_URL}/area", params={"length": 3.5, "width": 2.5})
    assert response.status_code == 200
    data = response.json()
    assert data["length"] == 3.5
    assert data["width"] == 2.5
    assert data["area"] == 8.75
    print("✓ Test passed: Decimal values")

def test_missing_length():
    """Test error handling when length parameter is missing"""
    response = requests.get(f"{BASE_URL}/area", params={"width": 10})
    assert response.status_code == 400
    data = response.json()
    assert "error" in data
    assert "required" in data["error"].lower()
    print("✓ Test passed: Missing length parameter")

def test_missing_width():
    """Test error handling when width parameter is missing"""
    response = requests.get(f"{BASE_URL}/area", params={"length": 5})
    assert response.status_code == 400
    data = response.json()
    assert "error" in data
    assert "required" in data["error"].lower()
    print("✓ Test passed: Missing width parameter")

def test_missing_both_parameters():
    """Test error handling when both parameters are missing"""
    response = requests.get(f"{BASE_URL}/area")
    assert response.status_code == 400
    data = response.json()
    assert "error" in data
    assert "required" in data["error"].lower()
    print("✓ Test passed: Missing both parameters")

def test_invalid_numeric_value():
    """Test error handling with invalid non-numeric values"""
    response = requests.get(f"{BASE_URL}/area", params={"length": "abc", "width": 10})
    assert response.status_code == 400
    data = response.json()
    assert "error" in data
    assert "valid numbers" in data["error"].lower()
    print("✓ Test passed: Invalid numeric value")

def test_negative_values():
    """Test error handling with negative values"""
    response = requests.get(f"{BASE_URL}/area", params={"length": -5, "width": 10})
    assert response.status_code == 400
    data = response.json()
    assert "error" in data
    assert "positive" in data["error"].lower()
    print("✓ Test passed: Negative values validation")

def test_zero_values():
    """Test error handling with zero values"""
    response = requests.get(f"{BASE_URL}/area", params={"length": 0, "width": 10})
    assert response.status_code == 400
    data = response.json()
    assert "error" in data
    assert "positive" in data["error"].lower()
    print("✓ Test passed: Zero values validation")

def run_all_tests():
    """Run all tests"""
    print("\n" + "="*50)
    print("Running Flask API Tests")
    print("="*50 + "\n")
    
    tests = [
        test_valid_area_calculation,
        test_decimal_values,
        test_missing_length,
        test_missing_width,
        test_missing_both_parameters,
        test_invalid_numeric_value,
        test_negative_values,
        test_zero_values
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ Test failed: {test.__name__}")
            print(f"  Error: {e}")
            failed += 1
        except requests.exceptions.ConnectionError:
            print(f"✗ Connection failed: Make sure Flask app is running on {BASE_URL}")
            return
        except Exception as e:
            print(f"✗ Test error: {test.__name__}")
            print(f"  Error: {e}")
            failed += 1
    
    print("\n" + "="*50)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("="*50 + "\n")

if __name__ == "__main__":
    run_all_tests()
