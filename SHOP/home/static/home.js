
const color_button = document.getElementById('color_button')
const color_i = document.getElementById('color_i')
const color = [...document.getElementsByName('color')]
const uniq_ides=JSON.parse(document.getElementById('index').textContent)

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
