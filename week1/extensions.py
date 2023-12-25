x = (input("File name: ")).lower().strip().split(".")
img = ["png", "gif"]
app = ["zip", "pdf"]
jpg = ["jpg", "jpeg"]

if x[-1] in app:
    #used the separator here to remove the default space added by python
    print("application/",x[-1], sep="")
elif x[-1] == "txt":
    print("text/plain")
elif x[-1] in jpg:
    print("image/jpeg")
elif x[-1] in img:
    #used the f statement here because it turns out it removes the default space already
    print(f"image/{x[-1]}")
else:
    print("application/octet-stream")
