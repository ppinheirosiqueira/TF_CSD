function enviarTF(){
    var num = document.getElementById("num").value
    var den = document.getElementById("den").value

    if (num == ""){
        alert("Não é possível um numerador zerado")
        return
    }

    if (den == ""){
        alert("Não é possível um denominador zerado")
        return
    }

    var url = window.location.href
    var partes = url.split('/')
    var tipo = partes.pop()

    if (tipo == "nenhum"){
        kp = 0
        ki = 0 
        kd = 0
    }
    else if (tipo == "p"){
        kp = document.getElementById("kp").value
        ki = 0 
        kd = 0
        if (kp == ''){
            alert("Não é possível um controlador proporcional com ganho Kp zerado")
            return
        }
    }
    else if (tipo == "pi"){
        kp = document.getElementById("kp").value
        ki = document.getElementById("ki").value
        kd = 0
        if (kp == '' || ki == ""){
            alert("Não é possível um controlador PI com ganho Kp ou Ki zerado")
            return
        }
    }
    else if (tipo == "pd"){
        kp = document.getElementById("kp").value
        ki = 0 
        kd = document.getElementById("kd").value
        if (kp == '' || kd == ""){
            alert("Não é possível um controlador PD com ganho Kp ou Kd zerado")
            return
        }
    }
    else if (tipo == "pid"){
        kp = document.getElementById("kp").value
        ki = document.getElementById("ki").value
        kd = document.getElementById("kd").value
        if (kp == '' || kd == '' || ki == ''){
            alert("Não é possível um controlador PID com ganho Kp, Ki ou Kd zerado")
            return
        }
    }

    fetch('../atualizarTF/' + num + '/' + den + '/' + tipo + '/' + kp.toString() + '/' + ki.toString()  + '/' + kd.toString() )
    .then(function(response) {
        return response.json();
    })
    .then(function(data){
        if (data['status'] !== "Sucesso") {
            alert("Alguma coisa infelizmente deu errado")
            return
        }
    })
    .catch(function(error) {
        console.log('Ocorreu um erro:', error);
    })

}