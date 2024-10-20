from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import os
import subprocess
from datetime import datetime

def htop_view(request):
    # Fetch system details
    name = "Sandhya"  # Your full name
    username = os.getenv('USER')  # System username
    server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    
    # Run the 'top' command and capture its output
    top_output = subprocess.getoutput('top -b -n 1')

    # Format the response as HTML
    html_response = f"""
    <html>
    <body>
    <h1>System Info</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre>{top_output}</pre>
    </body>
    </html>
    """
    
    return HttpResponse(html_response)