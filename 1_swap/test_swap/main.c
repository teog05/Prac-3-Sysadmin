#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char **argv) {
    size_t block_size = 1024 * 1024 * 1024; /* Bloques de 1GB */
    int i = 0;
    void *ptr;

    printf("Iniciando consumo de RAM para forzar el uso de Swap...\n");
    while (1) {
        ptr = malloc(block_size);
        if (ptr == NULL) {
            printf("Memoria máxima alcanzada. No se puede alojar más.\n");
            break;
        }
        memset(ptr, 1, block_size);
        i++;
        printf("Asignados y escritos %d GB\n", i);
        sleep(1);
    }
    return 0;
}
