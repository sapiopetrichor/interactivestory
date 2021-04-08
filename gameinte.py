from tkinter import *
from PIL import ImageTK,Image 

root = Tk()
root.iconbitmap ('~/Desktop/brain-png.png') #topicon

#creating a label widget
mylabel = Label(root, text ="Με το νου σου!")
#putting the label onto the screen
mylabel.pack()

my_img = ImageTk.PhotoImage(Image.open("brain-png.png")) #put image

root.mainloop()

import time #time between text

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]

required = ("\nUse only A or B\n") #Cutting down on duplication

def start_game():
    intro()

#intro
def intro():
    print('Εργάζεσαι στο γνωστό ειδησεογραφικό οργανισμό “Ειδήσεις Τώρα!” που έχει πρωτοπορήσει στον τομέα της ηλεκτρονικής δημοσιογραφίας με έγκυρη πληροφόρηση που είναι άμεσα προσβάσιμη στους λογαριασμούς κοινωνικών δικτύων και την ιστοσελίδα του οργανισμού.')
    time.sleep(5.0)
    print('Το πρώτο πράγμα που πάντα κάνεις το πρωί είναι να ελέγξεις τα email σου στο κινητό σου ενώ ετοιμάζεσαι για το γραφείο, για να δεις στα γρήγορα αν υπάρχει κάτι που να πρέπει να διερευνήσεις για τη μέρα.')
    time.sleep(5.0)
    storyline_A()


#end of intro background context of game, follows on to story
#player clicks on email to read message

def storyline_A():
    time.sleep(5.0)
    print('Email message from Local News Editor sent 5 minutes ago:')
    time.sleep(2.0)
    print ('Καλημέρα ελπίζω να δεις αυτό το μήνυμα άμεσα.')
    time.sleep(2.0)
    print('Παρατηρώ ότι στο #Cyprus άρχισαν να παρουσιάζονται φωτογραφίες από ένα περίεργο εύρημα σε κάποιο χωριό της Κύπρου.')
    time.sleep(2.0)
    print('Ακόμη δε ξέρουμε πολλές λεπτομέρειες.')
    time.sleep(2.0)
    print ('Πάρε με τηλέφωνο να συντονιστούμε άμεσα.')
#email message ends 
    time.sleep(5.0)
    first_choice()

def first_choice():
    print ('Τι θα κάνεις;') 
    time.sleep(2.0)
    print('A: Παίρνεις τηλέφωνο τον/την συντάκτη')
    print('ή')
    print('B: Μπαίνεις στο Pistagram για να δεις φωτογραφίες στο #cyprus')
    time.sleep(2.0)
    choice = input(">>> ") #Here is your first choice. 
    #player responds with eith A or B
    if choice in answer_A:
        story_2A()
    else:
        story_2B()
#if player responds with eith A goes to story 2A, or  if B goes to story 2B

#story_2A
def story_2A():
    print ('Συνομιλία με συντάκτη:')
    time.sleep(5.0)
    print ('Συντάκτης: Καλημέρα! Ευτυχώς που με πήρες τηλέφωνο, έχω περισσότερες λεπτομέρειες.')
    time.sleep(2.0)
    print ('Εσύ: Τέλεια - τι είναι τελικά;')
    time.sleep(2.0)
    print ('Συντάκτης: Βασικά βρέθηκε ένα τεράστιο πιθάρι στη Χοιροκοιτία στη μέση του πουθενά και είναι… έξυπνη.')
    time.sleep(2.0)
    print ('Εσύ: Τι εννοείς;')
    time.sleep(2.0)
    print ('Συντάκτης: Δε ξέρω σίγουρα.')
    time.sleep(2.0)
    print('Θέλω να πας εκεί να δεις τις λεπτομέρειες και να μάθεις όσα περισσότερα μπορείς.')
    time.sleep(2.0)
    print ('Νομίζω κανένα άλλο ειδησεογραφικό κανάλι δεν το έχει καλύψει ακόμη.')
    time.sleep(2.0)
    print('Πρέπει να προλάβουμε, αλλά πρέπει να ξέρουμε ακριβώς για τι πρόκειται.')
    time.sleep(2.0)
    print ('Εσύ: Έγινε, θα σε ενημερώσω μόλις έχω περισσότερες λεπτομέρειες.')
    time.sleep(5.0)
    story_2A_question()


