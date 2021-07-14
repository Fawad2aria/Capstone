const TwoWayBinding = {
    data() {
        return {
            message: 'Hello vue!'
        }
    }
}
console.log('hello')
Vue.createApp(TwoWayBinding).mount('#two-way-binding')