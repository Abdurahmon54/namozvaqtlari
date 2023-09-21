from requests import get, post

class PrayRequests:
    def __init__(self, reg:str) -> None:
        self.__reg_id = {"Toshkent": 1,
            "Namangan": 149,
            "Farg'ona": 77,
            "Qo'qon":78,
            "Andijon": 17,
            "Samarqand": 47,
            "Buxoro": 34,
            "Sirdaryo": 73,
            "Navoiy": 136,
            "Jizzax": 107,
            "Qashqadaryo": 121,
            "Xorazm": 101,
            "Surxandaryo": 122,
            "Qora qalpog'iston Respublikasi": 176}
        self.__city = reg
        self.__content = ""
        self.__url = "https://praytime.uz/"
    def requests(self):
        try:
            id = 1
            if self.__city in self.__reg_id.keys():
                id = self.__reg_id[self.__city]
            body = {
                "region_id":id
            }
            res = get(self.__url, params = body)
            if res.status_code == 200:
                self.__content = res.text
            else:
                raise Exception(f"Surov yuborilgandan keyin xatolig vujudga keldi: {res.status_code}")
        except Exception as e:
            print(e)
    @property
    def Content(self):
        return self.__content
