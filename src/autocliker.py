import pyautogui
import appJar

def buttonPress(button):
    if(button == "Go"):
        amount = int(app.getEntry("amount"))
        button = app.radioButton("click")
        if(button == "Right Clicl"):
            button = "right"
        else:
            button = "left"
        for _ in range(amount):
            pyautogui.click(button=button)

app = appJar.gui("autoclicker")
app.setSize("300x200")
app.setSticky("new")
app.addLabel("Add meg a klikkek számát", row=0)
app.addEntry("amount", row=1)
app.addButton("Inditás", buttonPress,row=3)
app.setSticky("e")
app.radioButton("click", "Jobb Click", row=2)
app.setSticky("w")
app.radioButton("click", "Bal Click", row=2)

app.go()