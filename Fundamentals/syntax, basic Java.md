
<h2><b>Types and Privacy</b></h2>
<h4>Types are outlines for what data can mean. Privacy defines what conditions another object or member must meet to access or use it.</h4><br>

`[privacy] [type] [name]` <br>

`private string comedyGold = "fish";` Object that can only be accessed by members in the same class as `comedyGold`, describing a word. 
`public int beforeThree = 2;` Object available to **ALL** other parts of the code (with a few exceptions) that descibes a whole number. <br>
`public float beforeThreeAndAHalf = 3.499;` Object available to **ALL** other parts of the code (with a few exceptions) that descibes a number that can be a decimal or whole. <br>
`public boolean limeLightOn = false;` a true or false value, used for simple state. <br>
`public int[] numbers = new int[] {1, 4, 2, 19};` An array, a type of container for holding multiple of the same type. Max element count can't be changed after creation. <br>
`Double`: might as well be float, change as you need to for compatablility

<h2><b>Containers, Organization</b></h2>
<h4>Classes, Methods are important for organizing types and other method calls into groups.</h4>

<h3><b>Methods</b></h3>
Also known as functions, methods exist to perform a specific action. They can act on their own, or take and use extra <b>parameter</b> values. They can also return a type from them, making them act not only as an action, but also a way to get a new value, also having the choice to take parameters. Here's examples:

```
type can be void, meainng that it is only an action, and has no return value. 
[privacy] [type] [name](args) 
{
    [body]
}

public void SayHi()
{
    Console.print("Hi");
}


//private, so only the class this belongs to can call
private void Scream(string phrase,)
{
    Console.print(phrase.ToUpperCase());
}


private int WhatComesAfterThree()
{
    return 4;
}


public string ListInventory(string item, int count)
{

    return "We have " + count + " " + item + " left"
}
```

Calling a method is simple: 

```
int beforeFive = WhatComesAfterThree();
string report = ListInventory("apples", 5);
```


<h3><b>Operators</b></h3>
<h4>Math</h4>
```
+ : you already know
- : you already know
* : multiplication
/ : division
    With all of these above, you can do this to apply the operator to a variable.:
    int i = 10;
    i += 5;     //equals 15
    i -= 10;    //equals 5
    i *= 20;    //equals 100
    i /= 25;    //equals 4;
```

<h3><b>Classes</b></h3>
<h4>Classes define a group of code that fulfills one particular function; it's best to think of them as complex, user-defined types.</h4> <br>


```
public class Person()
{
 int age;
 string Name;

 

 private string Greet()
 {
    System.print("Hi! My name is " + Name);
 }   

//The following is a constructor. There can be more than one, and it serves only to initalize variables when the class is created.
 public Person(int _age, string _name)
 {
    this.age = _age;
    this.Name = _name;
 }

}
```

<h2> <b>Control Flow</b></h2>
Here are some more complex things you'll see: <br>

<b>foreach loops:</b>
Iterates over an array and acts on each element.
```
for (type var : array) 
{ 
    statements using var;
}

for (int i : numbers)
{
    //adds 5 to i; same as i = i + 5
    i += 5;
}
```

<br>
<b>For loops:</b>
Goes through a range of numbers, and does a particular action. Provides more control than a foreach.

```
//i++ is adding 1 to i
(int i = 0; i++; i < numbers.length)
{
    statement using i, possibly numbers[i] to access that array index
}
```
<br>