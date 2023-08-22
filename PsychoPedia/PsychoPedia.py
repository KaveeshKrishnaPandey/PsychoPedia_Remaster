import os
import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
from tkinter import scrolledtext, Menu
import webbrowser
import pygame

# Set the working directory
os.chdir("D:/ABHI/Programming/PsychoPedia (Remaster)/App")

# Initialize pygame
pygame.mixer.init()

# Read Deases Text Files
with open("..\\Articles\\Depression.txt") as f:
    depression_article = f.read()

with open("..\\Articles\\Anxiety.txt") as f:
    anxiety_article = f.read()

with open("..\\Articles\\Bipolar Disorder.txt") as f:
    bipolar_disorder_article = f.read()

with open("..\\Articles\\Schizophrenia.txt") as f:
    schizophrenia_article = f.read()

with open("..\\Articles\\OCD.txt") as f:
    ocd_article = f.read()

with open("..\\Articles\\PTSD.txt") as f:
    ptsd_article = f.read()

with open("..\\Articles\\Eating Disorders.txt") as f:
    eating_disorder_article = f.read()
    
with open("..\\Articles\\ADHD.txt") as f:
    adhd_article = f.read()

with open("..\\Articles\\ASD.txt") as f:
    asd_article = f.read()

with open("..\\Articles\\BPD.txt") as f:
    bpd_article = f.read()

# Read Motivation TXT File
with open("..\\Motivation\\Motivation.txt") as f:
    motivation_quote = f.read()

motivation_textbox = None

# Define a list of widgets that should not be destroyed during theme updates
widgets_to_skip = []

def show_motivation_article():
    motivation_window = tk.Toplevel(root)
    motivation_window.title("Motivation")
    motivation_window.configure(bg=bg_color)
    motivation_window.minsize(800, 600)
    motivation_window.geometry("800x600")

    motivation_text = motivation_quote

    motivation_textbox = scrolledtext.ScrolledText(motivation_window, wrap=tk.WORD, font=("Helvetica", 12), bg=button_color, fg=text_color)
    motivation_textbox.insert(tk.END, motivation_text)
    motivation_textbox.config(state='disabled')  # Set the state to 'disabled' to prevent editing
    motivation_textbox.pack(fill='both', expand=True, padx=10, pady=10)

def show_motivation():
    global motivation_textbox
    clear_motivation()  # Clear any existing motivation content

    content_label.config(text="")
    content_label.pack(fill='both', expand=True)
    content_label.update_idletasks()

    motivation_text = motivation_quote

    motivation_textbox = tk.Label(content_label, wraplength=800, text=motivation_text, justify='center', anchor='center', font=("Helvetica", 14), bg=bg_color, fg=text_color)
    motivation_textbox.pack(pady=150, fill='x')
    clear_disease_buttons()

    # Append motivation_textbox to the list of widgets to skip
    widgets_to_skip.append(motivation_textbox)

    # Create the "Get Motivated!!" button and style it similarly to the disease buttons
    get_motivated_button = tk.Button(content_label, text="Get Motivated!!", command=get_motivated, relief="ridge", borderwidth=3, bd=0, highlightthickness=0, padx=10, pady=5, bg=button_color, fg=text_color, font=("Helvetica", 13), width=50, height=2)
    get_motivated_button.pack(pady=10, anchor='center')
    disease_buttons.append(get_motivated_button)  # Add the button to the list of disease buttons for consistent styling

    # Create the "Relaxin Music" button and style it similarly to the disease buttons
    relaxing_music_button = tk.Button(content_label, text="Relaxing Music", command=relaxing_music, relief="ridge", borderwidth=3, bd=0, highlightthickness=0, padx=10, pady=5, bg=button_color, fg=text_color, font=("Helvetica", 13), width=50, height=2)
    relaxing_music_button.pack(pady=10, anchor='center')
    disease_buttons.append(relaxing_music_button)  # Add the button to the list of disease buttons for consistent styling

    # Create the "Pause Music" button and style it similarly to the disease buttons
    pause_music_button = tk.Button(content_label, text="Pause Music", command=pause_music, relief="ridge", borderwidth=3, bd=0, highlightthickness=0, padx=10, pady=5, bg=button_color, fg=text_color, font=("Helvetica", 13), width=50, height=2)
    pause_music_button.pack(pady=10, anchor='center')
    disease_buttons.append(pause_music_button)  # Add the button to the list of disease buttons for consistent styling

    # Create the "Browse Music!!" button and style it similarly to the disease buttons
    brows_music_button = tk.Button(content_label, text="Browse Music!!", command=browse_music, relief="ridge", borderwidth=3, bd=0, highlightthickness=0, padx=10, pady=5, bg=button_color, fg=text_color, font=("Helvetica", 13), width=50, height=2)
    brows_music_button.pack(pady=10, anchor='center')
    disease_buttons.append(brows_music_button)  # Add the button to the list of disease buttons for consistent styling

