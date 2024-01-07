#NoEnv
SendMode Input
SetWorkingDir %A_ScriptDir%
initialN := 301  ; Initial value of n
n := initialN

; Hotkey, for example, Ctrl + Shift + X to start the script
^+x::
Loop
{
    if (n > initialN + 50)  ; Check if n has been incremented 50 times
    {
        break  ; Exit the loop
    }

    Loop, %n%
    {
        Send, {Up} ; Press Down key n times
        Sleep, 1 ; Pause for 2 seconds after each press
    }
    Send, {Enter} ; Press Enter key
    Sleep, 500 ; Pause for half a seconds
    Send, {Tab} ; Press Tab key
    Sleep, 500 ; Pause for half a seconds
    n := n + 1 ; Increment n
}
return

; Hotkey to stop the script, for example, Ctrl + Shift + Y
^+y::Reload
