from django.shortcuts import render
from . import algorithm
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
import asyncio
# Create your views here.

tf = {}
control = {}

def home(request):
    return HttpResponseRedirect(reverse("controlador",None,["nenhum",]))

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
    
    try:
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
        
        asyncio.run(controladorAtual.plot_step_response())
        data = {'status': "Sucesso"}
        return JsonResponse(data)
    except:
        data = {'status': "Falha"}
        return JsonResponse(data)
