
# untracked

# git config --global user.email "you@example.com"
# git config --global user.name "Your Name"

# git config --global user.email "matteo.massa@studenti.isissgobetti.it"
# git config --global user.name "Matteo Massa"

# python -m venv .venv

# read file
file_path = "password_super_segrete.txt"
with open(file_path, "r") as file:
    password = file.read()
    print(password)