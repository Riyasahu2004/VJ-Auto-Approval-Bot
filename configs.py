from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "22027848"))
    API_HASH = getenv("API_HASH", "38d38ac476379f7c0a60a1964ffe2eb3)
    BOT_TOKEN = getenv("BOT_TOKEN", "7184639056:AAELK02xUZeHYtR2pDX24MHp9mZqXc8BHzg")
    FSUB = getenv("FSUB", "")
    CHID = int(getenv("CHID", "-1001966682921"))
    SUDO = list(map(int, getenv("SUDO", "1750583099 827547960").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://vg766337:lOFhHGJF4vkSzaOY@cluster0.re8zmhy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

