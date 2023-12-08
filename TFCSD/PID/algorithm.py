import matplotlib.pyplot as plt
import control as ctrl

# PID controller class

class PID:
    def __init__(self, Kp: float, Ki: float, Kd: float, feedback: float, Tf: ctrl.tf):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.Tf = Tf
        self.feedback = feedback

    def plot_step_response(self):
        """"
        Ploting the step response of the PID controller
        """
        # Calculando a função de transferência da malha fechada com o controlador PID
        pid_controller = ctrl.TransferFunction([self.Kd, self.Kp, self.Ki], [1, 0])

        print(pid_controller)

        system_closed_loop = ctrl.feedback(self.Tf * pid_controller, self.feedback)

        # Obtendo a resposta ao degrau da malha fechada
        time, response = ctrl.step_response(system_closed_loop)

        # Plotando a resposta ao degrau
        plt.plot(time, response)
        plt.xlabel('Tempo')
        plt.ylabel('Resposta ao Degrau')
        plt.title('Resposta ao Degrau da Malha Fechada com PID')
        plt.grid(True)
        plt.show()





def main():
    dados_entrada = {
        'Kp': 1,
        'Ki': 1,
        'Kd': 1,
        'numerador': [1],
        'denominador': [1, 2, 1],
        'feedback': 1
    }

    Tf = ctrl.tf(dados_entrada['numerador'], dados_entrada['denominador'])

    pid = PID(
        Kp = dados_entrada['Kp'],
        Ki = dados_entrada['Ki'],
        Kd = dados_entrada['Kd'],
        feedback = dados_entrada['feedback'],
        Tf = Tf
    )

    pid.plot_step_response()

if __name__ == '__main__':
    main()
