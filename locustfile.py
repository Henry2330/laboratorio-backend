from locust import HttpUser, task, between
import random

class EvaluacionesUser(HttpUser):
    wait_time = between(1, 3) # Cada usuario espera entre 1 y 3 segundos entre tareas

    @task
    def evaluar_rechazo(self):
        edad = random.randint(0, 17)
        self.client.get("/evaluaciones/tarjetas", params=
            {"edad": edad,
             "ingresos": 500
             })
        
    # @task
    # def evaluar_tarjeta_normal(self):
    #     self.client.get("/evaluar", params=
    #         {"edad": 21,
    #          "ingresos": 2000
    #          })
        
    # @task
    # def evaluar_tarjeta_premium(self):
    #     self.client.get("/evaluar", params=
    #         {"edad": 30,
    #          "ingresos": 7500
    #          })
