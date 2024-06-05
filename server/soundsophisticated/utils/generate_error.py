from datetime import datetime

def generate_error(error, request=None): 
    # Log or use the request details
    if request:
        return {
            "request_time": str(datetime.now()),
            "ip_address": request.remote_addr,
            "host": request.host,
            "user_agent": request.user_agent.string,
            "url": request.url,
            "method": request.method,
            "headers": dict(request.headers),
            "error": error
        }
    else: 
        return error