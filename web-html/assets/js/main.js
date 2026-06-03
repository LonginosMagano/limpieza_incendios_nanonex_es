document.addEventListener("DOMContentLoaded",()=>{
  // Menú hamburguesa
  const h=document.querySelector(".hamburger"),n=document.querySelector(".nav");
  if(h&&n){h.addEventListener("click",()=>{n.classList.toggle("active");h.classList.toggle("active");});
    document.querySelectorAll(".nav-list a").forEach(l=>l.addEventListener("click",()=>{n.classList.remove("active");h.classList.remove("active");}));}
  // Scroll suave solo para anclas internas (no rompe navegación entre páginas)
  document.querySelectorAll('a[href^="#"]').forEach(a=>{
    a.addEventListener("click",function(e){const id=this.getAttribute("href");if(id.length>1){const t=document.querySelector(id);if(t){e.preventDefault();t.scrollIntoView({behavior:"smooth"});}}});
  });
  // Año dinámico
  const y=document.getElementById("currentYear");if(y)y.textContent=new Date().getFullYear();
  // Reveal al hacer scroll (umbral 0: aparece en cuanto entra, también en textos largos)
  const reveals=document.querySelectorAll(".reveal");
  const io=new IntersectionObserver((es,o)=>{es.forEach(en=>{if(en.isIntersecting){en.target.classList.add("active");o.unobserve(en.target);}});},{threshold:0,rootMargin:"0px 0px -40px 0px"});
  reveals.forEach(el=>io.observe(el));
  // Salvaguarda: a los 2.5s revela cualquier bloque que siga oculto
  setTimeout(()=>reveals.forEach(el=>el.classList.add("active")),2500);
  // Contadores
  const cw=new IntersectionObserver((es)=>{es.forEach(en=>{if(en.isIntersecting){en.target.querySelectorAll(".stat-number,.metric-number").forEach(c=>{const t=parseInt(c.getAttribute("data-counter"));let v=0;const inc=t/120;const up=()=>{if(v<t){v+=inc;c.textContent=Math.ceil(v);requestAnimationFrame(up);}else c.textContent=t;};up();});cw.unobserve(en.target);}});},{threshold:.4});
  document.querySelectorAll(".stats,.equipo-metrics").forEach(s=>cw.observe(s));
  // Banner de cookies: aparece si no se ha aceptado y se oculta al aceptar o al hacer scroll
  const cb=document.getElementById("cookie-banner");
  if(cb&&!localStorage.getItem("cookies-ok")){
    cb.hidden=false;
    const cerrar=()=>{localStorage.setItem("cookies-ok","1");cb.hidden=true;window.removeEventListener("scroll",onScroll);};
    const ok=document.getElementById("cookie-ok");if(ok)ok.addEventListener("click",cerrar);
    const onScroll=()=>{if(window.scrollY>60)cerrar();};
    window.addEventListener("scroll",onScroll,{passive:true});
  }
  // El formulario usa FormSubmit (POST nativo): no se intercepta.
});
