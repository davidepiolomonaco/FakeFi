class NetworkError(Exception):
    def __init__(self, message="[!] Network Error"):
        super().__init__(message)
        

class AccessPointError(NetworkError):
    def __init__(self, message="[!] Access Point Error"):
        super().__init__(message)
        
        
class JammerError(NetworkError):
    def __init__(self, message="[!] Jammer Error"):
        super().__init__(message)