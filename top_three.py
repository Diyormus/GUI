#  This is an individual assessment item for QUT's teaching unit
#  IFB104, "Building IT Systems", Semester 2, 2024.  By submitting
#  this code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#  Put your student number here as an integer and your name as a
#  character string:
#
student_number = 12155942
student_name = "Diyorbek Musaev"
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
# --------------------------------------------------------------------#


# -----Assessment Task 2 Description----------------------------------#
#
#  In this assessment task you will combine your knowledge of Python
#  programming, HTML-style mark-up languages, pattern matching,
#  database management, and Graphical User Interface design to produce
#  a robust, interactive "app" that allows its user to view and save
#  data from multiple online sources.
#
#  See the client's briefings accompanying this file for full
#  details.
#
#  Note that this assessable assignment is in multiple parts,
#  simulating incremental release of instructions by a paying
#  "client".  This single template file will be used for all parts,
#  together with some non-Python support files.
#
# --------------------------------------------------------------------#


# -----Set up---------------------------------------------------------#
#
# This section imports standard Python 3 modules sufficient to
# complete this assignment.  Don't change any of the code in this
# section, but you are free to import other Python 3 modules
# to support your solution, provided they are standard ones that
# are already supplied by default as part of a normal Python/IDLE
# installation.
#
# However, you may NOT use any Python modules that need to be
# downloaded and installed separately, such as "Beautiful Soup" or
# "Pillow", because the markers will not have access to such modules
# and will not be able to run your code.  Only modules that are part
# of a standard Python 3 installation may be used.

# A function for exiting the program immediately (renamed
# because "exit" is already a standard Python function).
from sys import exit as abort

# A function for opening a web document given its URL.
# [You WILL need to use this function in your solution,
# either directly or via the "download" function below.]
from urllib.request import urlopen

# Some standard Tkinter functions.  [You WILL need to use
# SOME of these functions in your solution.]  You may also
# import other widgets from the "tkinter" module, provided they
# are standard ones and don't need to be downloaded and installed
# separately.  (NB: Although you can import individual widgets
# from the "tkinter.tkk" module, DON'T import ALL of them
# using a "*" wildcard because the "tkinter.tkk" module
# includes alternative versions of standard widgets
# like "Label" which leads to confusion.  If you want to use
# a widget from the tkinter.ttk module name it explicitly,
# as is done below for the progress bar widget.)
from tkinter import *

# Functions for finding occurrences of a pattern defined
# via a regular expression.  [You do not necessarily need to
# use these functions in your solution, because the problem
# may be solvable with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.]

# A function for displaying a web document in the host
# operating system's default web browser (renamed to
# distinguish it from the built-in "open" function for
# opening local files).  [You WILL need to use this function
# in your solution.]


# All the standard SQLite database functions.  [You WILL need
# to use some of these in your solution.]

#
# --------------------------------------------------------------------#


# -----Validity Check-------------------------------------------------#
#
# This section confirms that the student has declared their
# authorship.  You must NOT change any of the code below.
#

if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer)\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string)\n')
    abort()


#
# --------------------------------------------------------------------#


# -----Supplied Function----------------------------------------------#
#
# Below is a function you can use in your solution if you find it
# helpful.  You are not required to use this function, but it may
# save you some effort.  Feel free to modify the function or copy
# parts of it into your own code.
#

