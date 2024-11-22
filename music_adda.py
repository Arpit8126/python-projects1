import tkinter as tk
from tkinter import messagebox, ttk
import webbrowser

# Sample data for categories and languages
song_categories_hindi = {
    "Romantic": [
        "Tera Ban Jaunga", "Tum Hi Ho", "Pehla Nasha", "Janam Janam", "Raabta",
        "Tera Hone Laga Hoon", "Mere Haath Mein", "Kabira", "Tum Se Hi", "Tum Mile",
        "Kahani Suno", "Ishq Wala Love", "Pyaar Kiya To Darna Kya", "Hasi",
        "Dil Diyan Gallan", "Main Hoon Na", "Tujhe Kitna Chahne Lage", "Tere Bina",
        "Tum Hi Ho Bandhu", "Dilbaro", "Khuda Jaane", "Tujh Mein Rab Dikhta Hai",
        "Main Agar Kahoon", "Bole Chudiyan", "Ghar More Pardesiya", "Tera Yaar Hoon Main",
        "Koi Mil Gaya", "Ae Mere Humsafar", "O Saathi", "Pal", "Zaalima", "Suno Ghar Ke",
        "Ye Sham Mastani", "Kabhi Kabhi Aditi", "Tum Jo Mil Gaye Ho", "Tera Mera Rishta",
        "Tu Jaane Na", "Pehla Nasha", "Dheere Dheere Se Meri Zindagi", "Kahin Door Jab Din",
        "Dil Se", "Agar Tum Saath Ho", "Tujhe Kitna Chahne Lage", "Moh Moh Ke Dhaage",
        "Mujhe Yaad Hai", "Kahin Toh Hogi Woh", "Tum Hi Aana", "Tu Hi Hai", "Tera Mera Rishta",
        "Tum Se Hi", "Jiyein Kyun", "O Saathi", "Teri Galliyan", "Kaise Hua", "Tumhare Hawaale",
        "Jeene Laga Hoon", "Jaane Dil Mein", "Main Rahoon Ya Na Rahoon", "Aankhon Ki Gustakhiyan",
        "Pyar Kiya To Darna Kya", "Dil Mein Chhupi Baat", "Jeene Laga Hoon", "Tum Jo Aaye",
        "Chura Liya Hai Tumne", "Pehla Nasha", "Tujhe Kitna Chahne Lage", "O Mere Dil Ke Chain",
        "Ghar Aaja Pardesi", "Dil Ke Armaan", "Pyaar Kiya To Darna Kya", "Ye Sham Mastani",
        "Dil Laga Liya Maine", "Khuda Jaane", "Tujhe Kitna Chahne Lage"
    ],
    "Sad": [
        "Channa Mereya", "Tujhe Kitna Chahne Lage", "Kabira", "Tum Hi Ho", "Dil Diyan Gallan",
        "Hasi", "Tadap Tadap", "Tera Yaar Hoon Main", "Agar Tum Saath Ho", "Phir Bhi Tumko Chaahunga",
        "Kabira", "Dil Mein Ho Tum", "Khuda Jaane", "Dard-E-Disco", "Mann Ki Manzil",
        "Gulon Mein Rang Bhare", "Jeene Laga Hoon", "Tanha Dil", "Mann Ki Manzil",
        "Dheere Dheere Se Meri Zindagi", "Tujhe Kitna Chahne Lage", "Ae Mere Humsafar",
        "Main Agar Kahoon", "Chhod Diya", "Bheegi Bheegi Raaton Mein", "Tumhare Hawaale",
        "Aankhon Ki Gustakhiyan", "Tum Se Hi", "Dard-E-Disco", "Phir Bhi Tumko Chaahunga",
        "Mujhe Yaad Hai", "Dil Se", "Pyar Kiya To Darna Kya", "Chura Liya Hai Tumne",
        "Tum Jo Aaye", "Yaad Hai Na", "Humsafar", "Pehli Nazar Mein", "Raabta",
        "Mere Rashke Qamar", "Kaise Hua", "Tera Ban Jaunga", "Gham Kya Hai",
        "Yaad Teri", "Tum Hi Ho Bandhu", "Jaane Dil Mein", "Bole Chudiyan", "Kabhi Kabhi Aditi",
        "Tera Mera Rishta", "Hasi Ban Gaye", "Ghar More Pardesiya", "Tujhe Kitna Chahne Lage",
        "Agar Tum Saath Ho", "Mann Ki Manzil", "Yaad Teri", "Kabir", "Dil Diyan Gallan"
    ],
    "Party": [
        "Despacito", "Badtameez Dil", "Uptown Funk", "Dilli Waali Girlfriend", "Kar Gayi Chull",
        "Lungi Dance", "London Thumakda", "Kala Chashma", "Saudagar Sauda Kar", "Mauja Hi Mauja",
        "Chaar Botal Vodka", "Pungi", "Balam Pichkari", "Baarish", "Aankh Marey",
        "Goli Maar Bheje Mein", "Bolo Ta Ra Ra", "Badtameez Dil", "Tum Hi Ho Bandhu",
        "Party All Night", "Chand Sifarish", "Pehla Nasha", "Duniya Haseeno Ka Mela",
        "Desi Girl", "Chikni Chameli", "Dilbar", "Genda Phool", "Malhari", "Baby Ko Bass Pasand Hai",
        "Ainvayi Ainvayi", "Bharat Ka Dum", "Zingaat", "Duniya Mein Aaye Ho", "Mera Wala Dance",
        "Oonchi Hai Building", "Main Tera Dushman", "Koi Kahe Kehta Rahe", "Ladki Beautiful",
        "Urvashi", "Gulaabo", "Besharam Rang", "Aankh Marey", "Pyaar Ki Pungi", "Bolo Ta Ra Ra",
        "Badal Pe Paon Hain", "Balam Pichkari", "Dilli Wali Girlfriend", "Zingaat",
        "Tum Hi Ho Bandhu", "Shaam Shaandaar", "Party in the USA", "Dilbaro"
    ],
    "Rock": [
        "Kahin Door Jab Din", "Tum Se Hi", "Pehla Nasha", "Dil Diyan Gallan", "Tera Ban Jaunga",
        "Khuda Jaane", "Raabta", "Kabira", "Tum Hi Ho", "Aankhon Ki Gustakhiyan",
        "Dil Se", "O Saathi", "Main Hoon Na", "Chura Liya Hai Tumne", "Kabhi Kabhi Aditi",
        "Bole Chudiyan", "Tum Jo Mil Gaye Ho", "Pal", "Koi Mil Gaya", "Tujhe Kitna Chahne Lage",
        "Ae Mere Humsafar", "Mere Rashke Qamar", "Mann Ki Manzil", "Hasi Ban Gaye",
        "Jeene Laga Hoon", "Tanha Dil", "Kabir", "Duniya Haseeno Ka Mela", "Kahin Toh Hogi Woh",
        "Raaz Aankhein", "Dil Mein Ho Tum", "Chhod Diya", "Aankhon Mein Basi Hai",
        "Dil Ki Baat", "Khuda Jaane", "Dil Bar Jaye", "Tumse Milke", "Dheere Dheere Se",
        "Baarish", "Tu Hi Hai", "Zindagi Ek Safar", "Main Agar Kahoon", "Tere Bina",
        "Besharam Rang", "Hasi", "Tum Jo Aaye", "Duniya Mein Aaye Ho", "Aankh Marey",
        "Pyar Kiya To Darna Kya", "Kabira", "Dil Diyan Gallan", "Tum Se Hi", "Kabhi Kabhi Aditi",
        "Mann Ki Manzil", "Dil Se", "Khuda Jaane", "Ae Mere Humsafar"
    ],
    "Pop": [
        "Lungi Dance", "Kala Chashma", "Dilbar", "Genda Phool", "Baby Ko Bass Pasand Hai",
        "Balam Pichkari", "Kar Gayi Chull", "Dilli Waali Girlfriend", "Saudagar Sauda Kar",
        "Aankh Marey", "Badshah", "Coka", "Pehla Nasha", "Bolo Ta Ra Ra", "Taki Taki",
        "Koi Kahe Kehta Rahe", "Tum Hi Ho Bandhu", "Chaar Botal Vodka", "Pyaar Ki Pungi",
        "Tumse Milke", "Tanha Dil", "Kabira", "Pyaar Kiya To Darna Kya", "Yaad Hai Na",
        "Kabhi Kabhi Aditi", "Besharam Rang", "O Saathi", "Jeene Laga Hoon", "Zingaat",
        "Tum Jo Aaye", "Dil Laga Liya Maine", "Dil Diyan Gallan", "Mann Ki Manzil",
        "Yaad Teri", "Chhod Diya", "Tumse Milke", "Dilbaro", "Jeene Laga Hoon",
        "Khuda Jaane", "Raabta", "Baarish", "Kahin Toh Hogi Woh", "Pyaar Kiya To Darna Kya",
        "Dil Laga Liya Maine", "O Saathi", "Tum Se Hi", "Tanha Dil", "Kabira", "Khuda Jaane",
        "Tum Jo Aaye", "Main Agar Kahoon", "Duniya Haseeno Ka Mela", "Mann Ki Manzil"
    ]
}

