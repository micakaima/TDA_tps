#!/bin/bash

TEST_DIR="tests"

echo -e "\tRESULTADOS\n" > salida.txt

for test_file in "$TEST_DIR"/*.txt; do
   
        test_name=$(basename "$test_file")
        echo -e "\n🏁 Prueba: $test_name$" >> salida.txt 
        
        #se saltea la primer linea de los tests que son comentarios
        tail -n +2 "$test_file" | python3 main.py >> salida.txt 
        
done

