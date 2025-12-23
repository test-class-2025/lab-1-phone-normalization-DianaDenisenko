import pytest
import random
import string
from main import UserProfile, normalize_phone_number

# --- Part 1: Unit Tests for the normalizer ---

def test_returns_none_for_none():
    """Ensure None remains None."""
    assert normalize_phone_number(None) is None

def test_converts_int_to_string():
    """Ensure integers are converted to string."""
    assert normalize_phone_number(1234567890) == "1234567890"

def test_cleans_formatted_string():
    """Ensure spaces, dashes, and parentheses are removed."""
    dirty_phone = "+1 (555) 123-4567"
    expected = "15551234567"
    assert normalize_phone_number(dirty_phone) == expected

def test_extracts_from_object():
    """Ensure it can pull data from a legacy object wrapper."""
    class UserWrapper:
        def __init__(self, p):
            self.phone = p
            
    obj = UserWrapper("999-000")
    assert normalize_phone_number(obj) == "999000"

def test_randomized_messy_input():
    """
    Randomized Test.
    Injects random special characters into a phone number to ensure
    the student uses a proper cleaning method (like regex or filter).
    """
    # Generate a clean number
    original_digits = str(random.randint(1000000000, 9999999999))
    
    # Inject noise characters
    noise = ["-", " ", "(", ")", "+", ".", "/"]
    messy_phone = ""
    for digit in original_digits:
        messy_phone += digit + random.choice(noise)
        
    # The function must recover the original digits
    result = normalize_phone_number(messy_phone)
    assert result == original_digits, f"Failed to clean input: {messy_phone}"

# --- Part 2: Integration Tests with Pydantic ---

def test_model_integration_clean():
    """Check integration within the Pydantic model."""
    payload = {
        "user_id": 1,
        "username": "jdoe",
        "phone_number": "(800) 555-HELP"
    }
    
    user = UserProfile(**payload)
    assert user.phone_number == "800555HELP"

def test_model_handles_int_input():
    """Check if model accepts integer phone numbers."""
    payload = {
        "user_id": 2,
        "username": "alice",
        "phone_number": 12345
    }
    user = UserProfile(**payload)
    assert user.phone_number == "12345"
