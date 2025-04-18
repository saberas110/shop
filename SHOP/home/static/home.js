
const color_button = document.getElementById('color_button')
const color_i = document.getElementById('color_i')
const color = [...document.getElementsByName('color')]
const uniq_ides=JSON.parse(document.getElementById('index').textContent)
const comments = JSON.parse(document.getElementById('comments').textContent)
console.log('comments',comments)








function check_color_cart(color, product_id) {

    const uniq_id = `${product_id}-${color}`

    if (uniq_ides.includes(uniq_id)) {
        color_button.classList = "btn btn-lg w-100 border-0 main-color-two-bg"
        color_button.innerText = 'حذف از سبد خرید'
        color_button.appendChild(color_i)

    } else {
        color_button.className = "btn btn-lg w-100 border-0 main-color-three-bg"
        color_button.innerText = 'خرید کالا '
        color_i.className = "bi bi-basket text-white font-20 me-1 float-lg-end"
        color_button.appendChild(color_i)

    }

}

function add_delete_cart(product_id) {


    for (let i = 0; i < color.length; i++) {

        if (color[i].checked) {
            var color_select = color[i].value
        }
    }
    const u_id = `${product_id}-${color_select}`

    if (color_button.className == "btn btn-lg w-100 border-0 main-color-three-bg") {
        console.log('start')
        $.ajax({
            type: 'POST',
            url: `/orders/add/${product_id}`,
            data: {
                color: color_select,
                quantity: $('#quantity').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            }
        })
        color_button.classList = "btn btn-lg w-100 border-0 main-color-two-bg"

        color_button.innerText = 'حذف از سبد خرید'
        color_button.appendChild(color_i)
        console.log('before',uniq_ides)
        uniq_ides.push(u_id)
        console.log('after', uniq_ides)


    } else {
        $.get(`/orders/delete/${product_id}/${color_select}`).then(response => {

            console.log('delete')

            color_button.className = "btn btn-lg w-100 border-0 main-color-three-bg"
            color_button.innerText = 'خرید کالا '
            color_i.className = "bi bi-basket text-white font-20 me-1 float-lg-end"
            color_button.appendChild(color_i)
            const index = uniq_ides.indexOf(u_id)
            console.log('before', uniq_ides)
            uniq_ides.splice(index, 1)
            console.log('after', uniq_ides)

        })
    }
}


function like(product_id,comment_id) {
    const like_class = document.getElementById(`like ${comment_id}`)
    const like_number = document.getElementById(`like_number ${comment_id}`)

    const dislike_class = document.getElementById(`dislike ${comment_id}`)
    const dislike_number = document.getElementById(`dislike_number ${comment_id}`)

    $.get(`/product/comment/like/${product_id}/${comment_id}`).then(response =>{
    if (like_class.className == "bi bi-hand-thumbs-up" && dislike_class.className == "bi bi-hand-thumbs-down") {
        console.log('start like1')
        like_number.innerText = Number(like_number.innerText) + 1
        like_class.className = "bi bi-hand-thumbs-up-fill"

    } else if (like_class.className == "bi bi-hand-thumbs-up" && dislike_class.className == "bi bi-hand-thumbs-down-fill") {
        console.log('start like2')
        like_class.className = "bi bi-hand-thumbs-up-fill"
        like_number.innerText = Number(like_number.innerText) + 1
        dislike_class.className = "bi bi-hand-thumbs-down"
        dislike_number.innerText = Number(dislike_number.innerText) - 1

    } else if (like_class.className == "bi bi-hand-thumbs-up-fill") {
        console.log('start like3')
        like_number.innerText = Number(like_number.innerText) - 1
        like_class.className = "bi bi-hand-thumbs-up"
    }
})}

function dislike(product_id,comment_id){
    const like_class = document.getElementById(`like ${comment_id}`)
    const like_number = document.getElementById(`like_number ${comment_id}`)

    const dislike_class = document.getElementById(`dislike ${comment_id}`)
    const dislike_number = document.getElementById(`dislike_number ${comment_id}`)

    $.get(`/product/comment/dislike/${product_id}/${comment_id}`).then(response =>{


    if (like_class.className == "bi bi-hand-thumbs-up" && dislike_class.className == "bi bi-hand-thumbs-down"){
console.log('start dislike1')
        dislike_number.innerText = Number(dislike_number.innerText)+1
        dislike_class.className = "bi bi-hand-thumbs-down-fill"

    } else if (like_class.className == "bi bi-hand-thumbs-up-fill" && dislike_class.className == "bi bi-hand-thumbs-down") {
        console.log('start dislike2')
        like_class.className = "bi bi-hand-thumbs-up"
        like_number.innerText = Number(like_number.innerText) - 1
        dislike_class.className = "bi bi-hand-thumbs-down-fill"
        dislike_number.innerText = Number(dislike_number.innerText) + 1

    } else if (dislike_class.className == "bi bi-hand-thumbs-down-fill" ){
        console.log('start dislike3')
           dislike_class.className = "bi bi-hand-thumbs-down"
        dislike_number.innerText = Number(dislike_number.innerText) - 1
    }
})
}

function favorite_add_remove(product_id){
    $.get(`/product/favorites/add/${product_id}`).then(response =>{

        const favorite_button = document.getElementById('favorite')
        if (favorite_button.className == "bi bi-heart fs-4"){
            favorite_button.className = "bi bi-heart-fill fs-4"
        }else {
            favorite_button.className = "bi bi-heart fs-4"
        }
    })
}


function delete_favorite_inlist(product_id){
        $.get(`/product/favorites/add/${product_id}`).then(response =>{
        const div_favorite_list = document.getElementById(`delete-favorite ${product_id}`)
            div_favorite_list.remove()

    })
}






















