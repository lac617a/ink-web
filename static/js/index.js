document.addEventListener('DOMContentLoaded',()=>{
  btnHambuerger();
  // preload();
  document.body.onscroll = ()=>{
    const y = window.pageYOffset;
    loadVideo(y)
    navbar(y)
  }
  formarDateWhatsapp()
})

function formarDateWhatsapp(){
  const data_href = document.querySelector('#data-whatsapp')
  const date = new Date()
  let hours = date.getHours()
  const amPm = hours >= 12 ? "PM":"AM"
  hours = hours % 12
  hours = hours ? hours:12
  let good;
  switch (true) {
    case hours >= 12:
      good = 'buenos tarde'
      break;
    case hours >= 6 && amPm === 'PM':
      good = 'buenos noche'
      break;
    default:
      good = 'buenos días'
      break;
  }
  let render = `${data_href.dataset.href}Hola muy ${good}, Señor Luis González, quisiera hacer una cotización. Espero su mensaje.&send?phone=+573002370341`
  render = render.replaceAll(',','%2C').replaceAll('.','%2E').replaceAll(' ','%20')
  return data_href.setAttribute('href',render)
}
function navbar (y) {
  const nav = document.querySelector('#header-main .wrapper-header');
  return y > 100 ? nav.classList.add('activa'):nav.classList.remove('activa')
}

function loadVideo (y){
  //1. saber el tamano del viewport
  let heightBrowser = window.innerHeight;
  //2. obtener el video.
  const video = document.querySelector('video')
  //4. Detectar ubicacion actual (top) con respecto al body
  const vidHeight = video.offsetHeight;
  const vidMax = video.offsetTop;
  const vidMin = video.offsetTop - heightBrowser + vidHeight;
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