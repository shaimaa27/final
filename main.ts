basic.showString("shaimaa")
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showIcon(IconNames.Heart)
})
let item = 0
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    item += 1
    basic.showNumber(item)
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    for (let i = 0; i < 11; i++) {
        basic.showNumber(i)
    }
})
let S = 100
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    if (S >= 50) {
        basic.showString("pass")
    } else {
        basic.showString("fail")
    }
    
})
