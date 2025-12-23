import re
from typing import Any, Optional, Annotated
from pydantic import BaseModel, ConfigDict, BeforeValidator

def normalize_phone_number(value: Any) -> Optional[str]:
    if value is None:
        return None

    value_str = str(value)

    if hasattr(value, "phone"):
        value_str = str(value.phone)

    cleaned = re.sub(r'[^a-zA-Z0-9]', '', value_str)
    
    return cleaned


ProductSpecsField = Annotated[Optional[str], BeforeValidator(normalize_phone_number)]


class UserProfile(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    user_id: int
    username: str
    phone_number: ProductSpecsField = None
