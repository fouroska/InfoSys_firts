# InfoSys_firts

Metadata = { "OS":"Windows10", "testing":"POSTMAN"} #τρεχω APP μέσα στο φάκελο που βρίσκεται η pymongo

#Ερώτημα 1
  με την εντολή users.find({"username":data["username"]}).count() ελέγχω αν υπάρχει άλλος χρήστης με το ίδιο username.
  εφόσον δεν υπάρχει δημιουργώ τον user (user = {"username": data['username'], "password": data['password']}) και τον βάζω μέσα στην βάση στη συλλογή users   (users.insert_one(user)
 
#Ερώτημα 2 
  ψάχνω στην συλλογή users με βάση το όνομα που έχουμε περάσει  στο json του body και το εκχωρώ στο user (user = users.find_one({"username":data['username']})
  αν είναι και το password του user ίδιο με αυτό που έδωσε ο χρήστης στο json του body τότε καλλώ τις συναρτήσεις σύμφωνα με τις οδηγίες της εκφώνησης.

#Ερωτήματα 3,4,5,6,7,8,9 (Αναφέρομαι στο κοινό τους σημείο δηλαδή στο uuid που περνάει στα header του request 
  Για να εκτελέσουμε αυτό το ζητούμενο με χρήση του POSTMAN πρέπει να στη επιλογή "Auth" να επιλέξουμε στο "Type" το "API Key" και στην συνέχεια να δώσουμε τιμή στο "API Key" το "authorization" και ακριβώς από κάτω στο "value" να βάλλουμε το uuid που έχουμε πάρει ως έξοδο από το #Ερώτημα 2 
  
#Ερώτημα 3
  βάζω όλα τα data του student στο student ψάχνοντας βάση το email του (student =  students.find_one({"email":data['email']}))
  
#Ερώτημα 4
  βάζω όλα τα data του student στο student ψάχνοντας βάση το yearOfBirth(ίσο με 1991 δηλαδή να είναι 30 χρονών) του (student =  students.find({"yearOfBirth": {"$eq":1991}}))
  
#Ερώτημα 5
  αρκετά παρόμοια με το #Ερώτημα 4, μόνο που τώρα θέλω να είναι μεγαλύτεροι ή ίσοι από 30 χρονών (student =  students.find({"yearOfBirth": {"$lte":1991}}))
  
#Ερώτημα 6
  ψάχνω φοιτητή με βάση το email και το κατοχωρώ στην student_temp με σκοπό να πάρω μετά το student_temp["name"](student_temp =  students.find_one({"email":data['email']})) και επίσης κοιτάω μέσω if statement αν υπάρχουν τα data του adrress και τα εκχωρώ στη student (student={"name": student_temp['name'], "street": student_temp['street'], "postcode": student_temp['postcode']})
  
#Ερώτημα 7
  διαγράφω χρήστη με βάση το email του (students.delete_one({'email': data['email']}))
#Ερώτημα 8
#Ερώτημα 9
