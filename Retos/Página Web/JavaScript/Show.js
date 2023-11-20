const show = document.getElementById("show"),
	  icon = document.querySelector(".M");
icon.addEventListener("click", e =>{
	if (show.type == "password"){
		show.type = "text";
		icon.classList.remove('fa-solid fa-eye-slash')
		icon.classList.add('fa-solid fa-eye')
	} else{
		show.type = "password"
	} 
})