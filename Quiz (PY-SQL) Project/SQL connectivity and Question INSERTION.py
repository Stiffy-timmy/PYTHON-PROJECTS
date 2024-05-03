import mysql.connector as c
con=c.connect(host='localhost',
              user='root',
              passwd='prajurjyaask007',
              database='quiz')
cursor=con.cursor()

query="insert into booklet values(%s,%s,%s,%s,%s,%s)"
value=[("A constant voltage is applied between the two ends of a uniform metallic wire. Some heat is developed in it. The heat developed is doubled if ?","a. the length of the wire is doubled","b. the radius of the wire is doubled","c. both the length and the radius of the wire are halved","d. both the length and the radius of the wire are doubled","d-both the length and the radius of the wire are doubled"),
       ("What is the pH value of the human body?","a. 9.2 to 9.8","b. 7.0 to 7.8","c. 6.1 to 6.3","d. 5.4 to 5.6","b-7.0 to 7.8"),
       ("Which of the following are called 'Key Industrial animals'?","a. Producers","b. Tertiary consumers","c. Primary consumers","d. None of these","c-Primary consumers")]
cursor.executemany(query,value)
con.commit()
print("successfully inserted")

