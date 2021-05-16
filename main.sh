#!/bin/sh



while true
do
    echo "Enter Lab ID"
    read lab_id
    

    case "$lab_id" in
    "1") echo "Running LAB 1 executable....." 
    cd LAB1
    ./regular
   ;;
   "2") echo "Running LAB 2 executable....." 
   cd LAB2
   ./count
   ;;
   "3") echo "Running LAB 3 executable....." 
   cd LAB3
   ./astar
   ;;
   "4") echo "Running LAB 4 executable....." 
   cd LAB4
   ./counter
   ;;
   "5") echo "Running LAB 5 executable....." 
   cd LAB5
   ./lowercase
   ;;
   "6") echo "Running LAB 6 executable....." 
   cd LAB6
   ./hexa
   ;;
   "7") echo "Running LAB 7 executable....." 
   cd LAB7
   ./add
   ;;
esac

done

    
