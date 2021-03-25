
let my_form={};
let url_post="http://127.0.0.1:8000/contacts";
document.getElementById("registration").addEventListener("submit",function(e){
    e.preventDefault();
    my_form["firstname"]=document.getElementById("first_name").value;
    my_form["lastname"]=document.getElementById("last_name").value; 
    my_form["birthday"]=document.getElementById("birthday").value; 
    my_form["phone"]=document.getElementById("phone").value; 
    my_form["email"]=document.getElementById("email").value; 
    console.log(my_form);
    let data=JSON.stringify(my_form)
    console.log(data);
    fetch(url_post,{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
            
        },
        body:data
    })
    .then((response)=>{
        if(response.ok) console.log("Contact crée");
        let ma_div = document.querySelector('.sign_in');
        let text = '<h3>Votre contact a été ajouté </h3><a href="index.html" class="btn-return">retour</a>';
        ma_div.innerHTML = text;
    })
})