# A function to download and save a web document.  The function
# returns the downloaded document as a character string and
# optionally saves it as a local file.  If the attempted download
# fails, an error message is written to the shell window and the
# special value None is returned.  However, the root cause of the
# problem is not always easy to diagnose, depending on the quality
# of the response returned by the web server, so the error
# messages generated by the function below are indicative only.
#
# Parameters:
# * url - The address of the web page you want to download.
# * target_filename - Name of the file to be saved (if any).
# * filename_extension - Extension for the target file, usually
#      "html" for an HTML document or "xhtml" for an XML
#      document.
# * save_file - A file is saved only if this is True. WARNING:
#      The function will silently overwrite the target file
#      if it already exists!
# * char_set - The character set used by the web page, which is
#      usually Unicode UTF-8, although some web pages use other
#      character sets.
# * incognito - If this parameter is True the Python program will
#      try to hide its identity from the web server. This can
#      sometimes be used to prevent the server from blocking access
#      to Python programs. However, we discourage using this
#      option as it is both unreliable and unethical to
#      override the wishes of the web document provider!
#
def download(url='http://www.wikipedia.org/',
             target_filename='downloaded_document',
             filename_extension='html',
             save_file=True,
             char_set='UTF-8',
             incognito=False):
    # Import the function for opening online documents and
    # the class for creating requests
    from urllib.request import urlopen, Request

    # Import an exception sometimes raised when a web server
    # denies access to a document
    from urllib.error import HTTPError

    # Import an exception raised when a web document cannot
    # be downloaded due to some communication error
    from urllib.error import URLError

    # Open the web document for reading (and make a "best
    # guess" about why if the attempt fails, which may or
    # may not be the correct explanation depending on how
    # well-behaved the web server is!)
    try:
        if incognito:
            # Pretend to be a web browser instead of
            # a Python script (not recommended!)
            request = Request(url)
            request.add_header('User-Agent',
                               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; ' + \
                               'rv:91.0; ADSSO) Gecko/20100101 Firefox/91.0')
            print("Warning - Request to server does not reveal client's true identity.")
            print("          Use this option only if absolutely necessary!\n")
        else:
            # Behave ethically
            request = url
        web_page = urlopen(request)
    except ValueError as message:  # probably a syntax error
        print(f"\nCannot find requested document '{url}'")
        print(f"Error message was: {message}\n")
        return None
    except HTTPError as message:  # possibly an authorisation problem
        print(f"\nAccess denied to document at URL '{url}'")
        print(f"Error message was: {message}\n")
        return None
    except URLError as message:  # probably the wrong server address
        print(f"\nCannot access web server at URL '{url}'")
        print(f"Error message was: {message}\n")
        return None
    except Exception as message:  # something entirely unexpected
        print("\nSomething went wrong when trying to download " + \
              f"the document at URL '{str(url)}'")
        print(f"Error message was: {message}\n")
        return None

    # Read the contents as a character string
    try:
        web_page_contents = web_page.read().decode(char_set)
    except UnicodeDecodeError as message:
        print("\nUnable to decode document from URL " + \
              f"'{url}' as '{char_set}' characters")
        print(f"Error message was: {message}\n")
        return None
    except Exception as message:
        print("\nSomething went wrong when trying to decode " + \
              f"the document from URL '{url}'")
        print(f"Error message was: {message}\n")
        return None

    # Optionally write the contents to a local text file
    # (silently overwriting the file if it already exists!)
    if save_file:
        try:
            text_file = open(f'{target_filename}.{filename_extension}',
                             'w', encoding=char_set)
            text_file.write(web_page_contents)
            text_file.close()
        except Exception as message:
            print(f"\nUnable to write to file '{target_filename}'")
            print(f"Error message was: {message}\n")

    # Return the downloaded document to the caller
    return web_page_contents


#
# --------------------------------------------------------------------#


# -----Student's Solution---------------------------------------------#
import ssl
import urllib.request
import re
import webbrowser
import sqlite3
import html

# Avoid certificate verification error
ssl._create_default_https_context = ssl._create_unverified_context

# URLs for data scraping
top_rating_iTunes_html = "http://www.itunescharts.net/aus/charts/tv-episodes/2024/09/26"
most_pirated_movies_html = "https://torrentfreak.com/top-10-most-torrented-pirated-movies/"
top_selling_songs_html = "https://www.officialcharts.com/charts/singles-chart/"