# Function to create the browse music window
def browse_music():
    browse_music_window = tk.Toplevel(root)
    browse_music_window.title("Browse Music")
    browse_music_window.configure(bg=bg_color)
    browse_music_window.minsize(800, 600)
    browse_music_window.geometry("800x600")

    music_buttons_frame = tk.Frame(browse_music_window, bg=bg_color)
    music_buttons_frame.pack(fill='both', expand=True, padx=10, pady=10)

    # Create a 2-column grid of music buttons
    num_columns = 2
    for i in range(10):
        row = i // num_columns
        col = i % num_columns
        music_button = tk.Button(music_buttons_frame, text=f"Music {i + 1}", command=lambda idx=i: play_music(idx), relief="ridge", borderwidth=3, bd=0, highlightthickness=0, padx=10, pady=5, bg=button_color, fg=text_color, font=("Helvetica", 13), width=50, height=2)
        music_button.grid(row=row, column=col, padx=10, pady=10)

    # Center-align the music buttons in the frame
    for i in range(len(music_buttons_frame.winfo_children())):
        music_buttons_frame.grid_rowconfigure(i, weight=1)
        music_buttons_frame.grid_columnconfigure(i % num_columns, weight=1)

    # Create the "Pause Music" button and center-align it
    pause_music_button = tk.Button(browse_music_window, text="Pause Music", command=pause_music, relief="ridge", borderwidth=3, bd=0, highlightthickness=0, padx=10, pady=5, bg=button_color, fg=text_color, font=("Helvetica", 13), width=50, height=2)
    pause_music_button.pack(pady=10, anchor='center')

# List of music tracks (file paths)
music_tracks = [
    "path_to_music_1.mp3",
    "path_to_music_2.mp3",
    "path_to_music_3.mp3",
    "path_to_music_4.mp3",
    "path_to_music_5.mp3",
    "path_to_music_6.mp3",
    "path_to_music_7.mp3",
    "path_to_music_8.mp3",
    "path_to_music_9.mp3",
    "path_to_music_10.mp3",
]

def play_music(track_idx):
    global is_music_playing
    is_music_playing = True
    audio_path = music_tracks[track_idx]
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

def relaxing_music():
    # Load and play the audio file
    global is_music_playing
    is_music_playing = True  # Add this global variable to track music playback
    audio_path = "..\\Motivation\\Relaxing Music.mp3"  # Replace with the actual file path
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

def pause_music():
    global is_music_playing
    if is_music_playing:
        pygame.mixer.music.pause()
        is_music_playing = False

def clear_motivation():
    for widget in content_label.winfo_children():
        widget.destroy()

def get_motivated():
    webbrowser.open("https://www.youtube.com/watch?v=Mye7bTaoUxo")

