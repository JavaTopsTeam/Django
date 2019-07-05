<script> 
function GEEKFORGEEKS()                                    
{ 
    var name = document.forms["RegForm"]["name"];               
    var email = document.forms["RegForm"]["email"];    
    var password = document.forms["RegForm"]["password"];  
    var c_pass =  document.forms["RegForm"]["confirmpassword"];  
    var address = document.forms["RegForm"]["address"];  
    var contno = document.forms["RegForm"]["contno"]; 
     var gender = document.forms["RegForm"]["gender"]; 
     var city= document.forms["RegForm"]["city"];
     var state = document.forms["RegForm"]["state"];
     var country = document.forms["RegForm"]["country"];
   
    if (name.value == "")                                  
    { 
        window.alert("Please enter your name."); 
        name.focus(); 
        return false; 
    } 
   
    if (address.value == "")                               
    { 
        window.alert("Please enter your address."); 
        address.focus(); 
        return false; 
    } 
       
    if (email.value == "")                                   
    { 
        window.alert("Please enter a valid e-mail address."); 
        email.focus(); 
        return false; 
    } 
   
    if (email.value.indexOf("@", 0) < 0)                 
    { 
        window.alert("Please enter a valid e-mail address."); 
        email.focus(); 
        return false; 
    } 
   
    if (email.value.indexOf(".", 0) < 0)                 
    { 
        window.alert("Please enter a valid e-mail address."); 
        email.focus(); 
        return false; 
    } 
   
    if (contno.value == "")                           
    { 
        window.alert("Please enter your contact number."); 
        contno.focus(); 
        return false; 
    } 
   
    if (password.value == "")                        
    { 
        window.alert("Please enter your password"); 
        password.focus(); 
        return false; 
    } 

    if (c_pass.value == "")                        
    { 
        window.alert("Please enter your confrim password"); 
        c_pass.focus(); 
        return false; 
    } 
   
    if (city.selectedIndex < 1)                  
    { 
        alert("Please select your city"); 
        city.focus(); 
        return false; 
    } 
    if (state.selectedIndex < 1)                  
    { 
        alert("Please select your state"); 
        state.focus(); 
        return false; 
    } 
    if (country.selectedIndex < 1)                  
    { 
        alert("Please select your country"); 
        country.focus(); 
        return false; 
    } 
   
    return true; 
}</script>