from greenery import fsm, lego

A, B = range(2)
a,b="a","b"
# create the FSM
machine = fsm.fsm(
    alphabet = {a, b},
    states   = {A, B,},
    initial  = A,
    finals   = {A},
    map      = {
            A : {a: B, b: A},
            B : {a: A, b: B},
    },
)
rex = lego.from_fsm(machine)
print(machine)
print(rex)