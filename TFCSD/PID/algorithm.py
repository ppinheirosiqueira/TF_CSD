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

        system_pid_closed_loop = ctrl.feedback(self.Tf * pid_controller, self.feedback)

        # Obtendo a resposta ao degrau da malha fechada
        time_pid, response_pid = ctrl.step_response(system_pid_closed_loop)


        # Plotando a resposta ao degrau
        label_text = f'PID: Kp={self.Kp:.2f}, Ki={self.Ki:.2f}, Kd={self.Kd:.2f}'
        plt.plot(time_pid, response_pid,  label = label_text)
        plt.xlabel('Tempo')
        plt.ylabel('Resposta ao Degrau')
        plt.legend()
        plt.title('Resposta ao Degrau do Sistema no Tempo')
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

        system_pi_closed_loop = ctrl.feedback(self.Tf * pi_controller, self.feedback)

        # Obtendo a resposta ao degrau da malha fechada
        time_pi, response_pi = ctrl.step_response(system_pi_closed_loop)
        
        # Plotando a resposta ao degrau
        label_text = f'PI: Kp={self.Kp:.2f}, Ki={self.Ki:.2f}'
        plt.plot(time_pi, response_pi, label= label_text)
        plt.xlabel('Tempo')
        plt.ylabel('Resposta ao Degrau')
        plt.title('Resposta ao Degrau do Sistema no Tempo')
        plt.legend()
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

        system_pd_closed_loop = ctrl.feedback(self.Tf * pd_controller, self.feedback)

        # Obtendo a resposta ao degrau da malha fechada
        time_pd, response_pd = ctrl.step_response(system_pd_closed_loop)

        # Plotando a resposta ao degrau
        label_text = f'PD: Kp={self.Kp:.2f}, Kd={self.Kd:.2f}'
        plt.plot(time_pd, response_pd, label= label_text)
        plt.xlabel('Tempo')
        plt.ylabel('Resposta ao Degrau')
        plt.title('Resposta ao Degrau do Sistema no Tempo')
        plt.legend()
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

        system_p_closed_loop = ctrl.feedback(self.Tf * p_controller, self.feedback)

        # Obtendo a resposta ao degrau da malha fechada
        time_p, response_p = ctrl.step_response(system_p_closed_loop)

        # Plotando a resposta ao degrau
        label_text = f'P: Kp={self.Kp:.2f}'
        plt.plot(time_p, response_p, label= label_text)
        plt.xlabel('Tempo')
        plt.ylabel('Resposta ao Degrau')
        plt.title('Resposta ao Degrau do Sistema no Tempo')
        plt.legend()
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

        tf_closed_layer = ctrl.feedback(self.Tf, self.feedback)
        time_gp, response_gp = ctrl.step_response(tf_closed_layer)

        # Criando um vetor de tempo mais adequado
        label_text = f'TFMF: {self.Tf}'
        plt.plot(time_gp, response_gp, label=label_text)
        plt.xlabel('Tempo')
        plt.ylabel('Resposta ao Degrau')
        plt.title('Resposta ao Degrau do Sistema no Tempo')
        plt.legend()
        plt.grid(True)
        plt.show()

def fazerTF(numerador,denominador):
    return ctrl.tf(numerador, denominador)