# Create a function to toggle between light and dark mode
def toggle_theme():
    global bg_color, button_color, text_color
    if bg_color == "#181818":
        bg_color = "white"
        button_color = "#DDDDDD"
        text_color = "black"
    else:
        bg_color = "#181818"
        button_color = "#272727"
        text_color = "white"
    update_theme()  # Call the function to update the theme colors

# Create a function to update the theme across all widgets
def update_theme():
    root.configure(bg=bg_color)
    content_frame.configure(bg=bg_color)
    content_label.configure(bg=bg_color, fg=text_color)
    button_frame.configure(bg=bg_color)
    for button in disease_buttons:
        button.configure(bg=button_color, fg=text_color)
    for widget in root.winfo_children():
        if isinstance(widget, tk.Toplevel):
            widget.configure(bg=bg_color)
            for sub_widget in widget.winfo_children():
                sub_widget.configure(bg=bg_color)
                if isinstance(sub_widget, scrolledtext.ScrolledText) and sub_widget not in widgets_to_skip:
                    sub_widget.configure(bg=button_color, fg=text_color)
        elif isinstance(widget, tk.Button):
            widget.configure(bg=button_color, fg=text_color)

# Create the main application window
root = tk.Tk()
root.title("PsychoPedia")
root.iconbitmap("..\\Icons\\icon.ico")
root.configure(bg="#181818")  # Set background color
root.minsize(1376,741)
root.geometry("1376x741")

# Define dark color scheme
bg_color = "#181818"
button_color = "#272727"
text_color = "white"
accent_color = "#5294E2"

# Create a menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Create a theme menu
theme_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Theme", menu=theme_menu)
theme_menu.add_command(label="Dark Mode", command=toggle_theme)
theme_menu.add_command(label="Light Mode", command=toggle_theme)

# Function to open different app sections
def open_section(section_title):
    clear_motivation()  # Clear motivation content
    if section_title == "News":
        show_sample_news()
    elif section_title == "Articles":
        show_mental_health_diseases()
    elif section_title == "Motivation":  # Add this condition
        show_motivation()
    else:
        content_label.config(text=f"Content for {section_title} goes here...")
        clear_disease_buttons()


def show_sample_news():
    content_label.config(text="Mental Health News:\n")
    sample_news = [
        "New Study Reveals Link Between Exercise and Mental Well-being",
        "Tips for Managing Stress and Anxiety in Daily Life",
        "Community Event: Mental Health Awareness Workshop",
        "Interview with Expert: Understanding the Importance of Self-Care",
        "Personal Story: Overcoming Depression and Finding Hope"
    ]
    for news_item in sample_news:
        content_label.config(text=content_label.cget("text") + f"\n- {news_item}")
    clear_disease_buttons()

def show_mental_health_diseases():
    content_label.config(text="Select a mental health disease:", font=("Helvetica", 14))
    for disease in mental_health_diseases:
        disease_button = tk.Button(content_frame, text=disease, command=lambda d=disease: open_disease_article(d), relief="ridge", borderwidth=3, bd=0, highlightthickness=0, padx=10, pady=5, bg=button_color, fg=text_color, font=("Helvetica", 13), width=50, height=2)
        disease_button.pack(pady=5, anchor='center')
        disease_buttons.append(disease_button)

def clear_disease_buttons():
    for button in disease_buttons:
        button.destroy()
    disease_buttons.clear()

def open_disease_article(disease):
    article_text = articles.get(disease, "No article available for this disease.")
    show_article_window(disease, article_text)


def show_article_window(disease, article_text):
    article_window = tk.Toplevel(root)
    article_window.title(f"{disease} Article")
    article_window.configure(bg=bg_color)
    article_window.minsize(1376,741)
    article_window.geometry("1376x741")

    article_label = tk.Label(article_window, text="Article about {}:".format(disease), font=("Helvetica", 14), bg=bg_color, fg=text_color)
    article_label.pack(pady=10)

    article_textbox = scrolledtext.ScrolledText(article_window, wrap=tk.WORD, font=("Helvetica", 12), bg=button_color, fg=text_color)
    article_textbox.insert(tk.END, article_text)
    article_textbox.config(state='disabled')  # Set the state to 'disabled' to prevent editing
    article_textbox.pack(fill='both', expand=True, padx=10, pady=10)

