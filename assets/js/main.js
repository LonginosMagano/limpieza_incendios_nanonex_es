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
  // Reveal al hacer scroll
  const io=new IntersectionObserver((es,o)=>{es.forEach(en=>{if(en.isIntersecting){en.target.classList.add("active");o.unobserve(en.target);}});},{threshold:.1});
  document.querySelectorAll(".reveal").forEach(el=>io.observe(el));
  // Contadores
  const cw=new IntersectionObserver((es)=>{es.forEach(en=>{if(en.isIntersecting){en.target.querySelectorAll(".stat-number,.metric-number").forEach(c=>{const t=parseInt(c.getAttribute("data-counter"));let v=0;const inc=t/120;const up=()=>{if(v<t){v+=inc;c.textContent=Math.ceil(v);requestAnimationFrame(up);}else c.textContent=t;};up();});cw.unobserve(en.target);}});},{threshold:.6});
  document.querySelectorAll(".stats,.equipo-metrics").forEach(s=>cw.observe(s));
  // Banner de cookies
  const cb=document.getElementById("cookie-banner");
  if(cb&&!localStorage.getItem("cookies-ok")){cb.hidden=false;
    const ok=document.getElementById("cookie-ok");if(ok)ok.addEventListener("click",()=>{localStorage.setItem("cookies-ok","1");cb.hidden=true;});}
  // El formulario usa FormSubmit (POST nativo): no se intercepta.
});
