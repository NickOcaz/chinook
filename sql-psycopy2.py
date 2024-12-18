import psycopg2

# Connect to your postgres DB
connection = psycopg2.connect(database="chinook")

# Open a cursor to perform database operations
cursor = connection.cursor()

# Execute a query
cursor.execute('SELECT * FROM "Artist"')

# Fetch the result
results = cursor.fetchall()

# Close the connection
connection.close()

# Print the results
for result in results:
    print(result)