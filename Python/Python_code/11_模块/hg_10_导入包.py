import hg_massge

hg_massge.send_massage.send("hello")
txt = hg_massge.receive_massage.receive()
print(txt)