def story_2A_question():
 #player responds with eith A or B
    print('Τι θα κάνεις;')
    time.sleep(2.0)
    print('A: Ξεκινάς για Χοιροκοιτία')
    time.sleep(2.0)
    print('ή') 
    time.sleep(2.0)
    print('B: Στέλνεις προσωπικό μήνυμα στο χρήση @KseroEgo για να ζητησεις περισσότερες πληροφορίες') 
    choice = input(">>> ") 
    #if A goes to story 4A if B goes to story 7A
    if choice in answer_A:
        story_4A()
    else: 
        story_7A()

#story4A
def story_4A():
    print('Φτάνεις στη Χοιροκοιτία και βρίσκεις το πιθάρι που φαίνεται να έχει διάμετρο περίπου 1 μέτρο.')
    time.sleep(5.0)
    print('‘Οσο το πλησιάσεις ακούς ήχο να βγαίνει από μέσα και με φωνή να λέει:')
    time.sleep(5.0)
    print('“Το 1468, ο Ιάκωβος Β΄ της Κύπρου, αλλιώς γνωστός ως Ιάκωβος ο Νόθος, έγινε Βασιλιάς της Κύπρου.') 
    time.sleep(5.0)
    print('Για βασίλισσα και γυναίκα του επέλεξε την Κατερίνα Κορνάρο”')
    time.sleep(5.0)
    print('Στο χώρο υπάρχουν άτομα από το Τμήμα Αρχαιολογίας και άτομα από το χωριό.')
    time.sleep(5.0)
    print('Προς το παρόν δεν μπορείς να δεις κανένα άλλο δημοσιογράφο.')
    time.sleep(5.0)
    story_4A_question()
        
        
def story_4A_question():       
#player responds with eith A or B
    print('Τι θα κάνεις;')
    time.sleep(5.0)
    print('A: Βγάζεις βίντεο με το κινητό σου και κάνεις αμέσως ανάρτηση στο κοινωνικό δίκτυο Quitter.') 
    time.sleep(5.0)
    print('ή') 
    time.sleep(5.0)
    print('B: Παίρνεις συνέντευξη από τα άτομα που που είναι στο χώρο.')
    choice = input(">>> ") 
#if A goes to story 5A if B goes to story 5B
    if choice in answer_A:
        story_5A()
    else: 
        story_5B()

#story 5A & Choice to 5B or 5C depending on selection of A/B
def story_5A():
    print ('Η ανάρτηση σου στο Quitter έχει μεγάλη ανταπόκριση!')
    time.sleep(5.0)
    print ('Ήδη έχεις εκατοντάδες shares, πολλά σχόλια και μόλις έλαβες ένα προσωπικό μήνυμα στο λογαριασμό σου.')
    time.sleep(5.0)
    print ('Μόλις έλαβες και ένα μήνυμα από το συντάκτη σου που σου ζητά να βρεις περισσότερες πληροφορίες άμεσα.')
    time.sleep(5.0)
    print('Έχεις δύο επιλογές.')
    time.sleep(5.0)
    print('A: Επικοινωνείς με το Τμήμα Αρχαιοτήτων.')
    time.sleep(5.0)
    print('ή') 
    time.sleep(5.0)
    print('B: Επικοινωνείς με το χρήστη που σου έστειλε προσωπικό μήνυμα')
#player selects A or B
    choice = input(">>> ") 
#if A goes to story 5B, if B goes to story 5C
    if choice in answer_A:
        story_5B()
    else: 
        story_5C()

#story 5B
def story_5B():
    print ('Αντιπρόσωπος από το Τμήμα Αρχαιοτήτων σε ενημερώνει ότι ήταν αρκετά συγκλονισμένοι με το εύρημα.')
    time.sleep(5.0)
    print('Ενώ προσπαθούσαν να διερευνήσουν τις συνθήκες με τις οποίες εμφανιστηκε στο πεδίο, έλαβαν ένα μήνυμα που ήταν υπογεγραμμένο από την “Ομάδα 7”')
    time.sleep(5.0)
    print ('Εν τω μεταξύ έχουν αρχίσουν να εμφανίζονται και άλλοι δημοσιογράφοι στη σκηνή.')
    time.sleep(5.0)
    story_5B_question()
    
