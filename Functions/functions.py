def python_food():
    width = 80
    text = "Spam and Eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)

def center_text(*args):
    text = ""
    for arg in args:
        text += str(arg) + " "
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text

# with open("centered", mode='w') as center_file:
with open("menu", mode='w') as menu:
    s1 = center_text("Spam and Eggs")
    print(s1, file=menu)
    s2 = center_text("Spam Spam and Eggs Eggs")
    print(s2, file=menu)
    s3 = center_text("Anand Kumar Jha Sonam Kumari Ananya Jha")
    print(s3, file=menu)
    s4 = center_text("First", "Second", 3, 4, "Five")
    print(s4, file=menu)