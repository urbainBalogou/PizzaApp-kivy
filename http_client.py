import json

from kivy.network.urlrequest import UrlRequest


class HttpClient:
    def get_pizzas(self, on_complete, on_error):
        url = "http://127.0.0.1:8000/api/GetPizzas"

        def data_received(req, result):
           data = json.loads(result)
           pizzas_dict =[]
           for pizza in data:
               pizzas_dict.append(pizza["fields"])
           print("data_received")

           if on_complete:
                on_complete(pizzas_dict)

        def data_error(req, error):
            print("data error " + str(error))
            if on_error:
                on_error(str(error))

        def data_failure(req, error):
            print("data failure " + str(error))
            if on_error:
                on_error("Erreur serveur: " + str(req.resp_status))


        req = UrlRequest(url, on_success=data_received,on_error=data_error, on_failure=data_failure)