# Function to initialize the SQLite database
def init_db():
    conn = sqlite3.connect('media_rankings.db')  # Connect to the database (it will be created if it doesn't exist)
    cursor = conn.cursor()
    # Create a table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS winners (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data_source TEXT,
        ranking INTEGER,
        identifier TEXT,
        property TEXT
    )
    ''')
    conn.commit()
    cursor.close()
    conn.close()


# Scraping functions
def scrape_itunes_top_episodes():
    try:
        with urllib.request.urlopen(top_rating_iTunes_html) as response:
            html_content = response.read().decode('utf-8')

        # Regular expression to match top 3 TV episodes
        pattern = re.compile(
            r'<li id="chart_aus_tv-episodes_\d+".*?no-move.*?<span class="artist">(.*?)</span>.*?<span class="entry">.*?">(.*?)</a>',
            re.DOTALL)
        matches = pattern.findall(html_content)

        top_three = matches[:3] if matches else []
        if top_three:
            # html.unescaped for correct decoding and displaying data
            return "\n".join(f"{ranking_number + 1}. {html.unescape(artist)} - {html.unescape(episode)}" for
                             ranking_number, (artist, episode) in
                             enumerate(top_three))
        else:
            return "No TV episodes found."
    except Exception as e:
        return f"Error retrieving iTunes data: {e}"


# Function to scrape most-pirated movies
def scrape_most_pirated_movies():
    try:
        # Create a request with a user agent to mimic a browser
        request = urllib.request.Request(most_pirated_movies_html, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(request) as response:
            html_content = response.read().decode('utf-8')

        # Regular expression to match rank, title, and IMDb rating
        pattern = re.compile(
            r'<tr>\s*<td><strong>(\d+)</strong></td>\s*<td>\(.*?\)</td>\s*<td>(.*?)</td>\s*<td><a href=".*?">(\d+\.\d+)</a>',
            re.DOTALL)
        matches = pattern.findall(html_content)

        top_three = matches[:3] if matches else []
        # html.unescaped for correct decoding and displaying data
        if top_three:
            return "\n".join(
                f"{html.unescape(rank)}. {html.unescape(title)} - IMDb Rating: {html.unescape(rating)}" for
                rank, title, rating in top_three)
        else:
            return "No movies found."
    except Exception as e:
        return f"Error retrieving pirated movies data: {e}"


# Function to scrape top-selling songs
def scrape_top_selling_songs():
    try:
        with urllib.request.urlopen(top_selling_songs_html) as response:
            html_content = response.read().decode('utf-8')

        # Regular expression to match rank, song title, and artist
        pattern = re.compile(
            r'<div class="position">.*?<strong>(\d+)</strong>.*?'
            r'<a href=".*?" class="chart-name font-bold inline-block">.*?<span>(.*?)</span>.*?'
            r'<a href=".*?" class="chart-artist text-lg inline-block"><span>(.*?)</span>',
            re.DOTALL
        )
        matches = pattern.findall(html_content)

        top_three = matches[:3] if matches else []
        if top_three:
            # Format titles to capitalize only the first letter of each word
            formatted_results = []
            for rank, song, artist in top_three:
                formatted_song = ' '.join(word.capitalize() for word in song.split())
                # html.unescaped for correct decoding and displaying data
                formatted_results.append(
                    f"{html.unescape(rank)}. {html.unescape(formatted_song)} ({html.unescape(artist)})")
            return "\n".join(formatted_results)
        else:
            return "No songs found."
    except Exception as e:
        return f"Error retrieving songs data: {e}"


# Function to open the URL when clicking "Show Data Source"
def open_data_source(url):
    webbrowser.open(url)


# Function to update the message box based on selection
def update_dashboard(message=""):
    message_label.config(text=message)


# Create the main window
main_window = Tk()
main_window.title('Media Rankings Dashboard')
window_font = ('Helvetica', 10)

# Load the background image
background_image = PhotoImage(file="podium.png")  # Replace with the correct image path
canvas = Canvas(main_window, width=background_image.width(), height=background_image.height())
canvas.grid(row=0, column=0, rowspan=5, columnspan=5)
canvas.create_image(0, 0, image=background_image, anchor="nw")

# Frame for buttons and other widgets
frame = Frame(main_window)
frame.grid(row=0, column=0, rowspan=4, columnspan=4)

# Shared variable for the radio buttons
ranking_choice = IntVar()

# Box for ranking radio buttons
ranking_buttons = LabelFrame(frame, relief='groove', font=window_font, borderwidth=2, text='Choose and view a ranking')
ranking_buttons.grid(pady=5, row=1, column=0)

# Radio buttons for different data-sources
itunes_top_episodes_button = Radiobutton(ranking_buttons, text='Top-Rating iTunes TV Episodes', variable=ranking_choice,
                                         value=1, font=window_font)
itunes_top_episodes_button.grid(sticky='w')

pirated_movies_button = Radiobutton(ranking_buttons, text='Most-Pirated Online Movies', variable=ranking_choice,
                                    value=2, font=window_font)
pirated_movies_button.grid(sticky='w')

top_songs_button = Radiobutton(ranking_buttons, text='Top-Selling Pop Songs in the UK', variable=ranking_choice,
                               value=3, font=window_font)
top_songs_button.grid(sticky='w')

# Box for message display
message_label_frame = LabelFrame(frame, relief="groove", font=window_font, borderwidth=2, text='Message Box')
message_label_frame.grid(pady=5, row=2, column=0, columnspan=2)

# Label for displaying messages
message_label = Label(message_label_frame, text="", font=window_font, anchor="w", justify="left", width=50)
message_label.grid(padx=10, pady=10)

# Button to show top 3
top_three_button = Button(ranking_buttons, text='Show top three', width=10, font=window_font,
                          command=lambda: show_top_three())
top_three_button.grid(pady=5, row=3, column=0)

# Button to show data source
data_source_button = Button(ranking_buttons, text='Show data source', width=10, font=window_font,
                            command=lambda: show_data_source())
data_source_button.grid(pady=5, row=3, column=1)

# Box for winner radial buttons
winner_buttons = LabelFrame(frame, relief='groove', font=window_font,
                            borderwidth=2, text='Save a winner')
winner_buttons.grid(pady=5, row=1, column=1)


# Functions to handle button actions
def show_top_three():
    choice = ranking_choice.get()
    if choice == 1:
        update_dashboard(scrape_itunes_top_episodes())
    elif choice == 2:
        update_dashboard(scrape_most_pirated_movies())
    elif choice == 3:
        update_dashboard(scrape_top_selling_songs())


# Function for redirecting to data source
def show_data_source():
    choice = ranking_choice.get()
    if choice == 1:
        open_data_source(top_rating_iTunes_html)
    elif choice == 2:
        open_data_source(most_pirated_movies_html)
    elif choice == 3:
        open_data_source(top_selling_songs_html)


# Save winner function in sql database
def save_winner(data_source, ranking, identifier, property_info):
    conn = sqlite3.connect('media_rankings.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO winners (data_source, ranking, identifier, property)
    VALUES (?, ?, ?, ?)
    ''', (data_source, ranking, identifier, property_info))
    conn.commit()
    conn.close()


