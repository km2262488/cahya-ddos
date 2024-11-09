import os

print("""[0] pip\n[1] pip3\nWhich one do you use?""")

c = input(">>>: ")
if c == "0":
     os.system("pip install requests")
     os.system("pip install setuptool")
     os.system("pip install wheel")
elif c == "1":
     os.system("pip install requests")
     os.system("pip install setuptool")
     os.system("pip install wheel")
     print("Done.")
