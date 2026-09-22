def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status" 
        # Usage print(http_status(200)) # Output: ok print(http_status(404)) # Output: Not Found print(http_status(500)) # Output: Internal Server Error print(http_status(403)) # Output: Unknown Status
        
# usage
print(http_status(200)) # Output: ok
print(http_status(404)) # Output: Not Found 
print(http_status(500)) # Output: Internal Server Error
print(http_status(403)) # Output: Unknown Status