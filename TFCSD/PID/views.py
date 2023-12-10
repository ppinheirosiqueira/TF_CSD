from django.shortcuts import render
from . import algorithm

# Create your views here.

tf = {}
control = {}

def home(request):
    variavel = False
    return render(request, "PID/home.html", {"variavel": variavel,})

def controlador(request, nome):
    return render(request, "PID/controlador.html", {"nome": nome, "tf" : tf, "controlador": control,})

def atualizarTF(request, num, den, tipo, kp, ki, kd):
    tf.update({'num': num})
    tf.update({'den': den})
    num = list(map(int, num.replace(',', ' ').split()))
    den = list(map(int, den.replace(',', ' ').split()))
    control.update({'kp' : kp})
    control.update({'ki' : ki})
    control.update({'kd' : kd})
    
    Tf = algorithm.fazerTF(num,den)

    if tipo == "nenhum":
        controladorAtual = algorithm.GpNoControlAction(1,Tf)
    elif tipo == "p":
        controladorAtual = algorithm.P(float(kp),1,Tf)
    elif tipo == "pi":
        controladorAtual = algorithm.PI(float(kp),float(ki),1,Tf)
    elif tipo == "pd":
        controladorAtual = algorithm.PD(float(kp),float(kd),1,Tf)
    else:
        controladorAtual = algorithm.PID(float(kp),float(ki),float(kd),1,Tf)
    
    controladorAtual.plot_step_response()
    return render(request, "PID/controlador.html", {"nome": num,})
