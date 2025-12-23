import re
from typing import Any, Optional, Annotated, Union
from pydantic import BaseModel, ConfigDict, BeforeValidator

def normalize_phone_number(value: Any) -> Optional[str]:
    """
    Cleans up the phone number input to return a string of digits only.
    
    TODO: Implement the logic:
    1. If `value` is None -> return None.
    2. If `value` is an integer (int) -> convert it to string.
    3. If `value` is a string -> remove all non-digit characters (spaces, dashes, parentheses, plus signs).
       Example: "+1 (555) 000-1111" should become "15550001111".
    4. If `value` is an object with a `.phone` attribute (LegacyWrapper) -> extract the phone and process it.
    5. Return the cleaned string.
    """
    # --- START OF YOUR CODE ---
    pass
    # --- END OF YOUR CODE ---


# Custom type: Validates/cleanups input before Pydantic checks string constraints
PhoneNumberField = Annotated[
    Optional[str], 
    BeforeValidator(normalize_phone_number)
]

class UserProfile(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: int
    username: str
    # The field that uses your cleaning logic
    phone_number: PhoneNumberField = None
