from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "10471716"))
    API_HASH = getenv("API_HASH", "f8a1b21a13af154596e2ff5bed164860")
    BOT_TOKEN = getenv("BOT_TOKEN", "7240311570:AAEzQj2J_sQq7cIPyuGZxIMHpnTANYd37GM")
    FSUB = getenv("FSUB", "Chinese_Korean_Drama_Hindii")
    CHID = int(getenv("CHID", "-1001966682921"))
    SUDO = list(map(int, getenv("SUDO", "6883997969 5460214165").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://appuz:chrijismiappuz@cluster0.yngvhc2.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
