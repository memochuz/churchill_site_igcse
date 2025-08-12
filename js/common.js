document.addEventListener("DOMContentLoaded", function() {
  'use strict';

  /* ==========================
  // Menu
  ========================== */

  // Menu Dragscroll
  !function(e,n){"function"==typeof define&&define.amd?define(["exports"],n):"undefined"!=typeof exports?n(exports):n(e.dragscroll={})}(this,(function(e){var n,t,o=window,l=document,c="mousemove",r="mouseup",i="mousedown",m="EventListener",d="add"+m,s="remove"+m,f=[],u=function(e,m){for(e=0;e<f.length;)(m=(m=f[e++]).container||m)[s](i,m.md,0),o[s](r,m.mu,0),o[s](c,m.mm,0);for(f=[].slice.call(l.getElementsByClassName("dragscroll")),e=0;e<f.length;)!function(e,m,s,f,u,a){(a=e.container||e)[d](i,a.md=function(n){e.hasAttribute("nochilddrag")&&l.elementFromPoint(n.pageX,n.pageY)!=a||(f=1,m=n.clientX,s=n.clientY,n.preventDefault())},0),o[d](r,a.mu=function(){f=0},0),o[d](c,a.mm=function(o){f&&((u=e.scroller||e).scrollLeft-=n=-m+(m=o.clientX),u.scrollTop-=t=-s+(s=o.clientY),e==l.body&&((u=l.documentElement).scrollLeft-=n,u.scrollTop-=t))},0)}(f[e++])};"complete"==l.readyState?u():o[d]("load",u,0),e.reset=u}));


  /* ==========================
  // Global Image Parallax
  ========================== */
  window.addEventListener('scroll', function() {
    var scroll = window.scrollTop || document.documentElement.scrollTop || document.body.scrollTop;
    var image = document.querySelector('.global-cover img');
    if (image) {
      image.style.transform = 'translate3d(0, ' + scroll / 3 + 'px, 0)';
    }
  });


  /* =======================
  // Responsive Videos
  ======================= */
  reframe(".post__content iframe:not(.reframe-off), .page__content iframe:not(.reframe-off)");


  /* =======================
  // LazyLoad Images
  ======================= */
  var lazyLoadInstance = new LazyLoad({
    elements_selector: ".lazy"
  })


  /* =======================
  // Zoom Image
  ======================= */
  const lightense = document.querySelector(".page__content img, .post__content img"),
  imageLink = document.querySelectorAll(".page__content a img, .post__content a img");

  if (imageLink) {
    for (var i = 0; i < imageLink.length; i++) imageLink[i].parentNode.classList.add("image-link");
    for (var i = 0; i < imageLink.length; i++) imageLink[i].classList.add("no-lightense");
  }

  if (lightense) {
    Lightense(".page__content img:not(.no-lightense), .post__content img:not(.no-lightense)", {
    padding: 60,
    offset: 30
    });
  }


  // =====================
  // Load More Posts
  // =====================
  var load_posts_button = document.querySelector('.load-more-posts');

  load_posts_button&&load_posts_button.addEventListener("click",function(e){e.preventDefault();var o=document.querySelector(".pagination"),e=pagination_next_url.split("/page")[0]+"/page/"+pagination_next_page_number+"/";fetch(e).then(function(e){if(e.ok)return e.text()}).then(function(e){var n=document.createElement("div");n.innerHTML=e;for(var t=document.querySelector(".grid"),a=n.querySelectorAll(".grid__post"),i=0;i<a.length;i++)t.appendChild(a.item(i));new LazyLoad({elements_selector:".lazy"});pagination_next_page_number++,pagination_next_page_number>pagination_available_pages_number&&(o.style.display="none")})});


  /* ============================
  // Testimonials Slider
  ============================ */
  const testimonialsSlider = document.querySelector(".testimonials__slider");

  if (testimonialsSlider) {
    new Splide(testimonialsSlider, {
      perPage: 2,
      perMove: 1,
      gap: 32,
      arrows: true,
      drag: true,
      pagination: false,
      type: 'loop',
      autoScroll: {
        autoStart: false,
        speed: 0.5,
        pauseOnHover: false,
        pauseOnFocus: false
      },
      intersection: {
        inView: {
          autoScroll: true,
        },
        outView: {
          autoScroll: false,
        },
      },
      breakpoints: {
        768: {
          perPage: 1
        },
        576: {
          drag: true,
        }
      }
    }).mount(window.splide.Extensions);
  }

 // ============================
  // Funciones y lógica para el menú de dificultad
  // ============================
  
  const difficultyButton = document.getElementById("difficultyButton");
  const dropdownList = document.getElementById("dropdownList");
  const exercisesContent = document.getElementById("exercises-content");
  
  if (difficultyButton && dropdownList) {
    // Escucha el clic del botón para mostrar/ocultar el menú
    difficultyButton.addEventListener("click", function() {
      dropdownList.classList.toggle("show");
    });
    
    // Escucha los clics en los enlaces del menú
    dropdownList.querySelectorAll("a").forEach(link => {
      link.addEventListener("click", async function(event) {
        event.preventDefault(); // Previene la navegación
        const filename = this.getAttribute("data-filename");
        
        try {
          const response = await fetch(filename);
          const markdown = await response.text();
          const htmlContent = marked.parse(markdown);
          exercisesContent.innerHTML = htmlContent;
        } catch (error) {
          console.error('Error al cargar el archivo:', error);
          exercisesContent.innerHTML = `<p style="color:red;">No se pudo cargar el contenido de ${filename}.</p>`;
        }
        dropdownList.classList.remove("show"); // Oculta el menú
      });
    });

    // Cierra el menú si se hace clic fuera de él
    window.addEventListener("click", function(event) {
      if (!event.target.matches('#difficultyButton')) {
        if (dropdownList.classList.contains('show')) {
          dropdownList.classList.remove('show');
        }
      }
    });
  }
  
  // ==============
  // Lógica para cargar ejercicios al hacer clic en las tarjetas
  // ==============
  const cardLinks = document.querySelectorAll('.card-link');
  
  if (cardLinks.length > 0) {
    cardLinks.forEach(card => {
      card.addEventListener('click', async function(event) {
        event.preventDefault(); // Evita la navegación por defecto

        const filename = this.getAttribute('href'); // Obtiene la URL del archivo
        const targetId = this.getAttribute('data-target'); // <-- Nuevo: Obtiene el ID del contenedor
        const exercisesContent = document.getElementById(targetId); // <-- Nuevo: Usa el ID dinámico
        
        try {
          const response = await fetch(filename);
          const markdown = await response.text();
          const htmlContent = marked.parse(markdown); // Convierte Markdown a HTML
          exercisesContent.innerHTML = htmlContent; // Inserta el HTML en el div

           if (typeof MathJax !== 'undefined') {
          MathJax.typesetPromise();
        }
        
        } catch (error) {
          console.error('Error al cargar el archivo:', error);
          exercisesContent.innerHTML = `<p style="color:red;">No se pudo cargar el contenido de ${filename}.</p>`;
        }
      });
    });
  }
});