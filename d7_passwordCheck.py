def validate_password(password: str) -> bool:  
    # Rules:  
    # - Min 8 chars  
    # - Contains uppercase/lowercase  
    # - Has digit  
    # - Has special char [!@#$%^&*]
    chars_allowed = ('!', '@', '#', '$', '%', '^', '&', '*')
    has_lower,has_upper,has_digit,has_char = False, False, False, False
    
    
    # Length check: Min 8 chars 
    if len(password)>=8:
        for letter in password:

            # Checks for each condition:
            if letter in chars_allowed:
                has_char = True
            
            if letter.isupper():
                has_upper = True
            
            if letter.islower():
                has_lower = True
            
            if letter.isdigit():
                has_digit = True
                
    else:
        return False
    
    return has_char and has_digit and has_lower  and has_upper
