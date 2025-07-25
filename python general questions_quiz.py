import tkinter as tk
from tkinter import messagebox

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["A. Wordsworth", "B. Jane Austen", "C. Shakespeare", "D. Dickens"],
        "answer": "C"
    },
    {
        "question": "Chemical symbol for water?",
        "options": ["A. CO2", "B. H2O", "C. O2", "D. NaCl"],
        "answer": "B"
    },
    {
        "question": "How many continents are there?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "question": "Which gas do plants absorb?",
        "options": ["A. Oxygen", "B. Carbon Monoxide", "C. CO2", "D. Nitrogen"],
        "answer": "C"
    },
    {
        "question": "Largest ocean?",
        "options": ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"],
        "answer": "D"
    },
    {
        "question": "Who invented the light bulb?",
        "options": ["A. Tesla", "B. Einstein", "C. Newton", "D. Edison"],
        "answer": "D"
    },
    {
        "question": "Smallest prime number?",
        "options": ["A. 0", "B. 1", "C. 2", "D. 3"],
        "answer": "C"
    },
    {
        "question": "India gained independence in?",
        "options": ["A. 1945", "B. 1947", "C. 1950", "D. 1952"],
        "answer": "B"
    }
]


current_q = 0
score = 0
timer = 90
timer_running = True

root = tk.Tk()
root.title("🧠 Python Quiz Game")
root.geometry("700x520")
root.configure(bg="#121212")

FONT_TITLE = ("Helvetica", 20, "bold")
FONT_QUESTION = ("Helvetica", 14)
FONT_INPUT = ("Helvetica", 12)
COLOR_BG = "#121212"
COLOR_LABEL = "#eaeaea"
COLOR_OPTION = "#a7c0f2"
COLOR_SUBMIT = "#4CAF50"
COLOR_NEXT = "#2196F3"
COLOR_ENTRY_BG = "#2d2d2d"
COLOR_ENTRY_FG = "#ffffff"


header = tk.Label(root, text="🔍 genral quetions quiz", font=FONT_TITLE, fg="#00e676", bg=COLOR_BG)
header.pack(pady=15)

score_label = tk.Label(root, text="Score: 0/10", font=("Helvetica", 12), fg="#f4f4f4", bg=COLOR_BG)
score_label.pack()


frame = tk.Frame(root, bg="#1e1e1e", padx=20, pady=15, bd=2, relief="ridge")
frame.pack(pady=15, padx=30, fill="both")

question_label = tk.Label(frame, text="", font=FONT_QUESTION, fg=COLOR_LABEL, bg=frame["bg"], wraplength=620, justify="left")
question_label.pack(pady=10)

options_list = []
for _ in range(4):
    lbl = tk.Label(frame, text="", font=FONT_QUESTION, fg=COLOR_OPTION, bg=frame["bg"], anchor="w")
    lbl.pack(anchor="w", pady=2)
    options_list.append(lbl)

entry_label = tk.Label(frame, text="Enter your answer (A/B/C/D):", font=FONT_INPUT, fg=COLOR_LABEL, bg=frame["bg"])
entry_label.pack(pady=(10, 2))

answer_entry = tk.Entry(frame, font=FONT_INPUT, bg=COLOR_ENTRY_BG, fg=COLOR_ENTRY_FG, insertbackground=COLOR_ENTRY_FG)
answer_entry.pack()

timer_label = tk.Label(root, text="⏳ Time Left: 90", font=FONT_INPUT, fg="#ff8a65", bg=COLOR_BG)
timer_label.pack(pady=10)


def show_question():
    global timer, timer_running
    answer_entry.delete(0, tk.END)
    timer = 90
    timer_running = True
    q = questions[current_q]
    question_label.config(text=f"Q{current_q + 1}: {q['question']}")
    for i in range(4):
        options_list[i].config(text=q["options"][i])
    update_timer()

def update_timer():
    global timer, timer_running
    if timer > 0 and timer_running:
        timer_label.config(text=f"⏳ Time Left: {timer} sec")
        timer -= 1
        root.after(1000, update_timer)
    elif timer == 0:
        messagebox.showinfo("⏰ Time's Up!", "You missed this question.")
        next_question()

def check_answer():
    global score, timer_running
    timer_running = False
    user_ans = answer_entry.get().strip().upper()
    correct_ans = questions[current_q]["answer"]
    if user_ans == correct_ans:
        score += 1
        messagebox.showinfo("✅ Correct!", "Good job!")
    else:
        messagebox.showinfo("❌ Wrong!", f"The correct answer was: {correct_ans}")
    score_label.config(text=f"Score: {score}/10")
    next_question()

def next_question():
    global current_q, timer_running
    timer_running = False
    current_q += 1
    if current_q >= len(questions):
        messagebox.showinfo("🎉 Quiz Completed", f"Your final score is: {score}/10")
        root.quit()
    else:
        show_question()


button_frame = tk.Frame(root, bg=COLOR_BG)
button_frame.pack(pady=10)

submit_btn = tk.Button(button_frame, text="Submit", command=check_answer,
                       bg=COLOR_SUBMIT, fg="white", font=FONT_INPUT, width=12)
submit_btn.grid(row=0, column=0, padx=10)

next_btn = tk.Button(button_frame, text="Next (Skip)", command=next_question,
                     bg=COLOR_NEXT, fg="white", font=FONT_INPUT, width=12)
next_btn.grid(row=0, column=1, padx=10)

footer = tk.Label(root, text="🎓 Created by Ritik Goyal - B.Tech IT, 2025", font=("Helvetica", 10), fg="#888", bg=COLOR_BG)
footer.pack(side="bottom", pady=10)

show_question()
root.mainloop()
       