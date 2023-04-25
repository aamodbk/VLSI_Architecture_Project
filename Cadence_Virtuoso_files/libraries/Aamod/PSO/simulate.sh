#!/bin/csh

echo "Starting The shell Script" 
date

cd /home/caduser1/
echo "Inside caduser1 . Sourcing Cshrc" 

source cshrc_hub
cd PSO_compound/cell1

echo "Inside PSO_compound/cell1" 

ocean -replay oceanscript.ocn

echo "done"