def story_5B_question():
    print ('Τι θα κάνεις;')
    time.sleep(5.0)
    print('A: Ενημερώνεις το κοινό μέσω επίσημης ανάρτησης στην ιστοσελίδα του Ειδήσεις Τώρα!')
    time.sleep(5.0)
    print('ή')
    time.sleep(5.0)
    print('B: Επικοινωνείς με συναδέλφους σου για να μάθεις περισσότερα για την Ομάδα 7.')
#player selects A or B
    choice = input(">>> ")
    if choice in answer_A:
        story_ending_4()
    else: 
        story_6A()
#if player selects option A goes to ending 4, or if option B goes to 6A

#story 6A
def story_6A():
    print('Παίρνεις μήνυμα από τη συνάδελφο σου Έλενα ότι η Ομάδα 7 είναι μια καλλιτεχνική ομάδα που έχει ως επικεφαλή τον Γιώργο Γ...')
    time.sleep(5.0)
    print('Σου δίνει και τις λεπτομέρειες επικοινωνίας που έχει ανακτήσει από την ιστοσελίδα της ομάδας.')
    time.sleep(5.0)
    print('Στη σκηνή φτάνουν περισσότερο άτομα για να δουν το πιθάρι από κοντά.')
    time.sleep(2.0)
    print('Τι θα κάνεις;')
    time.sleep(5.0)
    print('A: Επικοινωνείς με το Γιώργο Γ.')
    time.sleep(5.0)
    print('ή')
    print('B: Θα πάρεις συνέντευξη από άτομα που τώρα φτάνουν στη σκηνή.')
#player selects A or B
    choice = input(">>> ")
    if choice in answer_A:
        story_8A()
    else: 
        story_8B()
#if player selects option A goes to 8A, or if option B goes to 8B

#story 8A
def story_8A():
    print('Στο τηλέφωνο ο Γιωργος σε ενημερώνει ότι το “Εξυπνο Πιθάρι” είναι μια εικαστική παρέμβαση που έχει οργανώσει η Ομάδα 7.')
    time.sleep(5.0)
    print('Τίτλος του έργου είναι “Διάλογος με το Παρελθόν”.')
    time.sleep(5.0)
    print('Συγκεκριμένα ανέφερε:')
    time.sleep(2.0)
    print('“Το Πιθάρι παντρεύει τη τεχνολογία του σήμερα με την εικόνα του χθες.') 
    time.sleep(2.0)
    print('Τι ιστορίες αφήνουμε πίσω όταν είμαστε κολλημένοι με την τεχνολογία και το μέλλον;') 
    time.sleep(2.0)
    print('Αυτές είναι και σκέψεις που μας οδήγησαν σε αυτό το καλλιτεχνικό έργο.')
    time.sleep(2.0)
    print('Ελπίζουμε ο κόσμος να βρει το χρόνο να ζήσει αυτή τη μοναδική εμπειρία και να αγκαλιάσει το έργο μας.”')
    time.sleep(5.0)
    print('Λαμβάνεις ειδοποίηση από τις Ειδήσεις Αστραπή:')
    time.sleep(2.0)
    print('“Εξωγήινοι αφήνουν μυστηριώδες πιθάρι στην Χοιροκοιτία: Αποκλειστικό ρεπορτάζ”.')
    time.sleep(5.0)
    print('Τι θα κάνεις;')
    time.sleep(2.0)
    print('A: Ετοιμάζεις την αναφορά για το Ειδήσεις Τώρα!')
    print('ή')
    time.sleep(2.0)
    print('B: Θέλεις να πάρεις σχόλια και από άλλες πηγές.')
  #player selects A or B
    time.sleep(5.0)
    choice = input(">>> ")
    if choice in answer_A:
        story_ending_2()
    else: 
        story_ending_3()
#if player selects option A goes to ending 2, or if option B goes to ending 3

