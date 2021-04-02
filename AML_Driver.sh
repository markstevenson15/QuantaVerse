numcores=$(sysctl -n hw.ncpu)
flength=$(cat ./transactions.csv | wc -l)
echo $flength
echo $numcores
intervals=$(expr $((flength / $numcores)))
echo $intervals
declare -a arr=()
for (( COUNTER=0; COUNTER<=$flength; COUNTER+=$intervals )); do
    arr+=($COUNTER $intervals )
done

printf '%d ' "${arr[@]}" | xargs -n2 -P$numcores python AML.py