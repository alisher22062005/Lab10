import psycopg2

# Connect to the database by creating connection variable or object
conn = psycopg2.connect(
    host="localhost",
    database="students_data",
    user="postgres",
    password="Alisher_18"
)

# Creating cursor to get access to database
cur=conn.cursor()


# Delete previous table
cur.execute("DROP TABLE students_data")

# Creating table
cur.execute("""CREATE TABLE students_data(
            name VARCHAR (255),
            year_of_study INT,
            phone_number VARCHAR (255),
            id VARCHAR (200) PRIMARY KEY 

);""")
conn.commit()

# Inserting the information
cur.execute("""INSERT INTO students_data(name,year_of_study,phone_number,id) VALUES
            ('Maxim',3,'+7708765432','12346735'),
            ('Alisher',1,'+770897838',123456789),
            ('Ivan',4,'+77072345678',11748748),
            ('Nikita',2,'+770798756547',11113393),
            ('Denis',3,'46746474647',84983984948)
""")


# Updating the phone_number
cur.execute("""UPDATE students_data
            SET phone_number='000000000'
            WHERE phone_number='46746474647';
    
            
            
""")
# Deleting the name
cur.execute("""DELETE FROM students_data
            WHERE name='Nikita';
""")

#Querying data by the name 
""" SELECT 
  name,
  id,
  year_of_study,
  phone_number
FROM 
  students_data 
ORDER BY 
  name ASC;"""


conn.commit()



