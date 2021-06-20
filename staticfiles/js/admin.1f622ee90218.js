document.addEventListener('DOMContentLoaded',()=>{
  modal()
  // var formControlAll;
})

function modal(){
  const modalText = document.querySelector('.modal-text')
  const btnModal = document.querySelectorAll('.btn-modal')
  const closeModal = document.querySelector('.close')
  const modal = document.querySelector('.modal-custom')
  const modalC = document.querySelector('.modal-container')
  btnModal.forEach(btn=>{
    if(btn.classList.contains('modal-create')){
      btn.addEventListener('click',()=>{
        modalC.classList.add('is_active')
        modal.classList.toggle('modal-close')
        let url = btn.dataset.productUrl
        open_modal({get_url_id:url,render:modalText})
        document.body.style.overflow = 'hidden'
      })
    }else{
      btn.addEventListener('click',()=>{
        modalC.classList.add('is_active')
        modal.classList.toggle('modal-close')
        let url = btn.dataset.productUrl
        open_modal({get_url_id:url,render:modalText})
        document.body.style.overflow = 'hidden'
      })
    }
  })
  closeModal.addEventListener('click',()=>{
    modal.classList.toggle('modal-close')
    setTimeout(()=>{
      modalC.classList.remove('is_active')
      document.body.style.overflow = 'visible'
    },600)
  })
  window.addEventListener('click',(e)=>{
    if(e.target === modalC){
      modal.classList.toggle('modal-close')
      setTimeout(()=>{
        modalC.classList.remove('is_active')
        document.body.style.overflow = 'visible'
      },600)
    }
  })
}

/**
 *
 * @param {get_url_id} con este parametro obtendremos los id de cada producto para su edicion.
 * @param {render} Sera nuestro renderizador del formulario
 */
function open_modal({get_url_id = null,render}){
  const xhr = new XMLHttpRequest()
  const method = 'GET'
  const url = get_url_id
  const responseType = 'text'
  xhr.responseType = responseType
  xhr.open(method,url,true)
  xhr.onload = function(){
    if(this.readyState === 4)
      if(this.status === 200){
        let serverResponse = this.response
        render.innerHTML = serverResponse
      }else{console.log(this.status)}
  }
  xhr.send()
}
// formControlAll = document.getElementById('form-control-all')
// console.log(formControlAll)
// formControlAll.addEventListener('submit',send_form)
// function send_form(e){
//   e.preventDefault()
//   console.log(e.target)
// }