def save_gold_winner():
    choice = ranking_choice.get()
    data_source = ""
    ranking = 0
    identifier = ""
    property_info = ""

    if choice == 1:  # Top-Rating iTunes TV Episodes
        data_source = "Top-Rating iTunes"
        top_episodes = scrape_itunes_top_episodes()
        if top_episodes:
            ranking = 1  # Always saving as 1 for Gold
            lines = top_episodes.splitlines()
            identifier = lines[0].split(" - ")[0]  # Extracting the show name
            property_info = lines[0].split(" - ")[1]  # Extracting the episode title


    elif choice == 2:  # Most-Pirated Online Movies
        data_source = "Most-Pirated"
        top_movies = scrape_most_pirated_movies()
        if top_movies:
            ranking = 1
            lines = top_movies.splitlines()
            identifier = lines[0].split(" - ")[0]  # Extracting the title
            property_info = f"{lines[0].split(' - ')[1].split(': ')[1]}"  # Extract the rating

    elif choice == 3:  # Top-Selling Pop Songs in the UK
        data_source = "Top-Selling"
        top_songs = scrape_top_selling_songs()
        if top_songs:
            ranking = 1
            lines = top_songs.splitlines()
            identifier = lines[0].split(" (")[0]  # Extracting the song title
            property_info = lines[0].split(" (")[1].rstrip(')')  # Extracting the artist name

    if identifier:  # If we have a valid identifier, save it to the database
        save_winner(data_source, ranking, identifier, property_info)
        update_dashboard(f"Gold winner saved: {identifier} from {data_source}. Database successfully updated.")
    else:
        update_dashboard("No winner to save.")


