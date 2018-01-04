# script to model/understand wait for a command to succeed pattern

interval=1
max_time=20
i=0
while true; do
    sleep $interval
    i=$((i+=$interval))
    echo $i
    test 10 == $i
    if (( $? == 0)); then
        echo "Command succeeeded, so break out of the loop."
        break
    fi
    if (( $i >= $max_time)); then
        echo "ERROR: timeout"
        exit 1
    fi
done
