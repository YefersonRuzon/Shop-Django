document.addEventListener("keydown", (e)=> {
    if(e.target.matches(".search-filter")) {
        if(e.key === "Escape") e.target.value = ""
        const card = document.querySelectorAll(".cards");
        document.querySelectorAll(".cards").forEach((el) => {
            el.textContent.toLowerCase().includes(e.target.value)
              ? el.classList.remove("filter")
              : el.classList.add("filter")
        });
    }
  });
  