song_categories_english = {
    "Romantic": [
        "Perfect", "All of Me", "Thinking Out Loud", "Just the Way You Are", "I Will Always Love You",
        "A Thousand Years", "Can't Help Falling in Love", "My Heart Will Go On", "You're Still the One",
        "Unchained Melody", "At Last", "Something", "Wonderful Tonight", "Your Song", "Endless Love",
        "Kiss Me", "The Way You Look Tonight", "We Found Love", "Love Me Like You Do", "Adore You",
        "Bleeding Love", "Come Away With Me", "Hey There Delilah", "I Don't Want to Miss a Thing",
        "Truly Madly Deeply", "Time After Time", "You're Beautiful", "I Choose You", "Fallin'", "Love Story",
        "Back to You", "How Long Will I Love You", "Make You Feel My Love", "Chasing Cars", "Better Together",
        "The Best of Me", "I Knew I Loved You", "Is This Love", "You and Me", "Halo", "Always", "Everything",
        "Iris", "Stay with Me", "One Call Away", "When I Was Your Man", "You Make My Dreams", "Crazy for You",
        "You're the Inspiration", "In Your Eyes", "Say You Won't Let Go", "I Do", "I Finally Found Someone",
        "Love Is All Around", "From This Moment On", "You're Still the One", "Dancing on My Own",
        "Perfect Day", "I Want It That Way", "You and I", "We Belong Together", "The Look of Love"
    ],
    "Sad": [
        "Someone Like You", "Fix You", "The Night We Met", "Tears Dry on Their Own", "Hurt", "Someone You Loved",
        "Back to December", "The Reason", "Goodbye My Lover", "Let Her Go", "Chasing Cars", "I Will Always Love You",
        "When I Was Your Man", "Everybody Hurts", "Skinny Love", "Breathe Me", "My Immortal", "Fade Into You",
        "Tears in Heaven", "Creep", "I Don't Want to Talk About It", "Don't Speak", "All I Want", "Jar of Hearts",
        "Black and White", "Ain't No Sunshine", "Nothing Compares 2 U", "The Scientist", "Say Something",
        "Sitting on the Dock of the Bay", "I Will Remember You", "Angel", "Yesterday", "The Sound of Silence",
        "Nothing Else Matters", "Hallelujah", "Let It Be", "Here Without You", "Wherever You Will Go",
        "Goodbye", "It's So Hard to Say Goodbye to Yesterday", "Everybody's Changing", "I Will Follow You Into the Dark",
        "Home", "Long Gone", "Better Man", "Bleeding Out", "Somebody That I Used to Know", "The Night We Met",
        "Don't Let the Sun Go Down on Me", "Un-break My Heart", "Let Her Go", "Nothing Compares 2 U"
    ],
    "Party": [
        "Uptown Funk", "Shake It Off", "Can't Stop the Feeling!", "Despacito", "Get Lucky", "I Gotta Feeling",
        "Party in the USA", "Shape of You", "Blinding Lights", "24K Magic", "Shut Up and Dance", "Don't Start Now",
        "Dynamite", "Sucker", "Levitating", "Taki Taki", "Yeah!", "Hotline Bling", "Tik Tok", "Dancing Queen",
        "We Found Love", "Wake Me Up", "Dance Monkey", "Shallow", "Run the World (Girls)", "Single Ladies",
        "Crazy in Love", "Last Friday Night", "I Like It", "Rude", "Waka Waka (This Time for Africa)", "Ain't Nobody",
        "The Way You Make Me Feel", "Happy", "On The Floor", "Good Time", "We R Who We R", "Starships", 
        "Lights", "Something Just Like This", "Best Day of My Life", "Timber", "Cheap Thrills", "Let Me Love You",
        "My House", "Waves", "Show Me Love", "Don't Stop the Music", "Rockstar", "Savage Love", "Blow",
        "Colder Weather", "Shake It Off"
    ],
    "Rap": [
        "Godzilla", "Sicko Mode", "HUMBLE.", "Lose Yourself", "Juicy", "Mo Money Mo Problems", "Gold Digger",
        "N.Y. State of Mind", "In Da Club", "Alright", "Bodak Yellow", "Old Town Road", "Suge", "DNA.",
        "Started From the Bottom", "Rockstar", "RAPSTAR", "Goosebumps", "All of the Lights", "Nonstop",
        "Money Trees", "Hotline Bling", "The Box", "Without Me", "One Dance", "Love Sosa", "Trap Queen",
        "Glamorous", "What's My Name?", "Can't Tell Me Nothing", "Backseat Freestyle", "Humble", "Big Pimpin'",
        "Ambitionz Az a Ridah", "Run This Town", "Best I Ever Had", "Black and Yellow", "Sicko Mode", 
        "Bitch Don't Kill My Vibe", "I Like It", "Work It", "In Da Club", "Panda", "Get Ur Freak On", 
        "Fancy", "Finesse", "Hustlin'", "Jumpman", "Hotline Bling", "Look At Me!", "GOD.", "No Role Modelz",
        "All Eyez on Me", "Hypnotize", "Suge", "Truffle Butter"
    ],
    "Rock": [
        "Bohemian Rhapsody", "Hotel California", "Stairway to Heaven", "Back in Black", "Smoke on the Water",
        "Sweet Child o' Mine", "Wonderwall", "Billie Jean", "Every Breath You Take", "Born to Run", 
        "Livin' on a Prayer", "Hey Jude", "Black Dog", "Paint It Black", "More Than a Feeling", "Crazy Train",
        "You Shook Me All Night Long", "Hotel California", "Creep", "Sultans of Swing", "Welcome to the Jungle",
        "American Pie", "Paranoid", "Under Pressure", "Baba O'Riley", "Don't Stop Believin'", "Iron Man",
        "Jump", "Dream On", "Kashmir", "Zombie", "All Along the Watchtower", "Whole Lotta Love", 
        "Come Together", "Free Bird", "Brown Eyed Girl", "Roxanne", "November Rain", "Like a Rolling Stone", 
        "Sweet Home Alabama", "Take It Easy", "Tears in Heaven", "Black Hole Sun", "The Sound of Silence",
        "You Really Got Me", "Go Your Own Way", "Boulevard of Broken Dreams", "Enter Sandman", "Smells Like Teen Spirit"
    ]
}


