# Resources

## TOKENS.txt

    if 1 element in row:
        token = element
        token id = prefix + element
    
    else if multiple elements in row:
        if 3 elements:
            token = regex(3rd element)        
            
        else if 2 elements:
            token = 2nd element

        token id = 1st element

prefix defined in main.py
    