import re
def is_sqli(payload):
    sqli_patterns = [
        r'\bSELECT\b.*\bFROM\b',
        r'\bINSERT\b.*\bINTO\b',
        r'\bUPDATE\b.*\bSET\b',
        r'\bDELETE\b.*\bFROM\b',
        r'\bDROP\b.*\bTABLE\b',
        r'\bUNION\b',
        r'\bAND\b.*\b\w+\b\s*(=|>|<)',
        r'\bOR\b.*\b\w+\b\s*(=|>|<)',
        r'\bEXEC\b',
        r'\bXP_\b',
        r'\bALTER\b.*\bTABLE\b',
        r'\bCREATE\b.*\bTABLE\b',
        r'\bTRUNCATE\b.*\bTABLE\b',
        r'\bINTO\b.*\bOUTFILE\b',
        r'\bLOAD\b.*\bFILE\b'
    ]

    for pattern in sqli_patterns:
        if re.search(pattern, payload, re.IGNORECASE):
            return True

    return False