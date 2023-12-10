import matplotlib.pyplot as plt
import control as ctrl
import plotly.offline as plot

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
        pid_controller = ctrl.TransferFunction([self.Kp, self.Ki, self.Kd], [0, 1, 0])

        print("Gp: ", self.Tf)
        print("Ação PID: ", pid_controller)

        system_pid_closed_loop = ctrl.feedback(self.Tf * pid_controller, self.feedback)

        # Obtendo a resposta ao degrau da malha fechada
        time_pid, response_pid = ctrl.step_response(system_pid_closed_loop)

        # Plotando a resposta ao degrau
        plt.plot(time_pid, response_pid)
        plt.xlabel('Tempo')
        plt.ylabel('Resposta ao Degrau')
        plt.title('Resposta ao Degrau da Malha Fechada com PID')
        plt.grid(True)
        plt.show()

class PI:
    def __init__(self, Kp: float, Ki: float, feedback: float, Tf: ctrl.tf):
        self.Kp = Kp
        self.Ki = Ki
        self.Tf = Tf
        self.feedback = feedback

    def plot_step_response(self):
        """"
        Ploting the step response of the PI controller
        """
        # Calculando a função de transferência da malha fechada com o controlador PI
        pi_controller = ctrl.TransferFunction([self.Kp, self.Ki], [1, 0])

        print("Gp: ", self.Tf)
        print("Ação PI: ", pi_controller)

        system_pi_closed_loop = ctrl.feedback(self.Tf * pi_controller, self.feedback)

        # Obtendo a resposta ao degrau da malha fechada
        time_pi, response_pi = ctrl.step_response(system_pi_closed_loop)

        # Plotando a resposta ao degrau
        plt.plot(time_pi, response_pi)
        plt.xlabel('Tempo')
        plt.ylabel('Resposta ao Degrau')
        plt.title('Resposta ao Degrau da Malha Fechada com PI')
        plt.grid(True)
        plt.show()

class PD:
    def __init__(self, Kp: float, Kd: float, feedback: float, Tf: ctrl.tf):
        self.Kp = Kp
        self.Kd = Kd
        self.Tf = Tf
        self.feedback = feedback

    def plot_step_response(self):
        """"
        Ploting the step response of the PI controller
        """
        # Calculando a função de transferência da malha fechada com o controlador PD
        pd_controller = ctrl.TransferFunction([self.Kd, self.Kp], [0, 1])

        print("Gp: ", self.Tf)
        print("Ação PD: ", pd_controller)

        system_pd_closed_loop = ctrl.feedback(self.Tf * pd_controller, self.feedback)

        # Obtendo a resposta ao degrau da malha fechada
        time_pd, response_pd = ctrl.step_response(system_pd_closed_loop)

        # Plotando a resposta ao degrau
        plt.plot(time_pd, response_pd)
        plt.xlabel('Tempo')
        plt.ylabel('Resposta ao Degrau')
        plt.title('Resposta ao Degrau da Malha Fechada com PD')
        plt.grid(True)
        plt.show()

class P:
    def __init__(self, Kp: float, feedback: float, Tf: ctrl.tf):
        self.Kp = Kp
        self.Tf = Tf
        self.feedback = feedback

    def plot_step_response(self):
        """"
        Ploting the step response of the PI controller
        """
        # Calculando a função de transferência da malha fechada com o controlador P
        p_controller = ctrl.TransferFunction([self.Kp], [1])

        print("Gp: ", self.Tf)
        print("Ação P: ", p_controller)

        system_p_closed_loop = ctrl.feedback(self.Tf * p_controller, self.feedback)

        # Obtendo a resposta ao degrau da malha fechada
        time_p, response_p = ctrl.step_response(system_p_closed_loop)

        # Plotando a resposta ao degrau
        plt.plot(time_p, response_p)
        plt.xlabel('Tempo')
        plt.ylabel('Resposta ao Degrau')
        plt.title('Resposta ao Degrau da Malha Fechada com P')
        plt.grid(True)
        plt.show()

class GpNoControlAction:
    def __init__(self, feedback: float, Tf: ctrl.tf):
        self.Tf = Tf
        self.feedback = feedback

    def plot_step_response(self):
        """"
        Ploting the step response of the PI controller
        """

        print("Gp: ", self.Tf)

        tf_closed_layer = ctrl.feedback(self.Tf, self.feedback)
        time_gp, response_gp = ctrl.step_response(tf_closed_layer)

        # Criando um vetor de tempo mais adequado
        plt.plot(time_gp, response_gp)
        plt.xlabel('Tempo')
        plt.ylabel('Resposta ao Degrau')
        plt.title('Resposta ao Degrau da Gp em Malha Fechada sem Ação de Controle')
        plt.grid(True)
        plt.show()

def fazerTF(numerador,denominador):
    return ctrl.tf(numerador, denominador)

# def main():
#     dados_entrada = {
#         'Kp': 1,
#         'Ki': 1,
#         'Kd': 1,
#         'numerador': [1],
#         'denominador': [1, 2, 1],
#         'feedback': 1
#     }

#     Tf = ctrl.tf(dados_entrada['numerador'], dados_entrada['denominador'])

#     pid = PID(
#         Kp = dados_entrada['Kp'],
#         Ki = dados_entrada['Ki'],
#         Kd = dados_entrada['Kd'],
#         feedback = dados_entrada['feedback'],
#         Tf = Tf
#     )

#     pi = PI(
#         Kp = dados_entrada['Kp'],
#         Ki = dados_entrada['Ki'],
#         feedback = dados_entrada['feedback'],
#         Tf = Tf
#     )

#     pd = PD(
#         Kp = dados_entrada['Kp'],
#         Kd = dados_entrada['Kd'],
#         feedback = dados_entrada['feedback'],
#         Tf = Tf
#     )

#     p = P(
#         Kp = dados_entrada['Kp'],
#         feedback = dados_entrada['feedback'],
#         Tf = Tf
#     )

#     tfmf = GpNoControlAction(
#         feedback = dados_entrada['feedback'],
#         Tf = Tf
#     )

#     tfmf.plot_step_response()
#     p.plot_step_response()
#     pi.plot_step_response()
#     pd.plot_step_response()
#     pid.plot_step_response()

# if __name__ == '__main__':
#     main()
