function GRI(){
    var customer_id = math.floor(1000000 + Math.random() * 9000000);
    document.getElementById("customerId").value = customer_id;
      }
    function resgisterBtn(){
      if (document.getElementById("name").value==""){
        document.getElementById("nam").textContent="name is required"
      }else if (document.getElementById("name").value!=""){
        document.getElementById("nam").textContent=""
      }

      if (document.getElementById("email").value==""){
        document.getElementById("mail").textContent="email is required"
      }else if (document.getElementById("email").value!=""){
        document.getElementById("mail").textContent=""
      }

      if (document.getElementById("password").value==""){
        document.getElementById("pass").textContent="password is required"
      }else if (document.getElementById("password").value!=""){
        document.getElementById("pass").textContent=""
      }

      if (document.getElementById("address").value==""){
        document.getElementById("add").textContent="address is required"
      }else if (document.getElementById("address").value!=""){
        document.getElementById("add").textContent=""
      }

      if (document.getElementById("contact").value==""){
        document.getElementById("cont").textContent="contact no is required"
      }else if (document.getElementById("contact").value!=""){
        document.getElementById("cont").textContent=""
      }

      if (document.getElementById("nomineename").value==""){
        document.getElementById("nominame").textContent="nominee name is required"
      }else if (document.getElementById("nomineename").value!=""){
        document.getElementById("nominame").textContent=""
      }

       var cid=document.querySelector("#customerId").value;
       var cname=document.querySelector("#name").value;
       var em=document.querySelector("#email").value;
       var ob={
           cid,
           cname,
           em
       }
       console.log(ob);
       localStorage.setItem("ob",JSON.stringify(ob));
   }