# Similarly modify save_silver_winner and save_bronze_winner
def save_silver_winner():
    choice = ranking_choice.get()
    data_source = ""
    ranking = 0
    identifier = ""
    property_info = ""

    if choice == 1:  # Top-Rating iTunes TV Episodes
        data_source = "Top-Rating iTunes"
        top_episodes = scrape_itunes_top_episodes()
        if top_episodes:
            ranking = 2
            lines = top_episodes.splitlines()
            identifier = lines[1].split(" - ")[0]  # Extracting the show name
            property_info = lines[1].split(" - ")[1]  # Extracting the episode title


    elif choice == 2:  # Most-Pirated Online Movies
        data_source = "Most-Pirated"
        top_movies = scrape_most_pirated_movies()
        if top_movies:
            ranking = 2
            lines = top_movies.splitlines()
            identifier = lines[1].split(" - ")[0]
            property_info = f"{lines[1].split(' - ')[1].split(': ')[1]}"

    elif choice == 3:  # Top-Selling Pop Songs in the UK
        data_source = "Top-Selling"
        top_songs = scrape_top_selling_songs()
        if top_songs:
            ranking = 2
            lines = top_songs.splitlines()
            identifier = lines[1].split(" (")[0]
            property_info = lines[1].split(" (")[1].rstrip(')')  # Extracting the artist name

    if identifier:
        save_winner(data_source, ranking, identifier, property_info)
        update_dashboard(f"Silver winner saved: {identifier} from {data_source}. Database successfully updated.")
    else:
        update_dashboard("No winner to save.")


def save_bronze_winner():
    choice = ranking_choice.get()
    data_source = ""
    ranking = 0
    identifier = ""
    property_info = ""

    if choice == 1:  # Top-Rating iTunes TV Episodes
        data_source = "Top-Rating iTunes"
        top_episodes = scrape_itunes_top_episodes()
        if top_episodes:
            ranking = 3
            lines = top_episodes.splitlines()
            identifier = lines[2].split(" - ")[0]  # Extracting the show name
            property_info = lines[2].split(" - ")[1]  # Extracting the episode title


    elif choice == 2:  # Most-Pirated Online Movies
        data_source = "Most-Pirated"
        top_movies = scrape_most_pirated_movies()
        if top_movies:
            ranking = 3
            lines = top_movies.splitlines()
            identifier = lines[2].split(" - ")[0]
            property_info = f"{lines[2].split(' - ')[1].split(': ')[1]}"

    elif choice == 3:  # Top-Selling Pop Songs in the UK
        data_source = "Top-Selling"
        top_songs = scrape_top_selling_songs()
        if top_songs:
            ranking = 3
            lines = top_songs.splitlines()
            identifier = lines[2].split(" (")[0]
            property_info = lines[2].split(" (")[1].rstrip(')')  # Extracting the artist name

    if identifier:
        save_winner(data_source, ranking, identifier, property_info)
        update_dashboard(f"Bronze winner saved: {identifier} from {data_source}. Database successfully updated.")
    else:
        update_dashboard("No winner to save.")


# Button to save gold winner
gold_winner_button = Button(winner_buttons, text='Gold',
                            width=5, font=window_font,
                            command=lambda: save_gold_winner())
gold_winner_button.grid(sticky='w')

# Button to save silver winner
silver_winner_button = Button(winner_buttons, text='Silver',
                              width=5, font=window_font,
                              command=lambda: save_silver_winner())
silver_winner_button.grid(sticky='w')

# Button to save bronze winner
bronze_winner_button = Button(winner_buttons, text='Bronze',
                              width=5, font=window_font,
                              command=lambda: save_bronze_winner())
bronze_winner_button.grid(sticky='w')

# Call the init_db function to set up the database
init_db()

# Start the main loop
main_window.mainloop()
