import json

class KurzusFajlKezelo:
    ut = "kurzusok.json"
    #ut = "kurzus_proba.json"

    def kurzusok_olvasas(self):
        try:
            with open(self.ut, "r") as be:
                kurzusok = json.load(be)
        except FileNotFoundError:
            return []
        print(kurzusok)
        return kurzusok

    def kurzusok_iras(self, kurzusok):
        with open(self.ut, "w") as ki:
            json.dump(kurzusok, ki, indent=4)
