const policies = {
    GeneralInsurance: ["Janand", "BimaGold"],
    HealthInsurance: ["Vridhdhi", "ChildCareer"],
    MotorInsurance: ["Floater", "Conventional"]
  };
function firstDropdown(){
    const policyType = document.getElementById("title1").value;
    const policyTitleDropdown = document.getElementById("title2");
    policyTitleDropdown.innerHTML = '<option value="">Please Select</option>';
    policies[policyType].forEach(policy => {
    const option = document.createElement("option");
    option.value = policy;
    option.text = policy;
    option.id=policy;
    policyTitleDropdown.appendChild(option);
  });
}

function SecondDropdown(){
    if(document.getElementById("title2").value=="Janand"){
        document.getElementById("sumAssured").value=17000;
        document.getElementById("premAmount").value=10000;
        document.getElementById("policyTerm").value=10;
    }else if(document.getElementById("title2").value=="BimaGold"){
        document.getElementById("sumAssured").value=22080;
        document.getElementById("premAmount").value=12000;
        document.getElementById("policyTerm").value=12;
    }else if(document.getElementById("title2").value=="Vridhdhi"){
        document.getElementById("sumAssured").value=28700;
        document.getElementById("premAmount").value=14000;
        document.getElementById("policyTerm").value=15;
    }else if(document.getElementById("title2").value=="ChildCareer"){
        document.getElementById("sumAssured").value=34000;
        document.getElementById("premAmount").value=20000;
        document.getElementById("policyTerm").value=10;
    }else if(document.getElementById("title2").value=="Floater"){
        document.getElementById("sumAssured").value=20400;
        document.getElementById("premAmount").value=12000;
        document.getElementById("policyTerm").value=10;
    }else if(document.getElementById("title2").value=="Conventional"){
        document.getElementById("sumAssured").value=36000;
        document.getElementById("premAmount").value=15000;
        document.getElementById("policyTerm").value=20;
    }  
}

function func(){
    
    let premium=parseInt(document.getElementById("premAmount").value);
    let term=document.getElementById("policyTerm").value;
    if (document.getElementById("premAmount").value!="" && document.getElementById("sumAssured").value!=""){
        let sum=parseInt(premium*term*0.07);
        document.getElementById("sumAssured").value=premium+sum;
    }
}

function selectPolicyBtn(){
    if(document.getElementById("GeneralInsurance").selected==true){
        if(document.getElementById("Janand").selected==true || 
        document.getElementById("BimaGold").selected==true){
            if (document.getElementById("sumAssured").value!="" &&
            document.getElementById("premAmount").value!="" &&
            document.getElementById("policyTerm").value!=""){
                alert("Policy taken Successfully");
            }
        }
    }else if(document.getElementById("HealthInsurance").selected==true){
        if(document.getElementById("Vridhdhi").selected==true || 
        document.getElementById("ChildCareer").selected==true){
            if (document.getElementById("sumAssured").value!="" &&
            document.getElementById("premAmount").value!="" &&
            document.getElementById("policyTerm").value!=""){
                alert("Policy taken Successfully");
            }
        }
    }else if(document.getElementById("MotorInsurance").selected==true){
        if(document.getElementById("Floater").selected==true || 
        document.getElementById("Conventional").selected==true){
            if (document.getElementById("sumAssured").value!="" &&
            document.getElementById("premAmount").value!="" &&
            document.getElementById("policyTerm").value!=""){
                alert("Policy taken Successfully");
            }
        }
    }
}