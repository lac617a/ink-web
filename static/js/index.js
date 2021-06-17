document.addEventListener('DOMContentLoaded',()=>{
  btnHambuerger();
  let scrollPos = 0;
  const _BROWSERWIDTH = window.innerWidth;
  const _BROWSERHEIGHT = window.innerHeight;
  
  nav_flost(scrollPos,_BROWSERWIDTH);
  // renderSeeker()


  // Scroll actual
  document.body.onscroll = ()=>{
    const winY = window.pageYOffset;
    scroll_up(winY,_BROWSERHEIGHT);
    asidebar(winY,_BROWSERWIDTH)
    if(document.getElementById('content-first')){
      loadVideo(winY,_BROWSERHEIGHT);
      formarDateWhatsapp();
    };
    navbar(winY,_BROWSERWIDTH);
  }
})

function asidebar(winY,wid){
  const aside = document.querySelector('.sidebar-categories')
  if(winY > 0 && wid > 768){
    aside.classList.add('is_active')
  }else{aside.classList.remove('is_active')}
}

const btn = document.querySelectorAll('.wrapper-header-res ._private')
btn.forEach(item =>{
  item.addEventListener('click',()=>{
    const search = document.querySelector('.search')
    const navbar = document.querySelector('.wrapper-nav-bar')
    if(item.classList.item(0) == 'seeker'){
      search.classList.toggle('active')
      navbar.classList.remove('active')
    }else{
      navbar.classList.toggle('active')
      search.classList.remove('active')
    }
  })
})

function renderSeeker({btnClick,btnActive,btnVerify}){
  btnClick.addEventListener('click',()=>{
    btnActive.classList.toggle('active')
    btnVerify == 'true'? btnVerify = false:null
  })
}

/**
 * 
 * @param {scroll del browser en general} winY 
 * @param {el alto de cada browser actual} browserHeight 
 */
function scroll_up(winY,browserHeight){
  const scrollUp = document.querySelector('.scroll-up')
  scrollUp.addEventListener('click',()=>{
    return winY > browserHeight? window.scroll({top:0,behaviot:'smooth'}):null
  })
}

/**
 * 
 * @param {posicion del scroll actual} sp 
 * @param {el ancho de cada browser actual} bw 
 */
function nav_flost(sp,bw){
  document.addEventListener('scroll',()=>{
    const whr = document.getElementById('whr')
    if((document.body.getBoundingClientRect()).top > sp && bw <= 480)
      whr.classList.remove('active')
    else
      whr.classList.add('active')
    sp = (document.body.getBoundingClientRect()).top
  })
}

function formarDateWhatsapp(){
  const data_href = document.querySelector('#data-whatsapp')
  const date = new Date()
  let hours = date.getHours()
  const amPm = hours >= 12 ? "PM":"AM"
  hours = hours % 12
  hours = hours ? hours:12
  let good;
  switch (true) {
    case hours <= 12 && amPm === 'PM':
      good = 'buenos tarde'
      break;
    case hours >= 6 && amPm === 'PM':
      good = 'buenos noche'
      break;
    default:
      good = 'buenos días'
      break;
  }
  let render = `${data_href.dataset.href}Hola muy ${good}, Señor Luis González. Necesito asesoría.`
  render = render.replaceAll(',','%2C').replaceAll('.','%2E').replaceAll(' ','%20')
  return data_href.setAttribute('href',render)
}
/**
 * 
 * @param {scroll del browser en general} y 
 * @param {el ancho de cada browser actual} bw 
 * @returns 
 */
function navbar (y,bw) {
  const nav = document.querySelector('#header-main .wrapper-header');
  return y > 100 && bw >= 480 ? nav.classList.add('activa'):nav.classList.remove('activa')
}
/**
 * 
 * @param {scroll del browser en general} y 
 * @param {el alto de cada browser actual} browserHeight 
 * @returns 
 */
function loadVideo (y,browserHeight){
  //1. saber el tamano del viewport
  //2. obtener el video.
  const video = document.querySelector('video')
  //4. Detectar ubicacion actual (top) con respecto al body
  const vidHeight = video.offsetHeight;
  const vidMax = video.offsetTop;
  const vidMin = video.offsetTop - browserHeight + vidHeight;
  return y > vidMin && y < vidMax ? video.play():video.pause()
}

function btnHambuerger () {
  const nav = document.querySelector('#hamburger button')
  const sidebar = document.querySelector('.navbar-custom')
  return nav.addEventListener('click', () =>{
    nav.classList.toggle('open')
    sidebar.classList.toggle('active')
  })
}

// const slider_box = document.querySelector('.slider-box')
// const item = document.querySelector('.slider-box .item-v1')
// function changesBox ($item,remove,trans = null,time = 5000) {
//   return new Promise((resolve,reject)=>{
//     setTimeout(()=>{
//       const slider = document.getElementById('slider')
//       const changes = slider_box.children.item(`${$item}`)
//       const removeChange = slider_box.children.item(`${remove}`)
//       img_slider_style(slider,trans)
//       resolve(box_slider(changes,removeChange))
//     },time)
//   })
// }
// const img_slider_style = (item,trans) => {
//   item.style.transform = `translateX(-${trans}px)`
//   item.style.transition = 'transform .3s linear'
// }
// const box_slider = (change,remove) =>{
//   remove.classList.remove('active--slider-box')
//   remove.children.item(0).classList.remove('fill-slider')
//   change.classList.add('active--slider-box')
//   change.children.item(0).classList.add('fill-slider')
// }
// function preload(){
//   const _width = document.documentElement.clientWidth
//   const _default = _width / 2
//   return changesBox(0,null,0,0)
//   .then(() => {return changesBox(1,0,_default)})
//   .then(() => {return changesBox(2,1,_default*2)})
//   .then(() => {return changesBox(3,2,_default*3)})
//   .then(() => {return changesBox(0,3)})
//   .then(() => {return preload()})

//   if(_width < 768){
//   }else{
//     return changesBox(0,null,0,0)
//     .then(() => {return changesBox(1,0,_default)})
//     .then(() => {return changesBox(2,1,_default*2)})
//     .then(() => {return changesBox(3,2,_default*3)})
//     .then(() => {return changesBox(0,3)})
//     .then(() => {return preload()})
//   }
// }