# Main application window
class MusicAddaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Adda")
        self.root.geometry("700x600")
        self.root.config(bg="#1e1e1e")  # Dark background color

        # Frame for selecting language and category
        self.selection_frame = tk.Frame(root, bg="#1e1e1e")
        self.selection_frame.pack(pady=10)

        # Language selection
        self.language_label = tk.Label(self.selection_frame, text="Select Language:", font=("Segoe UI", 12), bg="#1e1e1e", fg="white")
        self.language_label.grid(row=0, column=0, padx=5)
        self.language_var = tk.StringVar(value='Hindi')  # Default to Hindi
        self.language_dropdown = ttk.Combobox(self.selection_frame, textvariable=self.language_var, font=("Segoe UI", 10), state="readonly")
        self.language_dropdown['values'] = ["Hindi", "English"]
        self.language_dropdown.grid(row=0, column=1, padx=5)

        # Category selection
        self.category_label = tk.Label(self.selection_frame, text="Select Category:", font=("Segoe UI", 12), bg="#1e1e1e", fg="white")
        self.category_label.grid(row=1, column=0, padx=5)
        self.category_var = tk.StringVar()
        self.category_dropdown = ttk.Combobox(self.selection_frame, textvariable=self.category_var, font=("Segoe UI", 10), state="readonly")
        self.category_dropdown['values'] = ["Romantic", "Sad", "Party", "Rock", "Pop"]
        self.category_dropdown.grid(row=1, column=1, padx=5)

        # Button to show songs
        self.show_songs_button = tk.Button(self.selection_frame, text="Show Songs", command=self.show_songs, font=("Segoe UI", 12, "bold"), bg="#007bff", fg="white", activebackground="#0056b3")
        self.show_songs_button.grid(row=2, columnspan=2, pady=10)

        # Listbox to display songs
        self.songs_listbox = tk.Listbox(root, width=70, height=15, font=("Segoe UI", 10), bg="#2e2e2e", fg="white", selectbackground="#555555")
        self.songs_listbox.pack(pady=10)

        # Button to play selected song
        self.play_button = tk.Button(root, text="Play Selected Song", command=self.play_song, font=("Segoe UI", 12, "bold"), bg="#28a745", fg="white", activebackground="#218838")
        self.play_button.pack(pady=5)

    def show_songs(self):
        # Clear previous songs from listbox
        self.songs_listbox.delete(0, tk.END)

        # Get selected language and category
        selected_language = self.language_var.get()
        selected_category = self.category_var.get()

        # Show songs based on selection
        if selected_language == 'Hindi':
            songs = song_categories_hindi.get(selected_category, [])
            for song in songs:
                self.songs_listbox.insert(tk.END, song)

        elif selected_language == 'English':
            songs = song_categories_english.get(selected_category, [])
            for song in songs:
                self.songs_listbox.insert(tk.END, song)

    def play_song(self):
        # Get selected song
        try:
            selected_song = self.songs_listbox.get(self.songs_listbox.curselection())
            webbrowser.open(f"https://open.spotify.com/search/{selected_song}")
        except tk.TclError:
            messagebox.showwarning("No Selection", "Please select a song to play.")

# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = MusicAddaApp(root)
    root.mainloop()