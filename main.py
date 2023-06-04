basic.show_string("shaimaa")
def on_button_pressed_a():   
    basic.show_icon(IconNames.HEART)
input.on_button_pressed(Button.A, on_button_pressed_a)
item = 0
def on_button_pressed_b():
    global item
    item +=1
    basic.show_number(item)
input.on_button_pressed(Button.B, on_button_pressed_b)
def on_gesture_shake():
       for i in range(11):
        basic.show_number(i)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
S=100
def on_button_pressed_ab():
 if S >=50:
    basic.show_string("pass")
 else:
  basic.show_string("fail")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

