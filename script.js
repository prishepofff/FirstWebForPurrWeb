let offset = 0;
const slider_line = document.querySelector('.slider__line')
const next = document.querySelector('.next')
const prev = document.querySelector('.prev')
let active=false
let all_img = document.querySelectorAll('.item')
let last_index = all_img.length-1
let index = 0
let prev_img
let main_img = document.querySelector(String('.'+all_img[0].classList[1]))
let next_img
let current_button = document.getElementById('0')
current_button.style.background = '#2d2d2d'

function animation_next(index_next_img){
    next_img = document.querySelector(String('.'+all_img[index_next_img].classList[1]))
    next_img.style.left = '512px'
    next_img.style.display = 'inline-block'
    current_button.style.background = ''
    current_button = document.getElementById(String(index_next_img))
    current_button.style.background = '#2d2d2d'
    let animation = setInterval(function () {
        offset -= 2
        slider_line.style.left = offset + 'px'
        if (offset === -512) {
            active = false
            clearInterval(animation)
            main_img.style.display='none'
            main_img = next_img
            main_img.style.left = '0'
            offset = 0
            slider_line.style.left = offset + 'px'
        }
    }, 2);
}
function animation_prev(index_prev_img){
    current_button.style.background = ''
    current_button = document.getElementById(String(index_prev_img))
    current_button.style.background = '#2d2d2d'
    prev_img = document.querySelector(String('.'+all_img[index_prev_img].classList[1]))
    prev_img.style.display='inline-block'
    prev_img.style.left = '-512px'
    let animation = setInterval(function () {
        offset += 2
        slider_line.style.left = offset + 'px'
        if (offset ===512) {
            active = false
            clearInterval(animation)
            main_img.style.display = 'none'
            main_img = prev_img
            main_img.style.left='0'
            offset = 0
            slider_line.style.left = offset + 'px'
        }
    }, 2);
}
function button_click(id){
    if (!active) {
        active = true
        if(index<id){
            animation_next(id)
        }
        else if(index>id){
            animation_prev(id)
        }
        else{active = false}
        index= Number(id)
    }
}

next.addEventListener('click', () => {
    if (!active) {
        active = true
        index+=1
        if(index>last_index){
            index=0
        }
        animation_next(index)
    }
})

prev.addEventListener('click', () => {
    if (!active) {
        active=true
        index-=1
        if(index<0){
            index=last_index
        }
        animation_prev(index)
    }
})
