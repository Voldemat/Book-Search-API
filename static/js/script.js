document.querySelectorAll(".book-card__submit").forEach(element => {
      element.addEventListener("click", handleClick);
})
function handleClick(e){
      e.preventDefault()
      if (e.target.getAttribute("data-access") != "True"){
            alert("Требуется авторизация!");
      }
      else{
            e.target.form.submit()
      }
}