#story_ending_2
def story_ending_2():
        print('Παίρνεις μήνυμα από τον συντάκτη σου που σε ενημερώνει ότι χρειάζεται να ισορροπήσεις το άρθρο σου')
        time.sleep(2.0)
        print('έτσι ώστε να μη φαίνεται σαν διαφήμιση του καλλιτεχνικού έργου.')
        time.sleep(2.0)
        print('Έπρεπε να είχες πάρει κι άλλες συνεντεύξεις.')
#endgame2 // player lost!
        intro()
        #restarts

#story_2B
def story_2B():
    print('Ενώ ψάχνεις φωτογραφίες στο #Cyprus ανακαλύπτεις  μια φωτογραφία που απεικονίζει ένα θεόρατο πιθάρι από τον χρήστη @KseroEgo και είναι tagged στο Κούριο.')
    time.sleep(5.0)
    print('Τι θα κάνεις;')
    time.sleep(2.0)
    print('A: Ξεκινάς για Κούριο.')
    time.sleep(2.0)
    print('ή') 
    time.sleep(2.0)
    print('Ζητάς από συνάδελφο σου να την επικυρώσει.') #possible visual road sign or email icon to show difference in choice
    #player chooses A or B
    time.sleep(5.0)
    choice = input(">>> ")
    if choice in answer_A:
        story_3A()
    else: 
        story_3B()
#if player selects A it goes to 3A, if B it goes to 3B

#story_3A
def story_3A():
    print('Φτάνεις στο Κούριο και δε μπορείς να εντοπίσεις κάπου το πιθάρι.')
    time.sleep(2.0)
    print('Αρχίζει να ανησυχείς επειδή ο χρόνος τρέχει και μπορεί να χάσεις την αποκλειστικότητα της είδησης.')
    time.sleep(5.0)
    print ('Τι θα κάνεις;') 
    time.sleep(2.0)
    print('A: Παίρνεις τηλέφωνο τον / την συντάκτη.')
    time.sleep(2.0)
    print('ή')
    time.sleep(2.0)
    print('B: Στέλνεις προσωπικό μήνυμα στο χρήση @KseroEgo για να πάρεις περισσότερες πληροφορίες') #possible visual phone icon
    time.sleep(5.0)
    #player chooses A or B
    choice = input(">>> ")
    if choice in answer_A:
        story_2A()
    else: 
        story_4B()
#if player selects A it goes to 2A, if B it goes to 4B

#story_4B
def story_4B():
    print('(Συνομιλία με @KseroEgo)')
    time.sleep(5.0)
    print('Εσύ: Γεια σου, είμαι δημοσιογράφος στον οργανισμό Ειδήσεις Τώρα!')
    time.sleep(2.0)
    print('Μπορείς να μου δώσεις περισσότερες λεπτομέρειες για το πιθάρι στη φωτογραφία;')
    time.sleep(5.0)
    print('@KseroEgo: Γεια. Ήταν του παππού μου.')
    time.sleep(2.0)
    print('Έγινε κάτι; Έγινα διάσημος;')
    time.sleep(5.0)
    print('Εσύ: Όχι, δεν έγινε κάτι.')
    time.sleep(2.0)
    print('Ευχαριστώ για το χρόνο σου, απλά ήθελα να το διευκρινίσω. Ευχαριστώ.')
    time.sleep(5.0)
    print('Ενώ τελειώνεις τη συνομιλία, έρχεται ειδοποίηση στο κινητό σου.')
    time.sleep(5.0)
    print('Τι θα κάνεις;')
    print('A: Παίρνεις τηλέφωνο τον / την συντάκτη.') 
    time.sleep(2.0)
    print('ή')
    time.sleep(2.0)
    print('B: Ελέγχεις την ειδοποίηση.') #possible visual phone icon and/or notification icon
#player chooses A or B
    time.sleep(5.0)
    choice = input(">>> ")
    if choice in answer_A:
        story_2A()
    else: 
        story_ending_1()
#if player selects A it goes to 2A, if B it goes to ending_1

#story_ending_1
def story_ending_1():
    print('Ο ανταγωνιστής “Ειδήσεις Αστραπή” μόλις ανάρτησε άρθρο για το “Εξυπνο Πιθάρι” που βρέθηκε στην Χοιροκοιτία.')
    time.sleep(2.0)
    print('Έχασες την αποκλειστικότητα της είδησης.')
