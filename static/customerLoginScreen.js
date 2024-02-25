function loginBtn(){
    if(document.getElementById("username").value==""){
        document.getElementById("user").textContent="Username Required";
    }else if(document.getElementById("username").value!=""){
        document.getElementById("user").textContent="";
    }

    if(document.getElementById("password").value==""){
        document.getElementById("pass").textContent="Password Required";
    }else if(document.getElementById("password").value!=""){
        document.getElementById("pass").textContent="";
    }


    /*if(document.getElementById("username").value!="" && document.getElementById("password").value!="" ){
        
        document.getElementById("welcomeUser").textContent=document.getElementById("username").value;
        document.getElementById("section3").style.display="none";
        document.getElementById("section4").style.display="block";
    }*/
}