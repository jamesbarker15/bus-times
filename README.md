## Bus Times Simplified

When my daughter began attending a new school, she had to rely on the bus for 
her daily commute. Unfortunately, the official bus app proved to be cumbersome 
and not user-friendly. To streamline her journey, I developed a simple 
application/script. This tool fetches real-time bus data from transportapi.com, 
displaying information about the next departing buses from her specific
bus stop. It then generates a basic HTML page, which I host on my VPS using 
NGINX. The entire process is automated through crontab and a script, ensuring 
minute by minute updates at the end of school.