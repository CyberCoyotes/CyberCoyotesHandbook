# Issue 07

### Symptoms: 
Rev Sparkmax Motor Controll on PWM (the Spark) running (not full send) while other systems independent of the Spark are running.

### Fix: 
To turn off the Spark, use Spark.disable(). Setting power to 0 won't fix this.

### Why?
While uncertain, I theorize this is due to EMI. It would explain the incoherent movement of a PWM system while wires are practically wrapped around other CAN wires. Further, setting power to 0 didn't work, but disabling the Spark did, proving that **code is not the issue.** Disabling the Spark (and re-enabling via sending a signal with code) is likely a change on a code level and not an electrical one; that is, a disabled Spark doesn't care about signals received until it is the CODE that sends that signal.