# Load and resize the images
article_button_img = ImageTk.PhotoImage(Image.open("..\\Icons\\article.png").resize((100, 100), Image.ANTIALIAS))
news_button_img = ImageTk.PhotoImage(Image.open("..\\Icons\\news.png").resize((100, 100), Image.ANTIALIAS))
motivation_button_img = ImageTk.PhotoImage(Image.open("..\\Icons\\motivation.png").resize((100, 100), Image.ANTIALIAS))
kyd_button_img = ImageTk.PhotoImage(Image.open("..\\Icons\\kyd.png").resize((100, 100), Image.ANTIALIAS))
medication_button_img = ImageTk.PhotoImage(Image.open("..\\Icons\\medication.png").resize((100, 100), Image.ANTIALIAS))

# Create a frame to hold the buttons
button_frame = tk.Frame(root, borderwidth=2, relief="ridge", bg=bg_color)
button_frame.grid(row=0, column=0, padx=20, pady=20)

# Create buttons to access different app sections
sections = [
    ("Articles", article_button_img),
    ("News", news_button_img),
    ("Motivation", motivation_button_img),
    ("Know Your Disease", kyd_button_img),
    ("Medication", medication_button_img)
]

for row, (section_title, image) in enumerate(sections):
    section_button = tk.Button(button_frame, image=image, text=section_title, compound='top', command=lambda title=section_title: open_section(title), relief="ridge", borderwidth=3, bd=0, highlightthickness=0, bg=button_color, fg=text_color)
    section_button.image = image
    section_button.grid(row=row, column=0, padx=10, pady=10, sticky='w')

# Create a frame to hold the content
content_frame = tk.Frame(root, borderwidth=2, relief="ridge", bg=bg_color)
content_frame.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')

# Configure grid weights to make the label expand vertically and the content frame expand horizontally
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
content_frame.grid_columnconfigure(0, weight=1)

# Create a label to display content
content_label = tk.Label(content_frame, text="Select a section to view its content...", justify='center', anchor='center', font=("Helvetica", 12), bg=bg_color, fg=text_color)
content_label.pack(fill='both', expand=True)

# List of mental health diseases
mental_health_diseases = [
    "Depression",
    "Anxiety",
    "Bipolar Disorder",
    "Schizophrenia",
    "Obsessive-Compulsive Disorder (OCD)",
    "Post-Traumatic Stress Disorder (PTSD)",
    "Eating Disorders",
    "Attention-Deficit/Hyperactivity Disorder (ADHD)",
    "Autism Spectrum Disorder",
    "Borderline Personality Disorder"
]

# Dictionary to store articles for each mental health disease
articles = {
    "Depression": depression_article,
    "Anxiety": anxiety_article,
    "Bipolar Disorder": bipolar_disorder_article,
    "Schizophrenia": schizophrenia_article,
    "Obsessive-Compulsive Disorder (OCD)": ocd_article,
    "Post-Traumatic Stress Disorder (PTSD)": ptsd_article,
    "Eating Disorders": eating_disorder_article,
    "Attention-Deficit/Hyperactivity Disorder (ADHD)": adhd_article,
    "Autism Spectrum Disorder": asd_article,
    "Borderline Personality Disorder": bpd_article
}

# List to store disease buttons
disease_buttons = []

# def size():
#     width = root.winfo_width()
#     height = root.winfo_height()
#     print(f"Window size: {width}x{height}")

# f1 = tk.Frame(root)
# f1.grid()

# b1 = tk.Button(f1, text="size", command=size)
# b1.grid()

# Start the main event loop
root.mainloop()