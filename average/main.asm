section .bss
    buf resb 65536
    out_buf resb 32

section .data
    colon db ": "
    err db "файл испорчен", 10
    err_len equ $ - err

section .text
    global _start

_start:
    pop rdi
    cmp rdi, 2
    jl exit

    pop rdi
    pop r15           ; r15 = имя файла

    ; 1. Вывод префикса "<имя_файла>: "
    mov rsi, r15
    xor rdx, rdx
.len:
    cmp byte [rsi+rdx], 0
    je .len_done
    inc rdx
    jmp .len
.len_done:
    mov rax, 1
    mov rdi, 1
    syscall           ; sys_write(имя файла)

    mov rax, 1
    mov rsi, colon
    mov rdx, 2
    syscall           ; sys_write(": ")

    ; 2. Открытие и чтение файла целиком
    mov rax, 2
    mov rdi, r15
    xor rsi, rsi
    xor rdx, rdx
    syscall           ; sys_open
    cmp rax, 0
    jl error

    mov rdi, rax
    xor rax, rax
    mov rsi, buf
    mov rdx, 65536
    syscall           ; sys_read
    cmp rax, 0
    jle error         ; пустой файл -> ошибка

    ; 3. Парсинг данных
    mov rcx, rax      ; rcx = оставшиеся байты
    mov rsi, buf
    xor r8, r8        ; r8 = sum_x
    xor r9, r9        ; r9 = count_x
    xor r10, r10      ; r10 = sum_y
    xor r11, r11      ; r11 = count_y
    xor r12, r12      ; r12 = флаг строки (0 - X, 1 - Y)

parse:
    test rcx, rcx
    jz done
    movzx rdx, byte [rsi]
    inc rsi
    dec rcx

    ; Пропуск разделителей
    cmp dl, ' '
    je parse
    cmp dl, 9 ; /t
    je parse
    cmp dl, 13 ;/r
    je parse
    cmp dl, ','
    je parse
    cmp dl, 10 ;/n
    jne .chk_sign
    mov r12, 1        ; Перенос строки -> переключаемся на массив Y
    jmp parse

.chk_sign:
    mov r14, 1        ; Знак числа
    cmp dl, '-'
    jne .chk_dig
    mov r14, -1
    test rcx, rcx
    jz error
    movzx rdx, byte [rsi]
    inc rsi
    dec rcx

.chk_dig:
    cmp dl, '0'
    jl error
    cmp dl, '9'
    jg error
    xor r13, r13      ; Аккумулятор числа

.dig_loop:
    sub dl, '0'
    imul r13, 10
    movsx rdx, dl
    add r13, rdx

    test rcx, rcx
    jz .save
    movzx rdx, byte [rsi]
    cmp dl, '0'
    jl .save
    cmp dl, '9'
    jg .save
    inc rsi
    dec rcx
    jmp .dig_loop

.save:
    imul r13, r14
    test r12, r12
    jnz .y_line
    add r8, r13       ; Добавляем к сумме X
    inc r9
    jmp parse
.y_line:
    add r10, r13      ; Добавляем к сумме Y
    inc r11
    jmp parse

    ; 4. Финальный расчет
done:
    test r9, r9
    jz error          ; Нет чисел
    cmp r9, r11
    jne error         ; Разное количество чисел

    ; (sum_x - sum_y) / count
    sub r8, r10
    mov rax, r8
    cqo
    idiv r9

    ; 5. Вывод результата
    mov rsi, out_buf + 31
    mov byte [rsi], 10 ; /n
    xor r8, r8
    test rax, rax
    jns .pos
    neg rax
    inc r8
.pos:
    mov r9, 10
.div:
    dec rsi
    xor rdx, rdx
    div r9
    add dl, '0'
    mov [rsi], dl
    test rax, rax
    jnz .div

    test r8, r8
    jz .prt
    dec rsi
    mov byte [rsi], '-'
.prt:
    mov rdx, out_buf + 32
    sub rdx, rsi
    mov rax, 1
    mov rdi, 1
    syscall
    jmp exit

error:
    mov rax, 1
    mov rdi, 1
    mov rsi, err
    mov rdx, err_len
    syscall

exit:
    mov rax, 60
    xor rdi, rdi
    syscall