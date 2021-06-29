class MobileNavbar{
	constructor(mobileMenu, navList, navLinks){
		this.mobileMenu = document.querySelector(mobileMenu);
		this.navList = document.querySelector(navList);
		this.navLinks = document.querySelectorAll(navLinks);
	}

	mobileMenuClickEvent(){
		if(this.mobileMenu){
			this.mobileMenu.addEventListener("click", () => this.navList.classList.toggle("active"));
		}
		else{
			console.log("mobileMenu não encontrado");
		}
	}
}

const mobileNavbar = new MobileNavbar(".mobile-menu", ".nav-list", ".nav-list li");
mobileNavbar.mobileMenuClickEvent();
