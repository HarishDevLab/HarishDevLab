#Requires AutoHotkey v2.0
#SingleInstance Force
SendMode "Input"

; =========================
; WEAPON SWITCH (X)
; =========================
currentWeapon := 1

*e:: {
    global currentWeapon
    if (currentWeapon = 1) {
        Send "2"
        currentWeapon := 2
    } else {
        Send "1"
        currentWeapon := 1
    }
}

; =========================
; STATE-SAFE CYCLIC REMAP
; A → LShift → 3 → A
; =========================




; C -> 3
*$c:: {
    Send "{6 Down}"
}
*$c Up:: {
    Send "{6 Up}"
}


; =========================
; BIDIRECTIONAL REMAP
; Y ↔ F
; =========================

; Y -> F
*$v:: {
    Send "{f Down}"
}
*$v Up:: {
    Send "{f Up}"
}

; F -> Y
*$f:: {
    Send "{v Down}"
}
*$f Up:: {
    Send "{v Up}"
}