#endgame1 // player lost!
    intro()
    #restarts

#story_7A
def story_7A():
    print ('Ο ειδικός σου δίνει περισσότερες πληροφορίες για τα πιθάρια στην Κύπρο.')
    time.sleep(2.0)
    print('Παίρνεις μήνυμα από το συντάκτη σου που πληροφορήθηκε ότι στη Χοιροκοιτία έχει αρχίσει ήδη να μαζεύεται κι άλλο κόσμος.')
    #https://www.philenews.com/politismos/kypros/article/514547/ta-pitharia-kai-oi-pitharades-tis-kyproy possible quote from this site
    story_4A()
    
    
#story_6B NO 6B **********

#story_5C
def story_5C():
    print('Το μήνυμα είναι μια σειρά από emoji και τελικά δεν ανταποκρίνεσαι.')
    time.sleep(2.0)
    print('Επικοινωνείς με το Τμήμα Αρχαιοτήτων.')
    story_5B () #goes to 5B 

#story_8B
def story_8B():
    print('Παίρνεις συνέντευξη από δύο άτομα που είναι στο χώρο και αλληλεπιδρούν με το “έξυπνο πιθάρι”.')
    #possible quotes from interviews with people
    time.sleep(5.0)
    print('Τι θα κάνεις;')
    time.sleep(2.0)
    print('A: Ετοιμάζεις την αναφορά για το Ειδήσεις Τώρα!') 
    time.sleep(2.0)
    print('ή')
    print('B: Επικοινωνείς με το Γιώργο Γ. από την Ομάδα 7')
    time.sleep(5.0)
    #player selects A or B
    choice = input(">>> ")
    if choice in answer_A:
        story_ending_4()
    else: 
        story_8A()
#if player selects A it goes to atory_ending_4, if B it goes to story_8A

#story_ending_4
def story_ending_4():
    print('Παίρνεις μήνυμα από τον συντάκτη σου που σε ενημερώνει ότι χρειάζεται επιπλέον πληροφορίες.')
    time.sleep(2.0)
    print('Δεν είναι ξεκάθαρο ποια είναι η Ομάδα 7 και ποιος είναι ο ρόλος της.')
    time.sleep(5.0)
    print('Έπρεπε να το ξεκαθαρίσεις, ή να μη εμπιστευτείς την πηγή.')
    time.sleep(2.0)
    print('Άλλη φορά, καλύτερα!')
#endof game 4 // player lost
    intro()
    #restarts

#story_ending_3
def story_ending_3():
    print('Μπράβο, πολύ καλή δουλειά!')
    time.sleep(2.0)
    print('Παρόλο που τελικά ήταν μια καμπάνια προώθησης κατάφερες να πάρεις πληροφορίες από αρκετές πηγές και να επικεντρωσεις στο κομμάτι της Κυπριακής ιστορίας.')
    time.sleep(2.0)
    print('Συνέχισε έτσι!')
#player wins! // end of game 3
    intro()
    #restarts


#story_3B
def story_3B():
    print('Ευτυχώς που μου έστειλες τη φωτογραφία.')
    time.sleep(2.0)
    print('Μόλις ελέγξα αν είναι αληθινή μέσω του εργαλείου TinEye και φαίνεται ότι είναι στο Φοινί και όχι στο Κούριο.')
    time.sleep(2.0)
    print('Ελπίζω να σε βοηθάει αυτό.')
    time.sleep(2.0)
    print('Τι θα κάνεις;')
    time.sleep(2.0)
    print('A: Παίρνεις τηλέφωνο τον / την συντάκτη') #possible visual phone
    time.sleep(2.0)
    print('ἠ')
    time.sleep(2.0)
    print('B: Στέλνεις προσωπικό μήνυμα στο χρήση @KseroEgo για να ζητησεις  περισσότερες πληροφορίες')
    #player selects A or B
    choice = input(">>> ")
    if choice in answer_A:
        story_2A()
    else: 
        story_4B()
#if player selects A it goes to story_2A, if B it goes to story_4B


start_game()
