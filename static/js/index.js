document.addEventListener('DOMContentLoaded',()=>{
  btnHambuerger()
  preload()
})
function btnHambuerger () {
  const nav = document.querySelector('#hamburger button')
  const sidebar = document.querySelector('.navbar')
  nav.addEventListener('click', () =>{
    nav.classList.toggle('open')
    sidebar.classList.toggle('active')
  })
}

const slider_box = document.querySelector('.slider-box')
const item = document.querySelector('.slider-box .item-v1')

function changesBox ($item,remove,trans = null,time = 5000) {
  return new Promise((resolve,reject)=>{
    setTimeout(()=>{
      const slider = document.getElementById('slider')
      const changes = slider_box.children.item(`${$item}`)
      const removeChange = slider_box.children.item(`${remove}`)
      img_slider_style(slider,trans)
      resolve(box_slider(changes,removeChange))
    },time)
  })
}
const img_slider_style = (item,trans) => {
  item.style.transform = `translateX(-${trans}px)`
  item.style.transition = 'transform .3s linear'
}
const box_slider = (change,remove) =>{
  remove.classList.remove('active--slider-box')
  remove.children.item(0).classList.remove('fill-slider')
  change.classList.add('active--slider-box')
  change.children.item(0).classList.add('fill-slider')
}
function preload(){
  const _width = document.documentElement.clientWidth
  const _default = 659

  if(_width < 659){
    return changesBox(0,null,0,0)
    .then(() => {return changesBox(1,0,_width)})
    .then(() => {return changesBox(2,1,_width*2)})
    .then(() => {return changesBox(3,2,_width*3)})
    .then(() => {return changesBox(0,3)})
    .then(() => {return preload()})
  }else{
    return changesBox(0,null,0,0)
    .then(() => {return changesBox(1,0,_default)})
    .then(() => {return changesBox(2,1,_default*2)})
    .then(() => {return changesBox(3,2,_default*3)})
    .then(() => {return changesBox(0,3)})
    .then(() => {return preload()})
  }
}