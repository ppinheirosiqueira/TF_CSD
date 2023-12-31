function enviarTF(){
    var num = document.getElementById("num").value
    var den = document.getElementById("den").value

    if (num == "" || den == "" || den == "0"){
        alert("Não é possível um numerador/denominador zerado, por favor, adicione-os no bloco G")
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
        if (kp == '' || kp == 0){
            alert("Não é possível um controlador proporcional com ganho Kp zerado")
            return
        }
    }
    else if (tipo == "pi"){
        kp = document.getElementById("kp").value
        ki = document.getElementById("ki").value
        kd = 0
        if (kp == '' || ki == "" || kp == 0 || ki == 0){
            alert("Não é possível um controlador PI com ganho Kp ou Ki zerado")
            return
        }
    }
    else if (tipo == "pd"){
        kp = document.getElementById("kp").value
        ki = 0 
        kd = document.getElementById("kd").value
        if (kp == '' || kd == "" || kp == 0 || kd == 0){
            alert("Não é possível um controlador PD com ganho Kp ou Kd zerado")
            return
        }
    }
    else if (tipo == "pid"){
        kp = document.getElementById("kp").value
        ki = document.getElementById("ki").value
        kd = document.getElementById("kd").value
        if (kp == '' || kd == '' || ki == '' || kp == 0 || ki == 0 || kd == 0){
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