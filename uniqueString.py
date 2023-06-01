def unique_characters(str):
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            if str[i] == str[j]:
                return False
    
    return True
    
# Test Case 1
print(unique_characters("He"))
# Test Case 2
print(unique_characters("Hello"))
        
    