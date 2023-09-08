import requests
import datetime
from keys import APP_ID, API_KEY, BUS_STOP
from style import STYLE

# API URL
url = f"https://transportapi.com/v3/uk/bus/stop_timetables/{BUS_STOP}.json?" \
      f"app_id={APP_ID}&app_key={API_KEY}"

# Get current time
current_time = datetime.datetime.now().strftime("%H:%M")

# Request the data
response = requests.get(url)
data = response.json()

# Extract bus departure information
departures = data['departures']
information = departures['all']

# Create the HTML file for writing
with open('index.html', 'w') as html_file:
    # Write the bulk HTML data and current time.
    html_file.write(STYLE)
    html_file.write(f"<p class='time'>The time right now is {current_time}</p>\n")
    html_file.write("<hr>\n")

    # Write bus departure information
    for info in information[:2]:
        line_number = info['line']
        departure_time = info['best_departure_estimate']

        html_file.write("<div class='bus-info'>\n")
        html_file.write(f"<p><strong>Route Number:</strong> {line_number}</p>\n")
        html_file.write(f"<p><strong>Departing at:</strong> {departure_time}</p>\n")
        html_file.write("</div>\n")
        html_file.write("<hr>\n")
        html_file.write("</body>\n</html>")

    print("Data has been written to index.html")