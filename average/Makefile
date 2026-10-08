TARGET = average
ASM_SRC = main.asm
OBJ = main.o

NASM = nasm
ASM_FLAGS = -f elf64
LD = ld
INPUT = data.txt

all: $(TARGET)

$(TARGET): $(OBJ)
	$(LD) -o $@ $(OBJ)

$(OBJ): $(ASM_SRC)
	$(NASM) $(ASM_FLAGS) $< -o $@

run: $(TARGET)
	./$(TARGET) $(INPUT)

clean:
	rm -f $(OBJ) $(TARGET)

.PHONY: all run clean