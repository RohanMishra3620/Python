from login import login
from dashboard import get_dashboard

def app_flow(username, password):
    if login(username, password):
        return get_dashboard(username)
    else:
        return "Login Failed"
